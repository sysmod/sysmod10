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


import pypvm
import os
import sys
from Serialize import *
import thread
import ThreadUtil

PVM_lock = ThreadUtil.AllocateLock()

def find_temp_path():
  for p in sys.path:
    try:
      if "PVMUtil.py" in os.listdir(p):
        return p
    except:
      pass
  return os.path.split(sys.argv[0])[0]

TEMP_PATH      = find_temp_path()
MASTER_ID_FILE = os.path.join(TEMP_PATH, 'DNS')
PRINT_PREFIX   = ' |  '

# DNS Server Events
INTERNAL_TYPE  = '__INTERNAL_EVENT__'
REQUEST_TYPE   = '__CONNECTION_REQUEST__'
ACCEPT_TYPE    = '__ACCEPT__'
REJECT_TYPE    = '__REJECT__'
COMMAND_TYPE   = '__COMMAND__'

# Model Server Events
MREQUEST_TYPE  = '__MODEL_REQUEST__'
MEVENT_TYPE    = '__MODEL_EVENT__'

# Other Events
USER_TYPE      = '__USER_EVENT__'

# Internal Events
DNS_START   = 'start'
DNS_STARTED = 'started'
DNS_STOP    = 'stop'
DNS_STOPPED = 'stopped'
DNS_CHECK   = 'check'

# life time of a client without renewal (in seconds)
LIFE_TIME   = 30

class DnsEvent:
  def __init__(self, type=INTERNAL_TYPE, event=None, param=None):
    self.type=type
    self.event=event
    self.param=param
    self.sender=pypvm.mytid()

  def __str__(self):
    return serialize(self)

def get_master_id():
  PVM_lock.acquire()
  try:
    idf=open(MASTER_ID_FILE, 'r')
    id=int(idf.readline())
    idf.close()
  except:
    id=None
  PVM_lock.release()
  return id

def put_master_id():
  PVM_lock.acquire()
  id=pypvm.mytid()
  idf=open(MASTER_ID_FILE, 'w')
  idf.write('%s'%id)
  idf.close()
  PVM_lock.release()

def check_master_started():
  started=0
  try:
    id=get_master_id()
    started=(id!=None) and (pypvm.pstat(id)==0)
  except:
    pass
  return started

def send_string(id, s):
  PVM_lock.acquire()
  pypvm.initsend(pypvm.data['default'])
  pypvm.pkstr(s)
  pypvm.send(id, 1)
  PVM_lock.release()

def mcast_string(ids, s):
  PVM_lock.acquire()
  pypvm.initsend(pypvm.data['default'])
  pypvm.pkstr(s)
  pypvm.mcast(ids, 1)
  PVM_lock.release()

def send_object(id, obj):
  send_string(id, serialize(obj))

def mcast_object(ids, obj):
  mcast_string(ids, serialize(obj))

def send_object_with_confirm(id, obj, timeout=None):
  send_object(id, obj)
  reply=recv_object(id, DnsEvent(), timeout)
  if reply==None or reply.type!=ACCEPT_TYPE:
    return 0
  else:
    return 1

def send_acceptance(id):
  send_object(id, DnsEvent(ACCEPT_TYPE))

def send_rejection(id):
  send_object(id, DnsEvent(REJECT_TYPE))
  
def recv_string(id, timeout=None):
  PVM_lock.acquire()
  if timeout==None:
    pypvm.recv(id, -1)
  else:
    if not pypvm.trecv(timeout, -1, id):
      PVM_lock.release()
      return None
  reply=pypvm.upkstr()
  PVM_lock.release()
  return reply

def recv_object(id, reply, timeout=None):
  r=recv_string(id, timeout)
  if r==None:
    return None
  else:
    return deserialize(r, reply)
