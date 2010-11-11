#!/usr/bin/env python

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


from pypvm_core import *
from pickle import dumps, loads

#PvmDataDefault = 0
#PvmDataRaw     = 1
#PvmDataInPlace = 2

#PvmTaskDefault = 0
#PvmTaskHost    = 1
#PvmTaksArch    = 2
#PvmTaskDebug   = 4
#PvmTaskTrace   = 8
#PvmMppFront    = 16
#PvmHostCompl   = 32

#PvmTaskExit   = 1
#PvmHostDelete = 2
#PvmHostAdd    = 3

#PvmRoute          = 1
#PvmDebugMask      = 2
#PvmAutoErr        = 3
#PvmOutputTid      = 4
#PvmOutputCode     = 5
#PvmTraceTid       = 6
#PvmTraceCode      = 7
#PvmFragSize       = 8
#PvmResvTids       = 9
#PvmSelfOutputTid  = 10
#PvmSelfOutputCode = 11
#PvmSelfTraceTid   = 12
#PvmSelfTraceCode  = 13
#PvmShowTids       = 14
#PvmPollType       = 15
#PvmPollTime       = 16

# ============================ pk () ==========================================
def pk (obj):
#  PRE: obj is assigned a Python object
# POST: obj has been packed into PVM send buffer
	pkstr (dumps (obj))

# ============================ upk () =========================================
def upk ():
# POST: FCTVAL == a Python object read from PVM receive buffer
	return (loads (upkstr ()))
