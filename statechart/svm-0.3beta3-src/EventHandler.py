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
import time
from copy import *
import types
from string import *
import thread
import sys
import os.path
import DefaultUI
from SnapShot import *

from Debugger import Debugger		# Debugger
from Debugger import DefaultInterpreter
from Clock import *

from StringUtil import *
if 1==2:
  from SVMPVM import *
  #from SVMCORBA import *
import ThreadUtil

vtest=1
internal_prefix=0

class Cache:
  DesCache={}

#======================================================================#
# General event handler class

class EventHandler:
 " Eventhandler class represents the simulator which interprets the model. "

 def __init__(self, filename, callback=None, param={}, use_gui=0, top_level=1, haddition=[], taddition=[], autoinit=1, modeltext=None, global_options=None):
   """ filename: the description file (probably .des) to load
       callback: the callback function to be called before and after a state change
   """
   self.finished=0
   self.Started=0
   self.top_level=top_level
   self.param=param
   self.callback=callback
   self.internal_num=0
   self.use_gui=use_gui
   self.clocks=[]
   self.modeltext=modeltext
   self.restored=0
   self.local_restored=0
   self.ttrans={}
   self.ports={}
   self.haddition=haddition
   self.taddition=taddition
   self.event_object=None
   self.event_list=[]
   self.event_lock=ThreadUtil.AllocateLock()
   self.handle_event_lock=ThreadUtil.AllocateLock()
   self.snapshot_requests=[]
   self.snapshot_requests_lock=ThreadUtil.AllocateLock()
   self.seq_snapshots={}
   self.seq_snapshots_lock=ThreadUtil.AllocateLock()
   self.snapshot_retrieve=None
   self.snapshot_retrieve_lock=ThreadUtil.AllocateLock()
   self.empty_event_signal=None
   self.empty_event_signal_lock=ThreadUtil.AllocateLock()
   self.outgoing_table={}
   self.future_events={}
   self.event_log={}
   self.encapsulated_components={}
   self.skewed_event=None
   self.influencees={}
   self.has_interactor=0
   global internal_prefix
   self.internal_prefix=internal_prefix
   internal_prefix=internal_prefix+1
   DefaultInterpreter.runsource('import EventHandler');
   DefaultInterpreter.runsource('from SnapShot import *');
   DefaultInterpreter.runsource('from DefaultUI import *');

   self.load_statechart(filename, global_options)
   if not self.restored and autoinit:
     self.state=self.find_initial_state(self.stateH)
   # The state attribute defines the current state. It is a list,
   # because there may be concurrency in the statechart.

 def is_final_state(self):
   for s in self.state:
     path=split(s, '.')
     states=self.stateH
     for p in path:
       if states[p][FINAL_STATE]:
         return 1
       states=states[p]
   return 0

 def find_initial_state(self, stateH, path=''):
   """ To find the initial state(s) in the state hierachy, stateH.
   """
   states=[]
   keys=stateH.keys()
   keys.sort()
   for s in keys:
     if not s in StateProperties:
       if stateH[s][DEFAULT_STATE]:
         newstateH=stateH[s]
         self.check_import(path, s, newstateH, 0)
         ds=self.find_initial_state(newstateH, self.append_path(path, s))
         if len(ds)==0:
           states.append(s)
         else:
           for d in ds:
             states.append(self.append_path(s, d))
   return states

 def is_or_is_substate(self, state1, state2):
   """ Return 1 if state1 is or is a substate of state2; 0 otherwise.
   """
   if state2=='' or (find(state1, state2)==0 and (len(state1)==len(state2) or state1[len(state2)]=='.')):
     return 1
   else:
     return 0

 def get_state_property(self, state, prop):
   st=split(state, '.')
   states=self.stateH
   for s in st:
     states=states[s]
   return states[prop]

 def record_state(self, state):
   self.history[state]=[]
   deep=self.get_state_property(state, DEEP_HISTORY_STATE)
   for s in self.state:
     if self.is_or_is_substate(s, state) and s!=state:
       tail=s[len(state)+1:len(s)]
       if deep or find(tail, '.')==-1:
         if not s in self.history[state]:
           self.history[state].append(s)
       else:
         ns=s[0:len(state)+1]+tail[0:find(tail, '.')]
         if not ns in self.history[state]:
           self.history[state].append(ns)

 def record_path(self, common, bottom, states_recorded):
   if common:
     com_split=split(common, ".")
   else:
     com_split=[]
   bot_split=split(bottom, ".")
   i=len(com_split)
   if i>0:
     i=i-1
     path=join(com_split[:i], ".")
   else:
     path=common
   while i<len(bot_split):
     if path:
       path=self.append_path(path, bot_split[i])
     else:
       path=bot_split[i]
     if self.get_state_property(path, HISTORY_STATE) and not path in states_recorded:
       self.record_state(path)
       states_recorded.append(path)
     i=i+1

 def record_history(self, oldstate, newstate):
   common=self.common_state(oldstate, newstate)
   states_recorded=[]
   for s in self.state:
     if not common or self.is_or_is_substate(s, common):
       self.record_path(common, s, states_recorded)

 def check_time_transition(self, state, check_created=1, common_state=None):
   for k in self.ttrans.keys():
     if self.is_or_is_substate(state, k) and (common_state==None or not self.is_or_is_substate(common_state, k)):
       if check_created:
         created=0
         for st in self.state:
           if self.is_or_is_substate(st, k):
             created=1
             break
         if created:
            continue
       for j in range(len(self.ttrans[k])):
         if self.ttrans[k][j][2]!=None:
           self.ttrans[k][j][2].stop()
         tname=self.ttrans[k][j][0]		# transition name
         ttime=self.ttrans[k][j][1]
         clock=Clock(self)
         if self.ttrans[k][j][3]:		# repeated or not
           self.ttrans[k][j][2]=clock	# Clock object
         clock.start(ttime, self.event, [EventObject(tname), [], 1], not self.ttrans[k][j][3], 1, 1)

 def remove_time_transition(self, state):
   for k in self.ttrans.keys():
     if self.is_or_is_substate(k, state):
       for j in range(len(self.ttrans[k])):
         if self.ttrans[k][j][2]!=None:
           self.ttrans[k][j][2].stop()
           self.ttrans[k][j][2]=None

 def common_state(self, state1, state2):
   if state1==state2:
     if self.options[HAREL]=='0' or self.get_state_property(state1, HISTORY_STATE):
       # if simply return state1, transition from A to A does not execute enter/exit actions (new style)
       return state1
     else:
       # if return the parent of state1 (or state2), the semantics is Harel's
       pos=rfind(state1, '.')
       if pos>=0:
         return state1[:pos]
       else:
         return ''
   elif len(state2)>len(state1) and state2[0:len(state1)+1]==state1+'.':
     return state1
   elif len(state2)<len(state1) and state1[0:len(state2)+1]==state2+'.':
     return state2
   start=find(state1, '.')
   last=0
   while start>=0 and start<len(state1) and start<len(state2):
     if state2[start]=='.' and state1[0:start]==state2[0:start]:
       last=start
       start=find(state1, '.', start+1)
     else:
       break
   return state1[0:last]

 def enter_transition_rec(self, states, path, finalpath, test_only):
   found=0
   keys=states.keys()
   keys.sort()
   for s in keys:
     if not s in StateProperties:
       newpath=self.append_path(path, s)
       if not finalpath or self.is_or_is_substate(finalpath, newpath):
         found=self.enter_transition_rec(states[s], newpath, finalpath, 1) or found
         if found:
           break
   if not found:
     found=path in self.state
   if found and not test_only:
     if self.enter.has_key(path):
       outputs=self.enter[path]
       for o in outputs:
         if o.has_key('C'):		# If there is a condition defined
           DefaultInterpreter.runsource(o['C'])
           if not vtest:
             continue
         if o.has_key('O'):
           self.outputFnc(o['O'])
     for s in keys:
       if not s in StateProperties:
         newpath=self.append_path(path, s)
         if not finalpath or self.is_or_is_substate(finalpath, newpath):
           found=self.enter_transition_rec(states[s], newpath, finalpath, 0)
   return found

 def exit_transition_rec(self, states, path, finalpath):
   found=0
   keys=states.keys()
   keys.sort()
   for s in keys:
     if not s in StateProperties:
       newpath=self.append_path(path, s)
       if not finalpath or self.is_or_is_substate(newpath, finalpath):
         found=self.exit_transition_rec(states[s], newpath, finalpath) or found
   if not found:
     found=path in self.state
   if found:
     if self.exit.has_key(path):
       outputs=self.exit[path]
       for o in outputs:
         if o.has_key('C'):		# If there is a condition defined
           DefaultInterpreter.runsource(o['C'])
           if not vtest:
             continue
         if o.has_key('O'):
           self.outputFnc(o['O'])
   return found

 def enter_exit_transition(self, oldstate, newstate, is_exit, restricted=0):
   """
   If restricted, only the enter/exit actions of newstate's parents are executed
   """
   common=self.common_state(oldstate, newstate)
   comset=split(common, '.')
   states=self.stateH
   for c in comset:
     if c!='':
       states=states[c]
   keys=states.keys()
   keys.sort()
   for s in keys:
     if not s in StateProperties:
       path=self.append_path(common, s)
       if self.is_or_is_substate(newstate, path) or self.is_or_is_substate(path, newstate):  # modified
         if not is_exit:
           if restricted:
             self.enter_transition_rec(states[s], path, newstate, 0)
           else:
             self.enter_transition_rec(states[s], path, None, 0)
         else:
           if restricted:
             self.exit_transition_rec(states[s], path, newstate)
           else:
             self.exit_transition_rec(states[s], path, None)

 def sort_substate_first(self, sa, sb):
   if sa==sb:
     return 0
   elif self.is_or_is_substate(sa, sb):
     return 1
   else:
     return -1
 
 def change_state(self, oldstate, newstate, history=0, output_actions=None):
   """ Change the state from oldstate to newstate.
       It is the user's business to be sure the model is currently in the specified old state,
       and the state change is meaningful.
   """
   self.record_history(oldstate, newstate)
   enabled=0
   delstate=[]

   if self.options[HAREL]=='1' and output_actions:  # Harel's semantics
     self.outputFnc(output_actions)

   common_state=self.common_state(oldstate, newstate)
   for s in self.state:
     if s!=common_state and self.is_or_is_substate(s, common_state):
       enabled=1
       delstate.append(s)
   if enabled:
     self.enter_exit_transition(newstate, oldstate, 1)

   if self.options[HAREL]=='0' and output_actions:  # not Harel's semantics
     self.outputFnc(output_actions)

   if enabled:
     for s in delstate:
       self.remove_time_transition(s)
       del self.state[FindInList(self.state, s)]
     if history and self.get_state_property(newstate, HISTORY_STATE) \
                and self.history.has_key(newstate) and len(self.history[newstate])>0:
       newstates=self.history[newstate]
       if self.get_state_property(newstate, DEEP_HISTORY_STATE):
         self.state=self.state+newstates
         self.state.sort()
         return
     else:
       newstates=[newstate]
     newstates.sort(self.sort_substate_first)
     for n in newstates:
       paths=split(n, '.')
       path=''
       oldpath=''
       for p in range(0, len(paths)):
         oldpath=path
         path=self.append_path(path, paths[p])
         found=0
         for p2 in self.state:	# O(n**2) of course is not a very good solution
           if self.is_or_is_substate(p2, path):
             found=1
         if not found:
           break
       state=self.stateH
       for i in range(0, p):
         state=state[paths[i]]
       self.add_states_to_path(oldpath, paths, p, state, common_state)
     self.enter_exit_transition(oldstate, newstate, 0)
   self.state.sort()

 def append_path(self, path1, path2):
   """ Append sub-path path2 to path1
   """
   if path1=='':
     return path2
   else:
     return path1+'.'+path2

 def reorder_transitions_rec(self, path, s, states, IFS):
   IFS2=IFS
   if states[INNER_TRANSITION_FIRST]:
     IFS2=1
   elif states[OUTER_TRANSITION_FIRST]:		# there may be conflict here
     IFS2=0
   elif states[REVERSE_TRANSITION_ORDER]:
     IFS2=not IFS2
   if IFS2!=IFS:
     self.reorder_transitions_for_state(path, IFS2)
   keys=states.keys()
   keys.sort()
   for s2 in keys:
     if not s2 in StateProperties:
       self.reorder_transitions_rec(self.append_path(path, s2), s2, states[s2], IFS2)

 def is_ifs(self, path):
   IFS=(self.options[INNER_FIRST]=='1')		# modify later
   if path=='':
     return IFS
   paths=split(path, '.')
   states=self.stateH
   for s in paths:
     states=states[s]
     if states[INNER_TRANSITION_FIRST]:
       IFS=1
     elif states[OUTER_TRANSITION_FIRST]:		# there may be conflict here
       IFS=0
     elif states[REVERSE_TRANSITION_ORDER]:
       IFS=not IFS
   return IFS
 
 def remove_final_states(self, stateH, found=0):
   keys=stateH.keys()
   keys.sort()
   for s in keys:
     if not s in StateProperties:
       if stateH[s][FINAL_STATE]:
         if not found:
           sys.stderr.write('WARNING: Imported model has final states. They are automatically converted to ordinary states.\n')
           found=1
         stateH[s][FINAL_STATE]=0
       found=self.remove_final_states(stateH[s])
   return found

 def dump_trans(self):
   print "///"
   for e in self.trans.keys():
     print e
     for t in self.trans[e]:
       print "  "+t['S']
   print "\\\\\\"

 def flatten_substatechart(self, path, s, states, eh):
   path2=self.append_path(path, s)
   # remove final states
   self.remove_final_states(eh.stateH)
   # merge state hierachy
   for st in eh.stateH.keys():
     states[st]=eh.stateH[st]
   # record encapsulated components
   # modify out-going connections from the submodel
   for ev in eh.trans:
     i=0
     while i<len(eh.trans[ev]):
       tr=eh.trans[ev][i]
       is_out_trans=0
       for p in eh.ports:
         if tr['N']==p and eh.ports[p]['out']:
	   is_out_trans=1
	   break
       if is_out_trans:
	 if states[ENC_CONNECT].has_key(p):
	   tr['N']=states[ENC_CONNECT][p]
	   tr['NotN']=""  # Do not change N state any more
	   i=i+1
         else:
	   del eh.trans[ev][i]
       else:
	 i=i+1
   # modify in-coming connections to the submodel
   if eh.trans.has_key(""):
     for tr in eh.trans[""]:
       is_in_trans=0
       for p in eh.ports:
         if tr['S']==p and eh.ports[p]['in']:
	   is_in_trans=1
	   break
       if is_in_trans:
         del eh.ports[p]
         for ev2 in self.trans:
	   for tr2 in self.trans[ev2]:  # O(|T|)
	     newst=tr2['N']
	     if newst==self.append_path(path2, p):
	       tr2['N']=self.append_path(path2, tr['N'])
     del eh.trans[""]
   # merge transitions
   top_ifs=self.is_ifs('')
   last_ifs=top_ifs
   turn_point=''
   pp=split(path2, '.')
   sh=self.stateH
   pa=''
   pos=0
   while pos<len(pp):
     p=pp[pos]
     if not p:
       continue
     sh=sh[p]
     pa=self.append_path(pa, p)
     if sh[INNER_TRANSITION_FIRST] and not last_ifs:
       last_ifs=1
       turn_point=pa
     elif sh[OUTER_TRANSITION_FIRST] and last_ifs:
       last_ifs=0
       turn_point=pa
     elif sh[REVERSE_TRANSITION_ORDER]:
       last_ifs=not last_ifs
       turn_point=pa
     pos=pos+1

   for ev in eh.trans.keys():
     if not ev in self.trans.keys():
       self.trans[ev]=[]
     for tr in eh.trans[ev]:
       tr['S']=self.append_path(path2, tr['S'])
       if not 'NotN' in tr.keys():
         tr['N']=self.append_path(path2, tr['N'])
       else:
	 del tr['NotN']
     l=len(self.trans[ev])
     if last_ifs:
       index=0
       while index<l and (find(self.trans[ev][index]['S'], turn_point)!=0):
         index=index+1
     else:
       index=l-1
       while index>=0 and (find(self.trans[ev][index]['S'], turn_point)!=0):
         index=index-1
       index=index+1
     for i in eh.trans[ev]:
       self.trans[ev].insert(index, i)
       index=index+1
   # merge importation information
   for im in eh.imports.keys():
     if im in self.imports.keys():
       if self.imports[im]!=eh.imports[im]:
         sys.stderr.write('ERROR: Importation conflict "'+im+'" (original value preserved).\n')
     else:
       self.imports[im]=eh.imports[im]
   # merge enter actions
   for ev in eh.enter.keys():
     p=self.append_path(path2, ev)
     if self.enter.has_key(p):
       self.enter[p]=self.enter[p]+eh.enter[ev]
     else:
       self.enter[p]=eh.enter[ev]
   # merge exit actions
   for ev in eh.exit.keys():
     p=self.append_path(path2, ev)
     if self.exit.has_key(p):
       self.exit[p]=self.exit[p]+eh.exit[ev]
     else:
       self.exit[p]=eh.exit[ev]
   # merge timed transitions
   for st in eh.ttrans.keys():
     p=self.append_path(path2, st)
     if self.ttrans.has_key(p):
       self.ttrans[p]=self.ttrans[p]+eh.ttrans[st]
     else:
       self.ttrans[p]=eh.ttrans[st]
   # merge snapshot objects
   for so in eh.snapshot_objects:
     if not so in self.snapshot_objects:
       self.snapshot_objects.append(so)
   # merge codes (interactor cannot be merged)
   self.init=self.init+eh.init	# in fact this is no use
   self.final=eh.final+self.final
   self.restore=eh.restore+self.restore
   self.beforesnp=eh.beforesnp+self.beforesnp
   self.aftersnp=eh.aftersnp+self.aftersnp
   # set state properties
   states[INNER_TRANSITION_FIRST]=eh.options[INNER_FIRST]=='1'
   states[OUTER_TRANSITION_FIRST]=eh.options[INNER_FIRST]=='0'
   states[REVERSE_TRANSITION_ORDER]=0

 def check_import(self, path, s, states, run_init=1):
   if states[IMPORT_STATE]!=None:
     for subs in states.keys():
       if not subs in StateProperties:
         sys.stderr.write('WARNING: Importation state has substate(s). This may cause unexpected error.\n')
         break
     filename=DynamicEvaluateExpression(states[IMPORT_STATE])
     params={}
     for k in states[PARAMETERS].keys():
       p=states[PARAMETERS][k]
       b=DynamicEvaluateExpression(p[1])
       params[k]=[p[0], b]
     eh=EventHandler(filename, self.callback, params, self.use_gui, 0)
     states[IMPORT_STATE]=None
     self.flatten_substatechart(path, s, states, eh)
     if eh.description!='':
       if self.use_gui:
         if DefaultUI.DefaultGUI.gui:
           DefaultUI.DefaultGUI.gui.send_output(eh.description+'\n')
       else:
         print eh.description
     if run_init:
       eh.run_initializer()
     if self.callback!=None:
       p=self.append_path(path, s)
       if self.top_level:
         self.callback(IMPORT_EVENT, None, p, p)	# oldstate and newstate are the state containing the submodel

 def add_states_to_path(self, path, paths, startpos, states, common_state):
   """ Should ONLY be called by change_state function
   """
   if startpos<len(paths):
     if states[paths[startpos]][CONCURRENT_STATE]:
       keys=states.keys()
       keys.sort()
       for s in keys:
         if not s in StateProperties:
           found=0
           for s2 in self.state:
             if self.is_or_is_substate(s2, self.append_path(path, s)):
               found=1
               break
           if found:
             continue
           if s!=paths[startpos]:
             self.check_import(path, s, states[s])
             self.add_states_to_path(self.append_path(path, s), [], 0, states[s], common_state)
           else:
             self.check_import(path, paths[startpos], states[paths[startpos]])
             self.add_states_to_path(self.append_path(path, paths[startpos]), paths, startpos+1, states[paths[startpos]], common_state)
     else:
       self.check_import(path, paths[startpos], states[paths[startpos]])
       self.add_states_to_path(self.append_path(path, paths[startpos]), paths, startpos+1, states[paths[startpos]], common_state)
   else:
     added=0
     keys=states.keys()
     keys.sort()
     for s in keys:
       if not s in StateProperties:
         if states[s][CONCURRENT_STATE] or states[s][DEFAULT_STATE]:
           added=1
           self.check_import(path, s, states[s])
           self.add_states_to_path(self.append_path(path, s), [], 0, states[s], common_state)
     if not added:
       if not path in self.state and path!=common_state:
         self.check_time_transition(path, 1, common_state)
         self.state.append(path)

 def add_state(self, path, line, default=0, concurrent=0, final=0, history=0, deephistory=0, \
               reverse=0, inner=0, outer=0, imports=None, param={}, enc_connect={}):
   """ Add an empty state (which only has the 3 special attributes) to the path
   """
   state=self.stateH
   for p in path:
     state=state[p]
   newstate={DEFAULT_STATE:default}
   newstate[CONCURRENT_STATE]=concurrent
   newstate[FINAL_STATE]=final
   newstate[HISTORY_STATE]=history
   newstate[DEEP_HISTORY_STATE]=deephistory
   newstate[REVERSE_TRANSITION_ORDER]=reverse
   newstate[INNER_TRANSITION_FIRST]=inner
   newstate[OUTER_TRANSITION_FIRST]=outer
   newstate[IMPORT_STATE]=imports
   newstate[PARAMETERS]=param
   newstate[ENC_CONNECT]=enc_connect
   state[line]=newstate

 def add_transition(self, event, desc):
   """ Add a transition to the list. The transition responses to the event,
       and its other attributes are specified in the dictionary desc
   """
   cond_changed=0
   if desc.has_key('T'):
     t=desc['T']
     del desc['T']
     if desc.has_key('S'):
       ip=self.internal_prefix
       tname='__INTERNAL_'+str(ip)+'_TIME_'+str(self.internal_num)
       self.add_transition(tname, desc)
       cond_changed=1
       if self.ttrans.has_key(desc['S']):
         self.ttrans[desc['S']].append([tname, t[0], None, t[1]])
       else:
         self.ttrans[desc['S']]=[[tname, t[0], None, t[1]]]
       self.internal_num=self.internal_num+1

   if desc.has_key('C') and not cond_changed:
     cond=desc['C']
     l='EventHandler.vtest='
     for i in range(0, len(cond)-1):
       l=l+'('+cond[i]+') and '
     l=l+'('+cond[-1]+')'
     desc['C']=l
   if event!=None:
     if self.trans.has_key(event):
       self.InsertSortedTransList(self.trans[event], desc)
     else:
       self.trans[event]=[desc]

 def InsertSortedTransList(self, trans, desc):
   """ Insert desc into the transition list ordering by the depth of its old state
       trans cannot be an empty list
       This shall be done because we stipulates that if an event enables two different
       transitions at the same time, the outer one is triggered. If they are in the
       same level, the choice is random. So designers should avoid the latter case.
   """
   ds=desc['S']
   added=0
   for i in range(0, len(trans)):
     ts=trans[i]['S']
     c1=self.is_or_is_substate(ts, ds) and ts!=ds
     c2=self.is_or_is_substate(ds, ts) and ts!=ds
     if (c1 and self.options[INNER_FIRST]=='0') or \
        (c2 and self.options[INNER_FIRST]=='1') or \
        (not c1 and not c2 and desc[TRANSITION_PRIORITY]<trans[i][TRANSITION_PRIORITY]):
       trans.insert(i, desc)
       added=1
       break
   if not added:
     trans.append(desc)

 def add_enter_exit_transition(self, estate):
   c={}
   if estate.has_key('C'):
     cond=estate['C']
     l='EventHandler.vtest='
     for i in range(0, len(cond)-1):
       l=l+'('+cond[i]+') and '
     l=l+'('+cond[-1]+')'
     c['C']=l
   if estate.has_key('S'):	# Exit transition
     state=estate['S']
     if estate.has_key('O'):
       c['O']=estate['O']
     if self.exit.has_key(state):
       self.exit[state].append(c)
     else:
       self.exit[state]=[c]
   else:
     state=estate['N']
     if estate.has_key('O'):
       c['O']=estate['O']
     if self.enter.has_key(state):
       self.enter[state].append(c)
     else:
       self.enter[state]=[c]

 def add_port(self, port_name, port_keys):
   self.ports[port_name]=port_keys

 def add_required_component(self, comp_id, comp_keys):
   self.required_components[comp_id]=comp_keys

 def load_statechart(self, filename, global_options):
   """ Loads the description of a statechart from a file
   """
   if self.modeltext:
     self.model_name=filename
     lines=split(self.modeltext, "\n")
   else:
     self.model_name=self.find_file(filename)
     if Cache.DesCache.has_key(self.model_name):
       lines=deepcopy(Cache.DesCache[self.model_name])
     else:
       if not self.model_name:
         raise FileNotFound, filename
       ext=os.path.splitext(self.model_name)[1]
       if upper(ext)=='.SNP':
         self.restore_from_file(self.model_name)
         self.restored=1
         return
       lines=[]
       for af in self.haddition:
         afname=self.find_file(af)
         if afname:
	   f=open(afname, 'r')
	   lines=lines+f.readlines()
	   f.close()
         else:
	   sys.stderr.write('WARNING: File %s cannot be included.\n' % af)
       f=open(self.model_name, 'r')
       lines=lines+f.readlines()
       f.close()
       for af in self.taddition:
         afname=self.find_file(af)
         if afname:
	   f=open(afname, 'r')
	   lines=lines+f.readlines()
	   f.close()
         else:
	   sys.stderr.write('WARNING: File %s cannot be included.\n' % af)
       
     Cache.DesCache[self.model_name]=deepcopy(lines)
     
   self.work_path=os.path.join(os.path.split(self.model_name)[0], 'svmwork')

   ismacro=0
   self.macro={}
   if self.use_gui:
     premacro=GPREDEFINED_MACROS
   else:
     premacro=TPREDEFINED_MACROS
   for p in premacro.keys():
     self.macro[p]=premacro[p]
   for i in range(len(lines)):
     line=lines[i]
     line=RemoveComment(RemoveReturn(TabToSpace(line)))
     if len(line)>0:
       lspace=len(line)-len(lstrip(line))
       if line[len(line)-1]=='\\':
         line=line[0:len(line)-1]
         k=i+1
         while k<len(lines):
           nline=lines[k]
           nline=RemoveComment(RemoveReturn(TabToSpace(nline)))
           l1=lstrip(nline)
           if (len(nline)-len(l1)<lspace):
             line=line+l1
           else:
             line=line+nline[lspace:len(nline)]
           lines[k]=''
           if line[len(line)-1]=='\\':
             line=line[0:len(line)-1]
           else:
             break
           k=k+1
     if IsDescriptor(line):
       if IsMacroDesc(line):
         ismacro=1
         line=''
       else:
         ismacro=0
     if ismacro:
       macro=ParseOption(line)
       if macro!=None:
         m=ParseParameter(macro[0])
         self.macro[m[0]]=[m[1], macro[1]]
       lines[i]=''
     else:
       lines[i]=line

   for p in self.param.keys():
     self.macro[p]=self.param[p]

   self.stateH={}
   self.trans={}
   self.history={}
   self.description=''

   self.options={}
   for dok in DEFAULT_OPTIONS.keys():
     self.options[dok]=DEFAULT_OPTIONS[dok]
   if global_options:
     for prop in INHERIT_GLOBAL_OPTIONS:
       self.options[prop]=global_options[prop]

   self.imports={}
   self.init=[]
   self.final=[]
   self.restore=[]
   self.snapshot_objects=[]
   self.beforesnp=[]
   self.aftersnp=[]
   if self.use_gui==1:
     self.interactor=[GDEFAULT_INTERACTOR]
   elif self.use_gui==0:
     self.interactor=[TDEFAULT_INTERACTOR]
   elif self.use_gui==2:
     self.interactor=[CDEFAULT_INTERACTOR]
   def_int=1
   self.ttrans={}
   self.enter={}
   self.exit={}
   parsing=None
   path=[]
   tabins={}
   lasttabin=0
   pt_in=1
   pt_out=1
   pt_name=None
   pt_buf=None
   depth=0
   estate={}
   definition=None
   curevent=None
   comp_id=None
   port_name=None
   self.required_components={}
   self.components={}
   self.required_connections=[]
   self.connections={}

   for line in lines:
     line=ReplaceMacro(line, self.macro)
     line=EvaluateExpression(line)
     if strip(line)=='':
       continue
     if IsStatechartDesc(line):
       parsing='SC'
     elif IsTransitionDesc(line):
       if (definition!=None):
	 if (curevent==None and not definition.has_key('T')):
	   curevent=""
         self.add_transition(curevent, definition)
       trstate=None
       trestate=None
       parsing='TR'
       lasttabin=0
       definition={}
       curevent=None
       for t in TransitionProperties:
         definition[t]=0
       prop=FindTransitionProperty(line)
       while prop!=None:
         line=RemoveTransitionProperty(line)
         definition[prop[0]]=prop[1]
         prop=FindTransitionProperty(line)
     elif IsPortDesc(line):
       parsing='PT'
       if port_name!=None:
	 self.add_port(port_name, port_keys)
       port_name=None
       port_keys={}
     elif IsDescriptionDesc(line):
       parsing='DC'
     elif IsOptionDesc(line):
       parsing='OP'
     elif IsImportationDesc(line):
       parsing='IM'
     elif IsInitializerDesc(line):
       parsing='IN'
       self.init.append('')
     elif IsFinalizerDesc(line):
       parsing='FI'
       self.final.append('')
     elif IsInteractorDesc(line):
       parsing='AC'
       self.has_interactor=1
       if def_int:
         def_int=0
         self.interactor=['']
       else:
         self.interactor.append('')
     elif IsEnterStateDesc(line):
       parsing='EN'
       if len(estate)>0:
         self.add_enter_exit_transition(estate)
       estate={}
     elif IsExitStateDesc(line):
       parsing='EX'
       if len(estate)>0:
         self.add_enter_exit_transition(estate)
       estate={}
     elif IsSnapshotDesc(line):
       parsing='SN'
     elif IsRestoreDesc(line):
       parsing='RE'
       self.restore.append('')
     elif IsComponentDesc(line):
       parsing='CP'
       if comp_id!=None:
	 self.add_required_component(comp_id, comp_keys)
       comp_id=None
       comp_keys=[]
     elif IsConnectionsDesc(line):
       parsing='CN'
     elif IsBeforeSnapshotDesc(line):
       parsing='BS'
       self.beforesnp.append('')
     elif IsAfterSnapshotDesc(line):
       parsing='AS'
       self.aftersnp.append('')
     else:
       if parsing=='SC':	# Parsing STATECHART section
         final=0
         concurrent=0
         default=0
         history=0
         deephistory=0
         inner=0
         outer=0
         reverse=0
         param={}
	 enc_connect={}
         imports=None
         prop=FindStateProperty(line, self.imports.keys())
         while prop!=None:
           line=RemoveStateProperty(line, self.imports.keys())
           if prop==FINAL_STATE:
             final=1
           elif prop==CONCURRENT_STATE:
             concurrent=1
           elif prop==DEFAULT_STATE:
             default=1
           elif prop==HISTORY_STATE:
             history=1
           elif prop==DEEP_HISTORY_STATE:
             history=1		# Deep history always overrides history
             deephistory=1
           elif prop==REVERSE_TRANSITION_ORDER:
             reverse=1
           elif prop==INNER_TRANSITION_FIRST:
             inner=1
           elif prop==OUTER_TRANSITION_FIRST:
             outer=1
           elif prop in self.imports.keys():
             imports=self.imports[prop]
           elif len(prop)==2:		# not string but list with 2 elements
             par=ParseParameter(prop[0])
             param[par[0]]=[par[1], prop[1]]
	   elif len(prop)==3 and prop[1]=="--":
	     enc_connect[prop[2]]=prop[0]
           prop=FindStateProperty(line, self.imports.keys())
         ti=GetTabinSize(line)
         line=strip(line)
         if ti in tabins.keys():
           pos=FindInList(path, tabins[ti])
           del path[pos:]
           for k in tabins.keys():
             if k>ti:
               del tabins[k]
         else:
           for k in tabins.keys():
             if k>ti:
               sys.stderr.write('ERROR: Bad format in the statechart description.\n')
               exit
         tabins[ti]=line
         self.add_state(path, line, default, concurrent, final, history, deephistory,
                        reverse, inner, outer, imports, param, enc_connect)
         path.append(line)
       elif parsing=='TR':	# Parsing TRANSITION section
         if len(line)<2:
           sys.stderr.write('ERROR: Bad format in the transition description.\n')
           exit
         ti=GetTabinSize(line)
         line=strip(line)
         if len(line)>=2 and line[0:2] in ['S:', 'E:', 'C:', 'N:', 'O:', 'T:']:
           # S: old State
           # E: Event
           # C: Condition (guard)
           # N: New state
           # O: Output
           # T: Time
           tii=2
           while tii<len(line):
             if line[tii]!=' ':
               break
             tii=tii+1
           lasttabin=ti+tii
	   if lasttabin==ti+2:
	     lasttabin=-1
           trstate=line[0]
           line=line[tii:]
           ti=ti+2
         if strip(line)=='':
           continue
         else:
           if trstate==None:
             sys.stderr.write('ERROR: Bad format in the transition description.\n')
             exit
           else:
             if trstate=='E':
               curevent=strip(line)
             else:
	       if lasttabin<0:
		 lasttabin=ti
               if ti>lasttabin:
                 l=GetSpace(ti-lasttabin)+line
               else:
                 l=line
               if trstate in ['O', 'C']:	# Output and Condition can have multiple lines
                 if definition.has_key(trstate):
                   definition[trstate].append(l)
                 else:
                   definition[trstate]=[l]
               elif trstate=='T':
                 repeated=1
                 prop=FindProperty(l, TimedTransitionProperties)
                 while prop!=None:
                   if prop==REPEATED_TIMED_TRANSITION:
                     repeated=1
                   elif prop==ONCE_TIMED_TRANSITION:
                     repeated=0
                   l=RemoveProperty(l, TimedTransitionProperties)
                   prop=FindProperty(l, TimedTransitionProperties)
                 definition[trstate]=[l, repeated]
               else:
                 definition[trstate]=l
       elif parsing=='PT':
	 opt=ParseOption(line)
	 if opt==None:
	   sys.stderr.write('ERROR: Bad format in the port description.\n')
	   exit
	 else:
	   if opt[0]==PORT_NAME:
	     port_name=opt[1]
	   else:
	     if opt[0]==PORT_TYPE:
	       if opt[1]==PORT_IN:
	         port_keys['in']=1
	         port_keys['out']=0
	       elif opt[1]==PORT_OUT:
	         port_keys['in']=0
	         port_keys['out']=1
	       elif opt[1]==PORT_INOUT:
	         port_keys['in']=1
	         port_keys['out']=1
	       else:
	         sys.stderr.write('ERROR: Bad format in the port description.\n')
	         exit
	     else:
	       port_keys[opt[0]]=opt[1]
       elif parsing=='EN' or parsing=='EX':
         if len(line)<2:
           sys.stderr.write('ERROR: Bad format in the enter/exit description.\n')
           exit
         ti=GetTabinSize(line)
         line=strip(line)
         if len(line)>=0 and (parsing=='EN' and line[0:2] in ['N:', 'O:', 'C:'] or \
            parsing=='EX' and line[0:2] in ['S:', 'O:', 'C:']):
           tii=2
           while tii<len(line):
             if line[tii]!=' ':
               break
             tii=tii+1
           lasttabin=ti+tii
           trestate=line[0]
           line=line[tii:]
           ti=ti+2
         if strip(line)=='':
           continue
         else:
           if trestate==None:
             sys.stderr.write('ERROR: Bad format in the transition description.\n')
             exit
           else:
             if ti>lasttabin:
               l=GetSpace(ti-lasttabin)+line
             else:
               l=line
             if trestate in ['O', 'C']:	# Output and Condition can have multiple lines
               if estate.has_key(trestate):
                 estate[trestate].append(l)
               else:
                 estate[trestate]=[l]
             else:
               estate[trestate]=l
       elif parsing=='DC':			# Parsing DESCRIOTION section
         if len(self.description)>0:
           self.description=self.description+'\n'
         self.description=self.description+line
       elif parsing=='OP':
         option=ParseOption(line)
         if option!=None:
           if option[0] in OPTION_NAMES and not option[0] in INHERIT_GLOBAL_OPTIONS and (ACCEPTABLE_VALUES[option[0]]==None) or (option[1] in ACCEPTABLE_VALUES[option[0]]):
             self.options[option[0]]=option[1]
       elif parsing=='IM':
         option=ParseOption(line)
         if option!=None:
           name='['+option[0]+']'
           if name in self.imports.keys():
             if self.imports[name]!=option[1]:
               sys.stderr.write('ERROR: Importation conflict "'+name+'".\n')
               exit
           else:
             self.imports[name]=option[1]
       elif parsing=='IN' or parsing=='FI' or parsing=='AC' or parsing=='RE' or parsing=='AS' or parsing=='BS':
         if parsing=='IN':
           st=self.init[len(self.init)-1]
         elif parsing=='FI':
           st=self.final[len(self.final)-1]
         elif parsing=='AC':
           st=self.interactor[len(self.interactor)-1]
         elif parsing=='RE':
           st=self.restore[len(self.restore)-1]
         elif parsing=='AS':
           st=self.aftersnp[len(self.aftersnp)-1]
         elif parsing=='BS':
           st=self.beforesnp[len(self.beforesnp)-1]
         if len(st)>0:
           st=st+'\n'
           if len(line)-len(lstrip(line))<init_space:
             line=lstrip(line)
           else:
             line=line[init_space:len(line)]
         else:
           init_space=len(line)-len(lstrip(line))
           line=lstrip(line)
         st=st+line
         if parsing=='IN':
           self.init[len(self.init)-1]=st
         elif parsing=='FI':
           self.final[len(self.final)-1]=st
         elif parsing=='AC':
           self.interactor[len(self.interactor)-1]=st
         elif parsing=='RE':
           self.restore[len(self.restore)-1]=st
         elif parsing=='AS':
           self.aftersnp[len(self.aftersnp)-1]=st
         elif parsing=='BS':
           self.beforesnp[len(self.beforesnp)-1]=st
       elif parsing=='SN':
         self.snapshot_objects.append(strip(line))
       elif parsing=='CP':
	 opt=ParseOption(line)
	 if opt==None:
	   sys.stderr.write('ERROR: Bad format in the component description.\n')
	   exit
	 if opt[0]==COMPONENT_ID:
	   comp_id=opt[1]
	 else:
	   comp_keys.append(opt)
       elif parsing=='CN':
	 midpos=find(line, '--')
	 left=None
	 right=None
	 if midpos>0:
	   left=strip(line[0:midpos])
	   right=strip(line[midpos+2:])
	 if not left or not right:
	   sys.stderr.write('ERROR: Bad format in the connections description.\n')
	   exit
	 self.required_connections.append([left, right])

   if (definition!=None):
     if (curevent==None and not definition.has_key('T')):
       curevent=""
     self.add_transition(curevent, definition)
   if port_name!=None:
     self.add_port(port_name, port_keys)
   if len(estate)>0:
     self.add_enter_exit_transition(estate)
   if comp_id!=None:
     self.add_required_component(comp_id, comp_keys)
   self.reorder_transitions()
   if self.options[MODEL_NAME]==None:
     mn=os.path.split(self.model_name)[1]
     pos=rfind(mn, '.')
     if pos>=1:
       self.options[MODEL_NAME]=mn[0:pos]
     else:
       self.options[MODEL_NAME]=mn

 def run_code(self, c):
   if type(c)==types.ListType:
     for cc in c:
       self.run_code(cc)
     return
   DefaultInterpreter.runsource(c+"\n", "<input>", "exec")

 def run_initializer(self):
   self.run_code(self.init)

 def run_finalizer(self):
   self.finished=1
   self.run_code(self.final)

 def run_interactor(self):
   self.run_code(self.interactor)

 def reorder_transitions_for_state(self, path, IFS):
   for ev in self.trans.keys():
     for tr in range(len(self.trans[ev])):
       t=self.trans[ev][tr]
       s=t['S']
       if self.is_or_is_substate(s, path):
         for tr2 in range(tr):
           t2=self.trans[ev][tr2]
           s2=t2['S']
           if self.is_or_is_substate(s2, path):
             l=len(split(s, '.'))
             l2=len(split(s2, '.'))
             if (IFS and l>l2) or (not IFS and l<l2):
               self.trans[ev][tr2]=t
               t=t2
               s=t2['S']
         self.trans[ev][tr]=t

 def reorder_transitions_rec(self, path, s, states, IFS):
   IFS2=IFS
   if states[INNER_TRANSITION_FIRST]:
     IFS2=1
   elif states[OUTER_TRANSITION_FIRST]:		# there may be conflict here
     IFS2=0
   elif states[REVERSE_TRANSITION_ORDER]:
     IFS2=not IFS2
   if IFS2!=IFS:
     self.reorder_transitions_for_state(path, IFS2)
   for s2 in states.keys():
     if not s2 in StateProperties:
       self.reorder_transitions_rec(self.append_path(path, s2), s2, states[s2], IFS2)

 def reorder_transitions(self):
   IFS=(self.options[INNER_FIRST]=='1')		# modify later
   for s in self.stateH.keys():
     if not s in StateProperties:
       self.reorder_transitions_rec(s, s, self.stateH[s], IFS)

 def outputFnc(self, outp):
   """ Runs the output function(s) in the list outp
   """
   for o in outp:
     if o!='':
       DefaultInterpreter.runsource(DynamicEvaluateExpression(o))

 def event(self, event, params=[], internal=1, lock=None):
   if self.callback!=None:
     self.event_lock.acquire()
     res=self.callback(str(event), -1, '', '')
     self.event_lock.release()
     if not res:
       return
   if not isinstance(event, EventObject):
     event=EventObject(event)
   event.params=params
   self.event_lock.acquire()
   is_handler_stopped=(len(self.event_list)==0)
   self.event_list.append([event, internal, lock])
   self.event_lock.release()
   if is_handler_stopped and self.Started:
     clock=Clock(self)
     clock.start(0, self.handle_event, [], 1, 1)

 def handle_seq_snapshot(self):
   self.take_seq_snapshot()
   self.snapshot_retrieve_lock.acquire()
   if self.snapshot_retrieve!=None:
     self.get_seq_snapshot(self.snapshot_retrieve)
     self.snapshot_retrieve=None
   self.snapshot_retrieve_lock.release()

 def take_seq_snapshot(self):
   self.seq_snapshots_lock.acquire()
   self.snapshot_requests_lock.acquire()
   ss=None
   for req in self.snapshot_requests:
     if not ss:
       ss=self.snap_to_string()
     self.seq_snapshots[req]=ss
   self.snapshot_requests=[]
   self.snapshot_requests_lock.release()
   if self.options[TIMEWARP]=='1':
     if not ss:
       ss=self.snap_to_string()
     t=eval(self.options[TIME_VARIABLE], sys.modules['__main__'].__dict__)
     self.seq_snapshots[t]=ss
   self.seq_snapshots_lock.release()

 def get_seq_snapshot(self, t_label):
   self.handle_event_lock.acquire()
   self.event_lock.acquire()
   self.seq_snapshots_lock.acquire()
   ss=self.seq_snapshots[t_label]
   self.restore_from_string(ss)
   self.seq_snapshots_lock.release()
   self.event_lock.release()
   self.handle_event_lock.release()
   self.local_restored=1
   self.start()

 def finalize_handle_event(self):
   self.event_lock.release()
   if self.options[TIMEWARP]=='1':
     self.synchronous_call(EventObject(self.options[TIMEWARP_PORT]+".notifyidle"), [], self.options[TIMEWARP_PORT]+".goahead")
   self.handle_event_lock.release()
   self.handle_seq_snapshot()
   self.empty_event_signal_lock.acquire()
   if self.empty_event_signal:
     self.empty_event_signal.release()
     self.empty_event_signal=None
   self.empty_event_signal_lock.release()
   
 def handle_event(self):
   """ Event handler
       When event E occurs, this handler is called.
       It first runs the callback function, which can be defined for debug purpose.
       After that, it decides whether a transition can be made.
       The decision is based on the current state and the definition of the transition.
       If a transition should be performed, it first runs the callback function, then changes
       the current state, carries out the output commands, and runs the callback function
       once more before return.
   """
   self.handle_event_lock.acquire()
   if self.options[TIMEWARP]=='1':
     ct=self.synchronous_call(EventObject(self.options[TIMEWARP_PORT]+".get"), [], self.options[TIMEWARP_PORT]+".time")[0]
     DefaultInterpreter.runsource(self.options[TIME_VARIABLE]+"="+str(ct))
   while 1:
     self.event_lock.acquire()
     if len(self.event_list)==0:
       self.finalize_handle_event()
       return
     [event, internal, lock]=self.event_list[0]
     self.event_lock.release()
     
     E=str(event)
     self.event_object=event

     if internal:
       dpos=find(E, '.')
       if dpos>=0:
         pname=E[:dpos]
	 if pname:
           if self.ports.has_key(pname):
             self.external_event(event, event.params)
           self.event_lock.acquire()
           del self.event_list[0]
           if len(self.event_list)==0:
	     self.finalize_handle_event()
             return
           self.event_lock.release()
           continue
	 else:  # fake an external event with event name starting with "." (i.e., no in-port name) e.g. ".in-port-name.in-event-name"
	   internal=0
	   event.event=event.event[1:]
	   E=str(event)
     else:
       chk=self.check_event_time(event)
       if chk==0:  # do not handle this event
         self.event_lock.acquire()
         del self.event_list[0]
         if len(self.event_list)==0:
	   self.finalize_handle_event()
           return
         self.event_lock.release()
         continue
       elif chk==-1:  # rollback needed
         self.event_lock.acquire()
         del self.event_list[0]
	 self.finalize_handle_event()
         return	 

     if self.finished:
       self.event_lock.acquire()
       del self.event_list[0]
       if len(self.event_list)==0:
	 self.finalize_handle_event()
         return
       self.event_lock.release()
       continue
     handled=1
     handled_states=[]
     oldstate=copy(self.state)
     while handled:
       handled=0
       if self.trans.has_key(E):
         desc=self.trans[E]
         di=0
         while di<len(desc):
           d=desc[di]
           di=di+1
           if not (d.has_key('S') and d.has_key('N')):	# If it is not a valid transition
             continue
           cannot_handle=0
           for ss in handled_states:
             if (self.is_or_is_substate(d['S'], ss) or \
                 self.is_or_is_substate(ss, d['S'])):
               cannot_handle=1
               break
           if cannot_handle:
             continue
           for s in oldstate:
             if self.is_or_is_substate(s, d['S']):
               if d.has_key('C'):		# If there is a condition defined
                 DefaultInterpreter.runsource(d['C'])
                 if not vtest:
                   continue
               # The transition can be carried out here
               if self.callback!=None:
                 self.callback(E, 0, d['S'], d['N'])

	       is_out_trans=0
	       for p in self.ports.keys():
		 if d['N']==p and self.ports[p]['out']:  # Transition going to an out-port
		   is_out_trans=1
		   
	       if d.has_key('O'):
		 output_actions=d['O']
	       else:
		 output_actions=None

	       if not is_out_trans:  # Do not change state if it is out-transition
		 # Recent change -- output actions are executed AFTER exit actions but before state change and enter actions
                 self.change_state(d['S'], d['N'], d[HISTORY_STATE], output_actions)
	       else:
		 self.outputFnc(output_actions)
               handled=1
               if self.callback!=None:
                 self.callback(E, 1, d['S'], d['N'])
               break
           if handled:
             di=0
             handled_states.append(d['S'])
             break
       if handled and self.is_final_state():
         self.run_finalizer()
         break
     self.event_lock.acquire()
     del self.event_list[0]
     if lock:
       lock.release()
     if len(self.event_list)==0:
       self.finalize_handle_event()
       return
     self.event_lock.release()

 def ShowStateH(self):
   print '{'
   self.ShowStateH_Rec(self.stateH, 3)
   print '}'

 def ShowStateH_Rec(self, state, space):
   """ Shows the internal state hierachy in a more readable way (for debug purpose)
   """
   i=0
   keys=state.keys()
   keys.sort()
   l=len(keys)
   for k in keys:
     i=i+1
     coma=''
     if i<l:
       coma=','
     if not k in StateProperties:
       brank=','
       lp=len(StateProperties)
       if len(state[k].keys())==lp:
         brank=' }'+coma
       print GetSpace(space)+'\''+k+'\' : {',
       for j in range(lp):
         if StateProperties[j]==IMPORT_STATE:
           prop='\''+str(state[k][StateProperties[j]])+'\''
         else:
           prop=str(state[k][StateProperties[j]])
         if j<lp-1:
           print '\''+StateProperties[j]+'\' : '+prop+',',
         else:
           print '\''+StateProperties[j]+'\' : '+prop+brank
       if len(state[k].keys())>lp:
         self.ShowStateH_Rec(state[k], space+3)
         print GetSpace(space)+' }'+coma

 def ShowTransitions(self):
   """ Shows the internal transition table in a more readable way (for debug purpose)
   """
   i=0
   l=len(self.trans)
   print '{'
   for t in self.trans.keys():
     i=i+1
     print '  \''+t+'\' : ['
     self.ShowAnEvent(self.trans[t])
     if i<l:
       print '  ],'
     else:
       print '  ]'
   print '}'

 def ShowAnEvent(self, trans):
   """ Should ONLY be called by ShowTransitions function
   """
   i=0
   l=len(trans)
   for t in trans:
     i=i+1
     s='    { '
     x=0
     y=len(t.keys())
     for k in TransitionProperties:
       x=x+1
       s=s+'\''+k+'\' : '+str(t[k])
       if x<y:
         s=s+',\n      '
       else:
         s=s+' }'
     y=y-x
     x=0
     for k in t.keys():
       if not k in TransitionProperties:
         x=x+1
         s=s+'\''+k+'\' : '+self.ShowKey(k, t[k])
         if x<y:
           s=s+',\n      '
         else:
           s=s+' }'
     if i<l:
       s=s+','
     print s

 def ShowKey(self, k, desc):
   """ Should ONLY be called by ShowAnEvent function
   """
   qchar='\''
   if k in ['S', 'N', 'C']:
     if find(desc, qchar)>=0:
       qchar='"'
     return qchar+desc+qchar
   else:
     s='[ '
     i=0
     j=len(desc)
     for d in desc:
       if find(d, qchar)>=0:
         qchar='"'
       i=i+1
       s=s+qchar+d+qchar
       if i<j:
         s=s+',\n              '
       qchar='\''
     s=s+' ]'
     return s

 def find_file(self, name):
   paths=sys.path
   for p in paths:
     n=os.path.join(p, name)
     if os.path.exists(n):
       return n
   return None

 def get_enabled_events(self):
   ee=[]
   keys=self.trans.keys()
   keys.sort()
   for ev in keys:
     found=0
     for t in self.trans[ev]:
       s=t['S']
       for c in self.state:
         if self.is_or_is_substate(c, s):
           ee.append(ev)
           found=1
           break;
       if found:
         break;
   ee.sort()
   return ee

 def start(self, signal=None):
   if not self.local_restored and self.ports:  # initiate dns only if the model has ports
     try:
       exec("from SVMPVM import *", globals())
     except:
       sys.stderr.write("WARNING: PyPVM is not installed.\n")
     #from SVMCORBA import *
     init_dns(self)
   if self.options[TIMEWARP]=='1':
     set_call_back(self.options[TIMEWARP_PORT]+".rollback", self.emergency_callback, [])
     DefaultInterpreter.runsource(self.options[TIME_VARIABLE]+"=0")
     t=self.synchronous_call(EventObject(self.options[TIMEWARP_PORT]+".get"), [], self.options[TIMEWARP_PORT]+".time")[0]
     DefaultInterpreter.runsource(self.options[TIME_VARIABLE]+"=%f"%t)
   if self.restored or self.local_restored:
     self.restored=0
     self.local_restored=0
     for k in self.global_snapshot_objects.keys():
       value=self.global_snapshot_objects[k]
       try:
         obj=eval(k, sys.modules['__main__'].__dict__)
       except:
         obj=k
       restore_snapshot(obj, value, k)
     del self.global_snapshot_objects
     self.run_code(self.restore)
     idx=0
     self.ttrans=self.newttrans
     for ct in self.clock_threads:
       clock=Clock(self)
       for tt in self.ttrans.keys():
         tts=self.ttrans[tt]
         for ttss in tts:
           if ttss[2]==idx:
             ttss[2]=clock
       idx=idx+1
       clock.start_ss(ct, self.event)
     del self.newttrans
   else:
     entered=[]
     for s in self.state:
       path=''
       comm_max=0
       for p in entered:
         comm=self.common_state(p, s)
         if len(comm)>comm_max:
           comm_max=len(comm)
           path=comm
       entered.append(s)
       self.enter_exit_transition(path, s, 0, 1)
     for s in self.state:
       self.check_time_transition(s, 0)
     if signal:
       self.event_lock.acquire()
       self.empty_event_signal_lock.acquire()
       if len(self.event_list)>0:
	 self.empty_event_signal=signal
       else:
	 signal.release()
       self.empty_event_signal_lock.release()
       self.event_lock.release()
   if not self.finished and self.is_final_state():
     self.run_finalizer()

   self.event_lock.acquire()
   self.Started=1
   if self.event_list:
     clock=Clock(self)
     clock.start(0, self.handle_event, [], 1, 1)
   self.event_lock.release()

 def has_substate(self, state):
   for s in state.keys():
     if not s in StateProperties:
       return 1
   return 0

 def get_clock_threads(self):
   cur_t=time.time()
   self.clock_threads=[]
   for c in self.clocks:
     if not c.func==self.event:
       continue
     names=dir(c)
     for u in C_UNSNAPPABLE:
       pos=FindInList(names, u)
       del names[pos]
     if c.first_interval:
       fi=c.first_interval-(cur_t-c.schedule_time)
     else:
       fi=c.inter-(cur_t-c.schedule_time)
     if fi<0:
       fi=0
     ss=take_snapshot(c, names, None, 'first_interval = %s' % str(fi))
     self.clock_threads.append(ss)

   self.newttrans={}
   for tt in self.ttrans.keys():
     tts=self.ttrans[tt]
     lst=[]
     for ttst in tts:
       if ttst[2]==None:
         lst.append(ttst)
       else:
         idx=0
         for c in self.clocks:
           if ttst[2]==c:
             break;
           idx=idx+1
         newt=ttst[0:2]+[idx]+ttst[3:len(ttst)]
         lst.append(newt)
     self.newttrans[tt]=lst

 def snap_to_string(self):
   self.run_code(self.beforesnp)
   self.handle_event_lock.acquire()
   clock_lock.acquire()
   start_lock.acquire()
   global_snapshot_objects={}
   for so in self.snapshot_objects:
     right=eval('take_snapshot('+so+')', sys.modules['__main__'].__dict__)
     global_snapshot_objects[so]=right
   self.get_clock_threads()
   names=dir(self)
   for u in E_UNSNAPPABLE:
     pos=FindInList(names, u)
     del names[pos]
   ss=take_snapshot(self, names, None, 'global_snapshot_objects = %s\n' % str(global_snapshot_objects)\
                                      +'clock_threads = %s' % str(self.clock_threads))
   del self.clock_threads
   del self.newttrans
   start_lock.release()
   clock_lock.release()
   self.handle_event_lock.release()
   return ss

 def snap_to_file_thread(self, filename=None):
   ss=self.snap_to_string()
   if not filename:
     filename=os.path.splitext(self.model_name)[0]+'.snp'
   f=open(filename, 'w')
   f.write(ss)
   f.close()
   self.run_code(self.aftersnp)
 
 def snap_to_file(self, filename=None):
   clock=Clock(self)
   clock.start(0, self.snap_to_file_thread, (filename), 1)

 def restore_from_string(self, ss):
   self.stop_all_clocks()
   restore_snapshot(self, ss)   
   
 def restore_from_file(self, filename):
   f=open(filename, 'r')
   ss=f.read()
   f.close()
   self.restore_from_string(ss)

 def request_snapshot(self, t_label):
   self.snapshot_requests_lock.acquire()
   self.snapshot_requests.append(t_label)
   self.snapshot_requests_lock.release()

 def retrieve_snapshot(self, t_label):
   self.snapshot_retrieve_lock.acquire()
   self.snapshot_retrieve=t_label
   self.snapshot_retrieve_lock.release()

 def stop_all_clocks(self):
   for c in self.clocks:
     c.stop()
 
 def is_in_state(self, state, check_substate=0):
   if not check_substate:
     return state in self.state
   else:
     for s in self.state:
       if self.is_or_is_substate(s, state):
         return 1
     return 0

 def shutdown(self):
   if not self.is_final_state():
     self.run_finalizer()
   self.finished=1
   try:
     end_dns()
   except:
     pass

 def get_event_params(self):
   if self.event_object and 'params' in dir(self.event_object):
     return self.event_object.params
   else:
     return None

 def get_event_sender(self):
   if self.event_object and 'sender' in dir(self.event_object):
     return self.event_object.sender
   else:
     return None

 def external_event(self, event, params=[], receivers=None):
   event.params=params
   influencees=send_external_event(self, event, receivers)
   if self.options[TIMEWARP]=='1':
     succ=0
     if self.options[TIME_VARIABLE]:
       try:
         t=eval(self.options[TIME_VARIABLE], sys.modules['__main__'].__dict__)
         succ=1
       except:
         pass
     if not succ:
       sys.stderr.write("WARNING: Cannot evaluate current time with %s global option; cannot record influencees.\n" % TIME_VARIABLE)
     else:
       if not self.influencees.has_key(t):
         self.influencees[t]=[]
       self.influencees[t]=self.influencees[t]+influencees

 def synchronous_callback(self, event, result, lock):
   result.append(event.params)
   lock.release()

 def emergency_callback(self, event):
   set_call_back(self.options[TIMEWARP_PORT]+".rollback", self.emergency_callback, [])
   ThreadUtil.StartThread(self.emergency_thread, (event,))

 def emergency_thread(self, event):
   if self.options[TIMEWARP]=='1':
     if event.event==self.options[TIMEWARP_PORT]+".rollback":
       self.handle_event_lock.acquire()
       t_rollback=event.params[0]
       keys=self.seq_snapshots.keys()
       keys.sort()
       lastsnapshot=None
       for k in keys:
         if k<=t_rollback:
           lastsnapshot=k
         else:
           break
       if lastsnapshot==None:
         sys.stderr.write("WARNING: Cannot rollback to time %f.\n" % t_rollback)
	 self.handle_event_lock.release()
       else:
         snp=self.seq_snapshots[lastsnapshot]
	 self.restore_from_string(snp)
	 DefaultInterpreter.runsource(self.options[TIME_VARIABLE]+"=%f"%t_rollback)
	 set_call_back(self.options[TIMEWARP_PORT]+".goahead", self.rollback_goahead, [])
	 self.external_event(EventObject(self.options[TIMEWARP_PORT]+".rollbacked"), [t_rollback])

 def rollback_goahead(self, event):
   ThreadUtil.StartThread(self.rollback_thread, (event,))

 def rollback_thread(self, event):
   rs=event.params[1]
   self.future_events={}
   keys=self.event_log.keys()
   keys.sort()
   for t in keys:
     if t<=event.params[0]:
       continue
     l=self.event_log[t]
     for r in rs:
       i=0
       while i<len(l):  # O(n^3) again!
         if r==l[i].sender:
	   del l[i]
	 else:
	   i=i+1
     if len(l)>0:
       self.future_events[t]=l
       self.event(EventObject(self.options[TIMEWARP_PORT]+".schedule", [t, eval(self.options[TIME_VARIABLE], sys.modules['__main__'].__dict__)]))
   if self.skewed_event:
     self.event_list=[[self.skewed_event, 0, None]]
     self.skewed_event=None
     print "Rollbacked to:", event.params[0]
     clock=Clock(self)
     clock.start(0, self.handle_event, [], 1, 1)
     self.handle_event_lock.release()
   else:
     self.event_list=[]
     self.handle_event_lock.release()
     self.synchronous_call(EventObject(self.options[TIMEWARP_PORT]+".notifyidle"), [], self.options[TIMEWARP_PORT]+".goahead")

 def synchronous_call(self, event, params, in_name):
   event.params=params
   result=[]
   lock=ThreadUtil.AllocateLock()
   lock.acquire()
   set_call_back(in_name, self.synchronous_callback, [result, lock])
   self.external_event(event)
   lock.acquire()
   lock.release()
   return result[0]

 def remove_old_records(self, dlist, t):
   keys=dlist.keys()
   keys.sort()
   i=0
   while i<len(keys):
     if keys[i]<=t:
       del dlist[keys[i]]
     i=i+1

 def check_event_time(self, event):
   """ return 1: continue handling the event
              0: omit the event and handle other events
	     -1: emergency stop
   """
   if self.options[TIMEWARP]=='1':
     if startswith(event.event, self.options[TIMEWARP_PORT]+'.'):
       if event.event==self.options[TIMEWARP_PORT]+".notify":  # "timewarp.notify" event to advance time
	 mt=event.params[0]
	 if self.future_events.has_key(mt):
	   DefaultInterpreter.runsource(self.options[TIME_VARIABLE]+"="+str(mt))
	   for e in self.future_events[mt]:
	     e.event='.'+e.event
	     self.event(e)
	   del self.future_events[mt]
	 return 1
       elif event.event==self.options[TIMEWARP_PORT]+".globaltime":
	 gt=event.params[0]
	 print "globaltime:", gt
	 keys=self.seq_snapshots.keys()
	 keys.sort()
	 # throw away useless snapshots
	 i=0
	 while i<len(keys)-1:
	   if keys[i]<gt and keys[i+1]<gt:
	     del self.seq_snapshots[keys[i]]
	   i=i+1
	 # throw away useless influencee records
	 self.remove_old_records(self.influencees, gt)
	 # throw away useless event logs
	 self.remove_old_records(self.event_log, gt)
	 return 0
     else:
       mt=eval(self.options[MESSAGE_TIME], sys.modules['__main__'].__dict__)
       ct=eval(self.options[TIME_VARIABLE], sys.modules['__main__'].__dict__)
       if mt<ct:  # message sent in the part
         print 'Time skew: mt=%f, ct=%f'%(mt, ct)
	 self.skewed_event=event
	 inf=[]
	 for k in self.influencees.keys():
	   if mt<k:
	     for i in self.influencees[k]:
	       if not i in inf:  # O(n^3)! god!
		 inf.append(i)
	 self.external_event(EventObject(self.options[TIMEWARP_PORT]+".timeskew"), [mt, inf+[self.GUID()]])
	 return -1
       else:
	 if not self.event_log.has_key(mt):
	   self.event_log[mt]=[]
	   self.event_log[mt].append(event)
         if mt>ct:  # the message is really sent in the future by a component other than the clock
	   if not self.future_events.has_key(mt):
	     self.future_events[mt]=[]
	   self.future_events[mt].append(event)
	   self.external_event(EventObject(self.options[TIMEWARP_PORT]+".schedule"), [mt, ct])
	   return 0
   return 1

 def GUID(self):
   return get_GUID()

 def set_event_signal(self, signal):
   self.empty_event_signal_lock.acquire()
   self.empty_event_signal=signal
   self.empty_event_signal_lock.release()

 def synchronous_event(self, event, internal=1, lock=None):
   signal=ThreadUtil.AllocateLock()
   signal.acquire()
   self.set_event_signal(signal)
   self.event(event, internal, lock)
   signal.acquire()
   signal.release()

 def get_current_state(self):
   return str(self.state)
