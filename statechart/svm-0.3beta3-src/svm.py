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


from Exception import *
from Debugger import Debugger		# Debugger
from EventHandler import EventHandler
from Clock import Clock
import sys
import os
from StringUtil import *
from __version__ import version
import DefaultUI

# deceive the installer (to include the following modules in the distribution)
if 1==2:
  import PYPVM
  import random
  import pygame
  import whrandom

sys.path=[""]+sys.path

#======================================================================#
# Simulator

def print_usage():
  print '========================================================='
  print '|  Python Implementation of Statechart Virtual Machine  |'
  print '|                       Version 0.3 Beta3               |'
  print '|              Presented by Thomas Feng, Nov. 2003      |'
  print '========================================================='
  print ''
  print 'Usage: svm [options...] <.des|.snp file> [parameters...]'
  print '       options:'
  print '           -c: force curses interface (Linux)'
  print '           -t: force textual interface'
  print '           -i <file>: include a file (to the head)'
  print '           -I <file>: include a file (to the tail)'
  print '       parameters:'
  print '           "name=value"'

if len(sys.argv)<2:
  print_usage()
else:
  argn=1
  is_param=1
  use_gui=1
  haddition=[]
  taddition=[]

  # Check options here.
  while is_param and argn<len(sys.argv):
    arg=sys.argv[argn]
    if arg=='-t':
      argn=argn+1
      use_gui=0
    elif arg=='-c':
      argn=argn+1
      use_gui=2
    elif arg=='-i' and argn<len(sys.argv)-1:
      argn=argn+1
      haddition.append(sys.argv[argn])
      argn=argn+1
    elif arg=='-I' and argn<len(sys.argv)-1:
      argn=argn+1
      taddition.append(sys.argv[argn])
      argn=argn+1
    else:
      is_param=0

  if argn>=len(sys.argv):
    print_usage()
    exit

  desc=arg
  argn=argn+1
  debugger=Debugger()
  path_name=os.path.split(desc)
  addpath=path_name[0]
  name=path_name[1]
  if len(addpath)>0:
    sys.path=[addpath]+sys.path

  params={}
  while argn<len(sys.argv):
    arg=sys.argv[argn]
    argn=argn+1
    param=ParseOption(arg)
    if param!=None:
      par=ParseParameter(param[0])
      params[par[0]]=[par[1], param[1]]

  try:
    eventhandler=EventHandler(name, debugger.EventDebugger, params, use_gui, 1, haddition, taddition)

  except FileNotFound, e:
    print e
    raise SystemExit

  debugger.SetEventHandler(eventhandler)
  
  if eventhandler.description:
    print eventhandler.description
  eventhandler.run_initializer()
  eventhandler.run_interactor()
