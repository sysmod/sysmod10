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


import time
import code
import thread
import ThreadUtil
from SnapShot import *

class DummyClock:
  def acquire(self):
    pass
  def release(self):
    pass

clock_lock=ThreadUtil.AllocateLock()
start_lock=ThreadUtil.AllocateLock()

#======================================================================#
# Clock class

class Clock:
 """ The Clock is a scheduler running in another thread. When it is time
     to raise an event, it runs the function func with parameter param.
 """
 def __init__(self, eventhandler):
   start_lock.acquire()
   self.eventhandler=eventhandler
   self.interval=None
   self.func=None
   self.param=None
   self.stopped=1
   self.inter=0
   self.autostop=0
   self.extendedparam=0
   self.schedule_time=0
   self.first_interval=0
   start_lock.release()

 def start_ss(self, snapshot, func):
   start_lock.acquire()
   restore_snapshot(self, snapshot)
   self.func=func
   self.eventhandler.clocks.append(self)
   self.schedule_time=time.time()
   start_lock.release()
   try:
     ThreadUtil.StartThread(self.ClockThread, (self.interval, func, self.param, self.autostop, self.extendedparam, self.uselock))
   except:
     print 'WARNING: Could not start a new thread.'

 def start(self, interval, func, param, autostop=0, extendedparam=0, uselock=0):
   start_lock.acquire()
   self.interval=interval
   self.func=func
   self.param=param
   self.stopped=0
   try:
     self.inter=float(self.interval)
   except:
     self.inter=0
   self.autostop=autostop
   self.extendedparam=extendedparam
   self.uselock=uselock
   self.eventhandler.clocks.append(self)
   self.schedule_time=time.time()
   self.first_interval=None
   start_lock.release()
   try:
     ThreadUtil.StartThread(self.ClockThread, (self.interval, func, self.param, self.autostop, self.extendedparam, self.uselock))
   except:
     print 'WARNING: Could not start a new thread.'
 
 def remove(self):
   for i in range(len(self.eventhandler.clocks)):
     if self.eventhandler.clocks[i]==self:
       del self.eventhandler.clocks[i]
       break

 def stop(self):
   clock_lock.acquire()
   self.remove()
   self.schedule_time=None
   self.stopped=1
   clock_lock.release()
 
 def ClockThread(self, interval, func, param, autostop, extendedparam, uselock):
   if uselock:
     event_lock=ThreadUtil.AllocateLock()
   while not self.stopped:
     clock_lock.acquire()
     self.schedule_time=time.time()
     clock_lock.release()
     if self.first_interval:
       if self.first_interval>0:
         time.sleep(self.first_interval)
       self.first_interval=None
     else:
       self.inter=eval(str(interval), sys.modules['__main__'].__dict__)
       if self.inter>0:
         time.sleep(self.inter)
     if not self.stopped:
       if extendedparam:
	 if uselock:
	   event_lock.acquire()
	   apply(func, param+[event_lock])
	   event_lock.acquire()
	   event_lock.release()
	 else:
	   apply(func, param)
       else:
	 func(param)
     if autostop:
       self.stop()
       break
