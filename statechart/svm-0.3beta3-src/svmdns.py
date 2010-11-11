#---------------------------------------------------------------------
#    SVM (Statechart Virtual Machine)
#         -- an interpreter for an extended statechart formalism
#---------------------------------------------------------------------
#
# Copyright (C) 2003 Thomas Huining Feng
#
#---------------------------------------------------------------------
# Address:      MSDL, SOCS, McGill Univ., Montreal, Canada
# HomePage:     http://msdl.cs.mcgill.ca/people/tfeng/
# SVM HomePage: http://msdl.cs.mcgill.ca/people/tfeng/?research=svm
# Download:     http://savannah.nongnu.org/files/?group=svm
# CVS:          :pserver:anoncvs@subversions.gnu.org:/cvsroot/svm
#               (projects "svm" and "jsvm")
# Email:        hfeng2@cs.mcgill.ca
#---------------------------------------------------------------------
#
# This file is part of SVM.
#
#---------------------------------------------------------------------
# SVM is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your
# option) any later version.
#
# SVM is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public
# License for more details.
#
# You should have received a copy of the GNU General Public License
# along with SVM; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
#---------------------------------------------------------------------


import sys
try:
  import pypvm
  from PVMUtil import *
  id=pypvm.mytid()
except:
  print "  PYPVM is not correctly installed.\n\
  Please refer to the README and INSTALL files for a solution."
  sys.exit(0)

from Serialize import *
from StringUtil import *
import os
import time
import code
import re
import whrandom
from string import *

SVMs={}
whrandom.seed()

def random_comp(a, b):
  return whrandom.randint(-1, 1)

def long_first_comp(a, b):
  if len(a)>len(b):
    return -1
  elif len(a)<len(b):
    return 1
  else:
    return cmp(a, b)

def remove_elements(list, e):
  i=0
  while i<len(list):
    if list[i]==e:
      del list[i]
    else:
      i=i+1

def parse_type(t):
  tt={PORT_IN:0, PORT_OUT:0, PORT_INOUT:0}
  tl=split(t, ' ')
  for i in tl:
    i=strip(i)
    k=tt.keys()
    k.sort(long_first_comp)
    for pt in k:
      if endswith(i, pt):
        num=i[0:len(i)-len(pt)]
        if not num:
	  num=1
        elif isint(num):
	  num=int(num)
        else:
	  break
        tt[pt]=tt[pt]+num
	break
  return tt

def count_ports(ports):
  pc={PORT_IN:0, PORT_OUT:0, PORT_INOUT:0}
  for p in ports.keys():
    if ports[p][PORT_IN] and ports[p][PORT_OUT]:
      pc[PORT_INOUT]=pc[PORT_INOUT]+1
    elif ports[p][PORT_IN]:
      pc[PORT_IN]=pc[PORT_IN]+1
    elif ports[p][PORT_OUT]:
      pc[PORT_OUT]=pc[PORT_OUT]+1
  return pc

def lookup_components(criteria):
  comps=SVMs.keys()
  comps.sort(random_comp)
  for c in criteria:
    if c[0]==COMPONENT_NAME:
      i=0
      while i<len(comps):
	id=comps[i]
	if not COMPONENT_NAME in SVMs[id].keys() or not re.match('\A'+c[1]+'\Z', SVMs[id][COMPONENT_NAME]):
	  remove_elements(comps, id)
	else:
	  i=i+1
    elif c[0]==COMPONENT_TYPE:
      t=parse_type(c[1])
      for id in SVMs.keys():
	match=0
	if COMPONENT_PORTS in SVMs[id].keys():
	  pt=SVMs[id][COMPONENT_PORTS]
	  pc=count_ports(pt)
	  match=t[PORT_IN]==pc[PORT_IN] and t[PORT_OUT]==pc[PORT_OUT] and t[PORT_INOUT]==pc[PORT_INOUT]
	if not match:
	  remove_elements(comps, id)
    elif c[0]==COMPONENT_KEYS: # not implemented yet
      pass
    else:
      return []
  return comps

def remove_expired():
  t=time.time()
  i=0
  ks=SVMs.keys()
  while i<len(ks):
    k=ks[i]
    if t-SVMs[k][COMPONENT_CHECKED]>LIFE_TIME:
      del SVMs[k]
      print PRINT_PREFIX+'Component %d is deleted from DNS because of timeout.'%k
    i=i+1

def handle_event(event):
  id=event.sender
  remove_expired()
  if event.type==REQUEST_TYPE:
    if event.event=='init':
      send_acceptance(id)
      SVMs[id]={COMPONENT_CHECKED:time.time()}
    elif event.event=='init name':
      if not SVMs.has_key(id):
	send_rejection(id)
        return
      send_acceptance(id)
      SVMs[id]['name']=event.param
    elif event.event=='init ports':
      if not SVMs.has_key(id):
	send_rejection(id)
        return
      send_acceptance(id)
      SVMs[id][COMPONENT_PORTS]=event.param
    elif event.event=='lookup':
      if not SVMs.has_key(id):
	send_rejection(id)
        return
      criteria=event.param
      components=lookup_components(criteria)
      send_object(id, DnsEvent(ACCEPT_TYPE, None, components))
    elif event.event=='keep alive':
      if SVMs.has_key(id):
	SVMs[id][COMPONENT_CHECKED]=time.time()
    elif event.event=='connect':
      if SVMs.has_key(id):
	[comp, pcomp, pself, pin, pout]=event.param
	send_object(comp, DnsEvent(MREQUEST_TYPE, 'connect', [pcomp, id, pself, pin, pout]))
        print PRINT_PREFIX+'Relayed connection request: '+str(event.param)
    elif event.event=='shutdown':
      if SVMs.has_key(id):
	del SVMs[id]
  elif event.type==ACCEPT_TYPE:
    if event.event=='connect':
      [pid, pself]=event.param
      send_object(pid, DnsEvent(ACCEPT_TYPE, 'connect', pself))
      print PRINT_PREFIX+'Accepted connection request: '+str(event.param)
  elif event.type==REJECT_TYPE:
    if event.event=='connect':
      [pid, pself]=event.param
      send_object(pid, DnsEvent(REJECT_TYPE, 'connect', pself))
      print PRINT_PREFIX+'Rejected connection request: '+str(event.param)

def get_executable():
  e1=sys.executable
  e2=sys.argv[0]
  if e1==e2:
    return [e1, [e1]]
  else:
    return [e1, [e1, e2]]

l=len(sys.argv)
if l==1:
  sys.__stdout__.write('SVM DNS User Interface\n')
  started=check_master_started()
  if started:
    print PRINT_PREFIX+'SVM DNS is already running.'
  else:
    print PRINT_PREFIX+'SVM DNS is not running.'
  s=''
  [pexec, pargv]=get_executable()
  while not s in ['exit', 'quit']:
    if s:
      if s in ['start'] and not started:
	id=pypvm.mytid()
        os.spawnvp(os.P_NOWAIT, pexec, pargv+ParseArgv(s)+[str(id)])
	reply=DnsEvent()
	while reply.type!=INTERNAL_TYPE or reply.event!=DNS_STARTED:
	  recv_object(-1, reply)
	started=1
      else:
        os.spawnvp(os.P_WAIT, pexec, pargv+ParseArgv(s))
    started=check_master_started()
    sys.__stdout__.write('>>> ')
    s=strip(sys.__stdin__.readline())
  
elif sys.argv[1] in ['-h', '--h', '-help', '--help', 'help', '-?'] and l==2:
  print PRINT_PREFIX+'Statechart Virtual Machine Dynamic Naming System'
  print PRINT_PREFIX+'USAGE:'
  print PRINT_PREFIX+'  svmdns <param>'
  print PRINT_PREFIX+'PARAMETERS:'
  print PRINT_PREFIX+'  help          print this help message'
  print PRINT_PREFIX+'  check         check if DNS has been started'
  print PRINT_PREFIX+'  exec "cmd"    execute a python command on the DNS (quotes are removed)'
  print PRINT_PREFIX+'  send "msg"    sends msg to the DNS (quotes are removed)'
  print PRINT_PREFIX+'  start         starts the DNS'
  print PRINT_PREFIX+'  stop          stops the DNS'

elif sys.argv[1]=='check' and (l==2 or (l==3 and isint(sys.argv[2]))):
  started=check_master_started()
  if started:
    if l==3:
      tid=int(sys.argv[2])
      send_object(tid, DnsEvent(INTERNAL_TYPE, DNS_STARTED))
    else:
      print PRINT_PREFIX+'SVM DNS is already running.'
  else:
    if l==3:
      tid=int(sys.argv[2])
      send_object(tid, DnsEvent(INTERNAL_TYPE, DNS_STOPPED))
    else:
      print PRINT_PREFIX+'SVM DNS is not running.'
    
elif sys.argv[1]=='start' and (l==2 or (l==3 and isint(sys.argv[2]))):
  if check_master_started():
    print PRINT_PREFIX+'SVM DNS is already running.'
  else:
    put_master_id()

    print PRINT_PREFIX+'DNS program starts.'
    if l==3:
      tid=int(sys.argv[2])
      send_object(tid, DnsEvent(INTERNAL_TYPE, DNS_STARTED))

    finished=0
    while not finished:
      reply=recv_object(-1, DnsEvent())
      print PRINT_PREFIX+'DNS program received "%s" of type "%s".' % (reply.event, reply.type)
      if reply.type==INTERNAL_TYPE and reply.event==DNS_STOP:
        if isint(reply.param):
	  send_object(int(reply.param), DnsEvent(INTERNAL_TYPE, DNS_STOPPED))
        pypvm.exit()
        print PRINT_PREFIX+'DNS program exits.'
        finished=1
      elif reply.type==COMMAND_TYPE:
        ii=code.InteractiveInterpreter(locals())
	try:
	  ii.runsource(reply.event)
	except:
	  1
      else:
	handle_event(reply)
      
elif sys.argv[1]=='stop' and l==2:
  if not check_master_started():
    print PRINT_PREFIX+'SVM DNS is not running.'
  else:
    id=get_master_id()
    myid=pypvm.mytid()
    send_object(id, DnsEvent(INTERNAL_TYPE, DNS_STOP, myid))
    reply=DnsEvent()
    while reply.type!=INTERNAL_TYPE or reply.event!=DNS_STOPPED:
      recv_object(id, reply)
    pypvm.exit()

elif sys.argv[1]=='send' and l==3:
  msg=sys.argv[2]
  id=get_master_id()
  send_object(id, DnsEvent(USER_TYPE, msg))
  pypvm.exit()

elif sys.argv[1]=='exec' and l==3:
  cmd=sys.argv[2]
  id=get_master_id()
  send_object(id, DnsEvent(COMMAND_TYPE, cmd))
  pypvm.exit()
  
else:
  print PRINT_PREFIX+'Parameter(s) not recognized.'
