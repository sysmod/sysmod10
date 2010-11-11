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


from thread import *

class WrappedLock:
  id_count=0
  
  def __init__(self, func=allocate_lock):
    self.lock=func()
    self.id=WrappedLock.id_count
    WrappedLock.id_count=WrappedLock.id_count+1

  def acquire(self):
    # print 'Acquire: %s'%self.id
    self.lock.acquire()

  def release(self):
    self.lock.release()
    # print 'Release: %s'%self.id

class FakedLock:
  def acquire(self):
    pass
  def release(self):
    pass

def StartThread(func, params=()):
  thread_lock.acquire()
  start_new_thread(thread_daemon, (func, params))

def AllocateLock(faked=0):
  if faked:
    return FakedLock()
  else:
    return WrappedLock()

def thread_daemon(func, params):
  thread_lock.release()
  apply(func, params)

thread_lock=AllocateLock()
