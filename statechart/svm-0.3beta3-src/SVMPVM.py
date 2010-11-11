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


import thread
import time
import ThreadUtil
from Clock import *

RESULT_OK                   = 0
RESULT_PVM_NOT_STARTED      = 5001
RESULT_DNS_NOT_STARTED      = 5002
RESULT_DNS_CONNECTION_ERROR = 5003

REQUEST_TIMEOUT             = 2    # timeout in seconds
CHECK_EVENT_INTERVAL        = 0.1

class SVMPVM_RECORD:
  pvm_started=0
  dns_started=0
  init_succ=0
  call_backs={}
  call_backs_lock=ThreadUtil.AllocateLock()
  
import pypvm
try:
  from PVMUtil import *
except:
  pass
SVMPVM_RECORD.myid=None

def build_port_list(eventhandler):
  ports={}
  for p in eventhandler.ports.keys():
    port={}
    port[PORT_IN]=eventhandler.ports[p][PORT_IN]
    port[PORT_OUT]=eventhandler.ports[p][PORT_OUT]
    ports[p]=port
  return ports

def check_kept_alive(newvalue=None):
  SVMPVM_RECORD.alive_lock.acquire()
  old_alive=SVMPVM_RECORD.is_kept_alive
  if newvalue!=None:
    SVMPVM_RECORD.is_kept_alive=newvalue
  SVMPVM_RECORD.alive_lock.release()
  return old_alive

def init_dns(eventhandler):
  # import pvm support
  try:
    SVMPVM_RECORD.myid=pypvm.mytid()
    SVMPVM_RECORD.pvm_started=1
    SVMPVM_RECORD.check_time={}
    SVMPVM_RECORD.dns_started=check_master_started()
    if SVMPVM_RECORD.dns_started:
      SVMPVM_RECORD.dnsid=get_master_id()
  except:
    pass

  if not SVMPVM_RECORD.pvm_started:
    return RESULT_PVM_NOT_STARTED
  if not SVMPVM_RECORD.dns_started:
    return RESULT_DNS_NOT_STARTED

  SVMPVM_RECORD.eventhandler=eventhandler
  SVMPVM_RECORD.alive_lock=ThreadUtil.AllocateLock()
  
  # Register to DNS
  if not send_object_with_confirm(SVMPVM_RECORD.dnsid, DnsEvent(REQUEST_TYPE, 'init'), REQUEST_TIMEOUT):
    return RESULT_DNS_CONNECTION_ERROR
  if not send_object_with_confirm(SVMPVM_RECORD.dnsid, DnsEvent(REQUEST_TYPE, 'init name', eventhandler.options[MODEL_NAME]), REQUEST_TIMEOUT):
    return RESULT_DNS_CONNECTION_ERROR
  ports=build_port_list(eventhandler)
  if not send_object_with_confirm(SVMPVM_RECORD.dnsid, DnsEvent(REQUEST_TYPE, 'init ports', ports), REQUEST_TIMEOUT):
    return RESULT_DNS_CONNECTION_ERROR

  # Start the keep-alive thread
  SVMPVM_RECORD.is_kept_alive=1
  ThreadUtil.StartThread(keep_alive, (eventhandler,))

  # Connect to other components
  for ck in eventhandler.required_components.keys():
    cid=ck
    send_object(SVMPVM_RECORD.dnsid, DnsEvent(REQUEST_TYPE, 'lookup', eventhandler.required_components[ck]))
    reply=recv_object(SVMPVM_RECORD.dnsid, DnsEvent(), REQUEST_TIMEOUT)
    if reply==None or reply.type!=ACCEPT_TYPE:
      return RESULT_DNS_CONNECTION_ERROR
    else:
      eventhandler.components[cid]=[]
      for rp in reply.param:
        if rp!=SVMPVM_RECORD.myid:
	  eventhandler.components[cid].append(rp)

  eventhandler.connections=establish_connections(eventhandler.components, eventhandler.required_connections, eventhandler.ports)

  ThreadUtil.StartThread(check_events, (eventhandler,))

  print 'init dns success (PID=%d)'%SVMPVM_RECORD.myid
  SVMPVM_RECORD.init_succ=1
  return RESULT_OK

def parse_ports(ports):
  if len(ports)!=2:
    return None
  pos1=find(ports[0], '.')
  pos2=find(ports[1], '.')
  if (pos1>=0 and pos2>=0) or (pos1<0 and pos2<0):
    return None
  if pos1>=0:
    comp=ports[0][:pos1]
    pcomp=ports[0][pos1+1:]
    pself=ports[1]
  else:
    comp=ports[1][:pos2]
    pcomp=ports[1][pos2+1:]
    pself=ports[0]
  return [comp, pcomp, pself]

def establish_connections(comp, reqconn, ports):
  connections={}
  for conn in reqconn:
    pp=parse_ports(conn)
    if not pp:
      print 'WARNING: Ignoring invalid connection %s.' % str(pp)
      continue
    [c, pc, ps]=pp
    if not comp.has_key(c):
      print 'WARNING: Component with identifier "%s" is not available.' % c
      continue
    for cid in comp[c]:  # by default, connect to all matched components
      if not send_object_with_confirm(SVMPVM_RECORD.dnsid, DnsEvent(REQUEST_TYPE, 'connect', [cid, pc, ps, ports[ps][PORT_IN], ports[ps][PORT_OUT]]), REQUEST_TIMEOUT):
        print 'WARNING: Cannot connect to port "%s" of component "%s" (PVM ID).' % (pc, str(cid))
      else:
	if ports[ps][PORT_IN]:
	  add_connection(connections, ps, cid, pc, 1)
	if ports[ps][PORT_OUT]:
	  add_connection(connections, ps, cid, pc, 0)
  return connections

def add_connection(connections, pcomp, pid, pself, is_in):
  if not connections.has_key(pcomp):
    connections[pcomp]=[]
  connections[pcomp].append([pid, pself, is_in])
  SVMPVM_RECORD.check_time[pid]=time.time()

def check_events(eventhandler):
  while check_kept_alive():
    reply=1
    external_queue=[]
    while 1:  # then handle other messages
      reply=recv_object(-1, DnsEvent(), 0)
      if not reply:
	break
      sender=reply.sender
      if reply.type==MREQUEST_TYPE and sender==SVMPVM_RECORD.dnsid:
	if reply.event=='connect':
	  # by default, accept all possible connection
	  # later version will contact DNS for security
	  [pcomp, id, pself, pin, pout]=reply.param
	  if eventhandler.ports.has_key(pcomp) and \
		 ((eventhandler.ports[pcomp][PORT_OUT] and pin) or \
		  (eventhandler.ports[pcomp][PORT_IN] and pout)):  # basic type checking
	    if eventhandler.ports[pcomp][PORT_OUT] and pin:
	      add_connection(eventhandler.connections, pcomp, id, pself, 0)
	    if eventhandler.ports[pcomp][PORT_IN] and pout:
	      add_connection(eventhandler.connections, pcomp, id, pself, 1)
	    send_object(SVMPVM_RECORD.dnsid, DnsEvent(ACCEPT_TYPE, 'connect', [id, pself]))
	    continue
	  send_object(SVMPVM_RECORD.dnsid, DnsEvent(REJECT_TYPE, 'connect', [id, pself]))
      elif reply.type==MEVENT_TYPE:
	ename=reply.event
	[pname, pc, params]=reply.param
	found=0
	if eventhandler.connections.has_key(pc):  # perform type checking
	  for pl in eventhandler.connections[pc]:
	    [pid, pp, is_in]=pl
	    if pid==sender and pname==pp and is_in:
	      found=1
	if found:
	  E=pc+'.'+ename
	  e=EventObject(E, sender)
	  func=None
	  SVMPVM_RECORD.call_backs_lock.acquire()
	  if SVMPVM_RECORD.call_backs.has_key(E) and len(SVMPVM_RECORD.call_backs[E])>0:
	    [func, eparams]=SVMPVM_RECORD.call_backs[E][0]
	    del SVMPVM_RECORD.call_backs[E][0]
	  SVMPVM_RECORD.call_backs_lock.release()
	  if func:
	    if not eparams:
	      eparams=[]
	    apply(func, [e, params]+eparams)
	  else:
	    eventhandler.event(e, params, 0)
      elif reply.type==MREQUEST_TYPE:
	if reply.event=='keep alive' and SVMPVM_RECORD.check_time.has_key(sender):
	  SVMPVM_RECORD.check_time[sender]=time.time()
	elif reply.event=='shutdown' and SVMPVM_RECORD.check_time.has_key(sender):
	  remove_component(eventhandler, sender)
	  
    time.sleep(CHECK_EVENT_INTERVAL)

def end_dns():
  if SVMPVM_RECORD.init_succ==1:
    check_kept_alive(0)
    if SVMPVM_RECORD.init_succ:
      send_object(SVMPVM_RECORD.dnsid, DnsEvent(REQUEST_TYPE, 'shutdown'))
      components=SVMPVM_RECORD.check_time.keys()
      mcast_object(components, DnsEvent(MREQUEST_TYPE, 'shutdown'))

def remove_expired(eventhandler):
  t=time.time()
  i=0
  ks=SVMPVM_RECORD.check_time.keys()
  while i<len(ks):
    k=ks[i]
    if t-SVMPVM_RECORD.check_time[k]>LIFE_TIME:
      remove_component(eventhandler, k)
    i=i+1

def remove_component(eventhandler, compid):
  del SVMPVM_RECORD.check_time[compid]
  for ck in eventhandler.connections.keys():
    c=eventhandler.connections[ck]
    i=0
    while i<len(c):
      [pid, pp, is_in]=c[i]
      if pid==compid:
        del c[i]
      else:
        i=i+1

def keep_alive(eventhandler):
  while check_kept_alive():
    time.sleep(LIFE_TIME/2)
    remove_expired(eventhandler)
    send_object(SVMPVM_RECORD.dnsid, DnsEvent(REQUEST_TYPE, 'keep alive'))
    components=SVMPVM_RECORD.check_time.keys()
    mcast_object(components, DnsEvent(MREQUEST_TYPE, 'keep alive'))

def send_external_event(eventhandler, event, receivers=None):
  influencees=[]
  if SVMPVM_RECORD.init_succ==1:
    E=str(event)
    pos=find(E, '.')
    if pos>=0:
      pname=E[:pos]
      ename=E[pos+1:]
    else:
      pname=E
      ename=''
    if 'params' in dir(event):
      params=event.params
    else:
      params=[]
    if eventhandler.connections.has_key(pname) and eventhandler.ports[pname][PORT_OUT]:
      rs=[]
      for [id, pc, is_in] in eventhandler.connections[pname]:
	if not is_in and (receivers==None or id in receivers):
	  rs.append(id)
      if rs:
        mcast_object(rs, DnsEvent(MEVENT_TYPE, ename, [pname, pc, params]))
	influencees=rs
  return influencees

def set_call_back(event_name, call_back_func, extra_params):
  SVMPVM_RECORD.call_backs_lock.acquire()
  if not SVMPVM_RECORD.call_backs.has_key(event_name):
    SVMPVM_RECORD.call_backs[event_name]=[]
  SVMPVM_RECORD.call_backs[event_name].append([call_back_func, extra_params])
  SVMPVM_RECORD.call_backs_lock.release()

def get_GUID():
  return SVMPVM_RECORD.myid
