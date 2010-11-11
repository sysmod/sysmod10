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
import time
from code import InteractiveInterpreter
import ThreadUtil

from DefaultUI import *

from string import *

try:
  import curses
except:
  pass

class Interpreter (InteractiveInterpreter):
  def __init__(self, output_method=None):
    InteractiveInterpreter.__init__(self, sys.modules['__main__'].__dict__)
    if output_method:
      self.output=output_method
    else:
      self.output=self.default_output

  def write(self, data):
    self.output(data)
  
  def default_output(self, data):
    usecurses=DefaultCurses.stdscr!=None
    if usecurses:
      DefaultCurses.stdscr.addstr(data)
    else:
      sys.__stdout__.write(data)

DefaultInterpreter=Interpreter()

class Debugger:

  def __init__(self):
    self.trace_list=[]
    self.interrupt_list=[]
    self.custom_list=[]
    self.eventhandler=None
    self.EventDebugger=self.TextEventDebugger

  def SetEventHandler(self, eventhandler):
    self.eventhandler=eventhandler

  def TraceEvent(self, event=None, before=-1, oldstate='', newstate=''):
    self.trace_list.append({'E':event, 'B':before, 'O':oldstate, 'N':newstate})

  def InterruptEvent(self, event=None, before=-1, oldstate='', newstate=''):
    self.interrupt_list.append({'E':event, 'B':before, 'O':oldstate, 'N':newstate})
  
  def CustomizeEvent(self, callback, event=None, before=-1, oldstate='', newstate=''):
    self.custom_list.append({'C':callback, 'E':event, 'B':before, 'O':oldstate, 'N':newstate})

  def CheckEvent(self, event, before, oldstate, newstate, elist, run_callback=0):
    """ before: a flag indicating the point where the event handler is in.
                -1: the event handler is starting; it still doesn't know whether the transition
                    will take place or not (so the oldstate and newstate had no meaning);
                    in this case, the event can be cancelled;
                 0: the event handler decided to make a transition; the transition is about to
                    take place;
                 1: the event handler decided to make a transition; the transition has been
                    complished.
    """
    found=0
    if self.eventhandler!=None:
      for i in elist:
        if (i['E']==event or i['E']==None) \
           and (before==None or i['B']==before) \
           and (oldstate==None or self.eventhandler.is_or_is_substate(oldstate, i['O'])) \
           and (newstate==None or self.eventhandler.is_or_is_substate(newstate, i['N'])):
          if not run_callback:
            return 1
          else:
            found=1
            i['C'](event, before, oldstate, newstate)
    return found
  
  def OutputTraceEvent(self, event, oldstate, newstate):
    DefaultInterpreter.write('Debugger: (Trace)\n')
    DefaultInterpreter.write('  Event \''+event+'\' occurred.\n')
    DefaultInterpreter.write('  Old state: '+str(oldstate)+'\n')
    DefaultInterpreter.write('  New state: '+str(newstate)+'\n')
    DefaultInterpreter.write('  Current state of the event handler:\n    '+str(self.eventhandler.state)+'\n')

  def OutputLeaveMessage(self):
    DefaultInterpreter.write('On leaving interrupt mode, the program is re-activated.\n')

  def OutputInterruptLogo(self, event):
    DefaultInterpreter.write('Debugger: (Interrupt)\n')
    DefaultInterpreter.write('  (Pseudo) Event \''+event+'\' occurred.\n')
    DefaultInterpreter.write('Interrupt mode: enter command \'exit\' to leave.\n')
  
  def TextEventDebugger(self, event, before=None, oldstate=None, newstate=None):
    self.CheckEvent(event, before, oldstate, newstate, self.custom_list, 1)
    if self.CheckEvent(event, before, oldstate, newstate, self.trace_list):
      self.OutputTraceEvent(event, oldstate, newstate)
    if self.CheckEvent(event, before, oldstate, newstate, self.interrupt_list):
      self.OutputInterruptLogo(event)
      lastprompt=''
      usecurses=DefaultCurses.stdscr!=None
      old_stdout=sys.__stdout__
      sys.stdout=DefaultInterpreter
      while 1:
        if not lastprompt:
	  if usecurses:
	    DefaultCurses.stdscr.addstr('>>> ', curses.color_pair(2))
	  else:
            sys.__stdout__.write('>>> ')
        else:
	  if usecurses:
	    DefaultCurses.stdscr.addstr('... ', curses.color_pair(2))
	  else:
            sys.__stdout__.write('... ')
	if usecurses:
	  #prompt=DefaultCurses.stdscr.getstr()
	  prompt=DefaultCurses.curses.curses_get_str(1)
	else:
          prompt=rstrip(sys.__stdin__.readline())
        if prompt=='exit':
          break;
        if lastprompt:
          cmd=lastprompt+'\n'+prompt
        else:
          cmd=prompt
        lastprompt=self.RunSource(cmd)
      sys.stdout=old_stdout
      self.OutputLeaveMessage()
    return 1
  
  def RunSource(self, source):
    if not source:
      return ''
    else:
      err=DefaultInterpreter.runsource(source)
      if err==1:
        return source
      else:
        return ''
  
  def CheckSource(self, source):
    try:
      if DefaultInterpreter.compile(source)!=None:
        err=1
      else:
        err=2
    except:
      err=3
    return err

class EmptyOutput:
  def write(self, data):
    return
