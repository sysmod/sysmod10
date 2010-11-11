# Python source code generated by SCC (StateChart Compiler) 0.1, written by Thomas Feng
#   Source: behaviour_generated_no_link_with_gui.des
#   Date:   March 19, 2004
#   Time:   18:22:37


# Header Section -- definition and module importation used by the following parts
import sys
import copy
import time
import string


class State:

  def __init__(self):

    self.StateID=-1
    self.Next=None


class History:

  def __init__(self):

    self.States=None
    self.Times=None
    self.Submodel=None


class EventList:

  def __init__(self):

    self.Event=None
    self.Next=None

  def Append(self, e):

    if isinstance(e, str):
      el=EventList()
      el.Event=e
      cur=this
      while cur.Next!=None and cur.Event!=e:
        cur=cur.Next;
      if cur.Event!=e:
        cur.Next=el

    elif isinstance(e, EventList):
      el=e
      while el!=None:
        self.Append(el.Event)
        el=el.Next


class StringList:

  def __init__(self, str=""):

    self.str=str
    self.Next=None


class IntList:

  def __init__(self, int=0):
    self.int=int
    self.Next=None


class Hierarchy:

  def __init__(self):

    self.StateName=None
    self.PathName=None
    self.StateNum=-1
    self.Level=-1
    self.Next=None


# Scheduler for timed transitions (used only when --pyext is set)
import thread
import time
class Scheduler:

  def __init__(self, model, event, interval, repeat):

    self.Model=model
    self.Event=event
    self.Interval=interval
    self.Repeat=repeat
    self.Lock=thread.allocate_lock()
    self.Stopped=0
    self.Next=None

  def start(self):

    thread.start_new_thread(self.run, ())

  def stop(self):

    self.Lock.acquire()
    self.Stopped=1
    self.Lock.release()

  def clear(self):

    self.stop()
    if self.Next:
      self.Next.clear()

  def run(self):

    stopped=0
    while not stopped:
      time.sleep(self.Interval)
      self.Lock.acquire()
      stopped=self.Stopped
      self.Lock.release()
      if not stopped:
        self.Model.event(self.Event, [], 0)
        stopped=not self.Repeat


class StateMachine:

  def eventStr2Int(self, event):

    return -1

  def handleEvent(self, se, params=[], lock=None, call_submodels=1):

    return 0

  def getCurrentStateList(self):

    return None

  def getCurrentState(self):

    return "[]"

  def getEnabledEvents(self):

    return None

  def initModel(self, run_initializer=1):

    pass

  def isInState(self, s):

    return 0

  def getParentState(self, state):

    return -1

  def isHistoryState(self, state):

    return 0

  def isLeafState(self, state):

    return 0

  def getHierarchy(self, start_level=0, state_prefix=None):

    return None

  def topLevelHistory(self):

    pass

  def runActionCode(self, code_num):

    pass

  def testCondition(self, cond_num):

    pass

  def runEnterActions(self, state):

    pass

  def runInitializer(self):

    pass

  def runFinalizer(self):

    pass

  def runInteractor(self):

    pass

  def state(self):
    pass

  def event(self, e, params=[], call_submodels=1):

    pass


def startswith(s, ss):
  return ss==None or (s!=None and len(s)>=len(ss) and s[0:len(ss)]==ss)


# used only when --pyext is set
from code import InteractiveInterpreter


# Main Class -- the top level model that is executed from the command line
class behaviour_generated_no_link_with_gui(StateMachine):

  # Constants for this model
  StateNum=4
  EventNames=["__INTERNAL_0_TIME_0",
              "press" 
             ]
  StateNames=["Disabled",
              "Enabled",
              "Enabled.Green",
              "Enabled.Red" 
             ]
  ParentTable=[-1,  # Disabled -- parent (None)
               -1,  # Enabled -- parent (None)
               1,  # Enabled.Green -- parent Enabled
               1   # Enabled.Red -- parent Enabled
              ]
  HistoryStateTable=[0,
                     0,
                     0,
                     0 
                    ]
  LeafStateTable=["Disabled",
                  None,
                  "Enabled.Green",
                  "Enabled.Red" 
                 ]
  OrthogonalInBetween=[[0, 0, 0, 0],
                       [0, 0, 0, 0],
                       [0, 0, 0, 0],
                       [0, 0, 0, 0],
                       [0, 0, 0, 0] 
                      ]
  Hierarchy=[[0, 0, 0, 0],  # substates of state Disabled
             [0, 0, 1, 1],  # substates of state Enabled
             [0, 0, 0, 0],  # substates of state Enabled.Green
             [0, 0, 0, 0]   # substates of state Enabled.Red
            ]
  CommonStateTable=[[0, -1, -1, -1],
                    [-1, 1, 1, 1],
                    [-1, 1, 2, 1],
                    [-1, 1, 1, 3] 
                   ]
  Description=None

  # used only when --pyext is set
  Lock=thread.allocate_lock()
  CurrentModel=None

  def __init__(self, Interpreter=None):

    # Variables
    self.state=None
    self.Submodels=[]
    for i in range(behaviour_generated_no_link_with_gui.StateNum):
      self.Submodels.append(None)
    self.history=[]
    for i in range(behaviour_generated_no_link_with_gui.StateNum):
      self.history.append(None)

    self.TimedTransitions=[] # used only when --pyext is set
    for i in range(behaviour_generated_no_link_with_gui.StateNum):
      self.TimedTransitions.append(None)

    self.clearEnteredStates()

    # Constructor
    for i in range(behaviour_generated_no_link_with_gui.StateNum):
      self.history[i]=History()
      self.history[i].States=[]
      self.history[i].Times=[]
      for j in range(behaviour_generated_no_link_with_gui.StateNum):
        self.history[i].States.append(-1)
        self.history[i].Times.append(-1)

    # Interpreter of action code
    if Interpreter:
      self.DefaultInterpreter=Interpreter
    else:
      self.DefaultInterpreter=InteractiveInterpreter()
    self.HasInteractor=0
    self.setupInterpreter()

    self.Started=0

    self.EventsLock=thread.allocate_lock()
    self.PendingEvents=None
    self.PendingEventsTail=None
    self.HandleEventRunning=0

    self.description=behaviour_generated_no_link_with_gui.Description

  # Methods
  def isParent(self, sp, sc):

    return sc>=0 and (sp<0 or behaviour_generated_no_link_with_gui.Hierarchy[sp][sc])

  def isInState(self, s):

    if isinstance(s, int):
      st=self.state
      while st!=None:
        if st.StateID==s or self.isParent(s, st.StateID):
          return 1
        else:
          st=st.Next
      return 0

    elif isinstance(s, str):
      for i in range(behaviour_generated_no_link_with_gui.StateNum):
        if s==behaviour_generated_no_link_with_gui.StateNames[i]:
          return self.isInState(i)
      for i in range(behaviour_generated_no_link_with_gui.StateNum):
        if self.Submodels[i]!=None and startsWith(s, behaviour_generated_no_link_with_gui.StateNames[i]+"."):
          SubmodelState=s[len(behaviour_generated_no_link_with_gui.StateNames[i])+1:]
          return self.isInState(i) and self.Submodels[i].isInState(SubmodelState)
    return 0

  def main(self, argv):

    model=behaviour_generated_no_link_with_gui()
    cmd=""
    model.initModel()
    if model.HasInteractor:
      model.runInteractor()
    else:
      if behaviour_generated_no_link_with_gui.Description:
        sys.__stdout__.write(behaviour_generated_no_link_with_gui.Description+"\n")
      lock=thread.allocate_lock()
      while cmd!="exit":
        sys.__stdout__.write(model.getCurrentState()+" > ")
        cmd=string.strip(sys.__stdin__.readline())
        if cmd=="exit":
          break
        lock.acquire()
        model.event(cmd, [], lock)
        lock.acquire()
        lock.release()
    model.runFinalizer()

  def initModel(self, run_initializer=1, run_enter_actions=1):

    self.clearEnteredStates()
    self.Started=1
    self.addInState(3) # init state "Enabled.Red"
    self.recordEnteredState(1)
    self.recordEnteredState(3)
    self.Started=1
    if run_initializer:
      self.runInitializer()
    if not self.HasInteractor:
      self.start(run_enter_actions)

  def handleEvent(self, se, params=[], lock=None, call_submodels=1):

    if not self.Started:
      if lock:
        lock.release()
      return 0
    e=self.eventStr2Int(se)
    self.EventsLock.acquire()
    self.HandleEventRunning=1
    self.EventsLock.release()
    self.params=params
    if e==0: # event "__INTERNAL_0_TIME_0"
      if self.isInState(1) and self.testCondition(0):
        self.runExitActionsForStates(-1)
	self.clearEnteredStates()
        self.changeState(1, 0)
        self.runEnterActionsForStates(self.StatesEntered, 1)
        if lock:
          lock.release()
        self.checkPendingEvents()
        return 1
    elif e==1: # event "press"
      if self.isInState(3) and self.testCondition(1):
        self.runExitActionsForStates(1)
	self.clearEnteredStates()
        self.changeState(3, 2)
        self.runEnterActionsForStates(self.StatesEntered, 1)
        if lock:
          lock.release()
        self.checkPendingEvents()
        return 1
      if self.isInState(2) and self.testCondition(2):
        self.runExitActionsForStates(1)
	self.clearEnteredStates()
        self.changeState(2, 3)
        self.runEnterActionsForStates(self.StatesEntered, 1)
        if lock:
          lock.release()
        self.checkPendingEvents()
        return 1
    if lock:
      lock.release()
    self.checkPendingEvents()
    return 0

  def forceIntoState(self, s):

    changed=0
    s2=self.state
    while s2!=None:
      HasCommonParent=0
      for i in range(behaviour_generated_no_link_with_gui.StateNum):
        if self.isParent(i, s2.StateID) and self.isParent(i, s):
          HasCommonParent=1
          if not self.hasOrthogonalStateInBetween(i, s2.StateID):
            self.changeState(s2.StateID, s)
            changed=1
      if not HasCommonParent:
        self.changeState(s2.StateID, s)
        changed=1
      s2=s2.Next
    if not changed:
      self.addInState(s)

  def changeState(self, s1, s2, check_history=0, top_level=0):

    # t1=common(s1, s2)
    t1=behaviour_generated_no_link_with_gui.CommonStateTable[s1][s2]
    self.recordHistory(t1)
    if t1>=0:
      self.removeOutStates(t1)
    else:
      self.state=None
    # t2=history(s2)
    t2=behaviour_generated_no_link_with_gui.HistoryStateTable[s2]
    if t2==0: # no history
      self.generateStates(t1, s2)
    elif t2==1: # normal history
      if not check_history:
        self.generateStates(t1, s2)
      elif self.hasHistoryRecorded(s2):
        self.generateStates(t1, self.history[s2].States[s2])
      else:
        self.generateStates(t1, s2, 1)
    elif t2==2: # deep history
      if check_history and self.hasHistoryRecorded(s2):
        for i in range(behaviour_generated_no_link_with_gui.StateNum):
          hs=self.history[s2].States[i]
          if hs>=0 and self.isLeafState(hs):
            # used only when --pyext is set
            self.recordEnteredState(hs, 1, 1, t1)
            self.addInState(hs)
      else:
        self.generateStates(t1, s2)

  def recordEnteredState(self, s, superstates=0, submodel=0, commonstate=-1):

    # test is s is already recorded
    se=self.StatesEntered
    found=0
    while se!=None:
      if se.int==s:
        found=1
        break
      se=se.Next

    if not found:
      if superstates:
        parent=self.getParentState(s)
        if parent>=0 and parent!=commonstate:
          self.recordEnteredState(parent, 1)
      st=IntList()
      st.Next=self.StatesEntered
      st.int=s
      self.StatesEntered=st
      if submodel and self.Submodels[s]:
        mdl=self.Submodels[s]
        st=mdl.state
        while st!=None:
          mdl.recordEnteredState(st.StateID, 1, 1)
          st=st.Next

  def addInState(self, s):
    if not self.isInState(s):
      st=State()
      st.StateID=s
      st.Next=self.state
      self.state=st
      return 1
    else:
      return 0

  def generateStates(self, common, dest, history_type=0):

    if common==-1:
      if dest==0:
        if history_type!=2 or self.check_history(-1):
          if history_type!=2 or self.check_history(0):
            self.recordEnteredState(0)
            self.addInState(0)  # move into leaf state "Disabled"
      elif dest==1:
        if history_type!=2 or self.check_history(-1):
          if history_type!=2 or self.check_history(1):
            self.recordEnteredState(1)
            if history_type!=2 or self.check_history(3):
              self.recordEnteredState(3)
              self.addInState(3)  # move into leaf state "Enabled.Red"
      elif dest==2:
        if history_type!=2 or self.check_history(-1):
          if history_type!=2 or self.check_history(1):
            self.recordEnteredState(1)
            if history_type!=2 or self.check_history(2):
              self.recordEnteredState(2)
              self.addInState(2)  # move into leaf state "Enabled.Green"
      elif dest==3:
        if history_type!=2 or self.check_history(-1):
          if history_type!=2 or self.check_history(1):
            self.recordEnteredState(1)
            if history_type!=2 or self.check_history(3):
              self.recordEnteredState(3)
              self.addInState(3)  # move into leaf state "Enabled.Red"
    elif common==0:
      if dest==0:
        if history_type!=2 or self.check_history(0):
          self.addInState(0)  # move into leaf state "Disabled"
    elif common==1:
      if dest==1:
        if history_type!=2 or self.check_history(1):
          if history_type!=2 or self.check_history(3):
            self.recordEnteredState(3)
            self.addInState(3)  # move into leaf state "Enabled.Red"
      elif dest==2:
        if history_type!=2 or self.check_history(1):
          if history_type!=2 or self.check_history(2):
            self.recordEnteredState(2)
            self.addInState(2)  # move into leaf state "Enabled.Green"
      elif dest==3:
        if history_type!=2 or self.check_history(1):
          if history_type!=2 or self.check_history(3):
            self.recordEnteredState(3)
            self.addInState(3)  # move into leaf state "Enabled.Red"
    elif common==2:
      if dest==2:
        if history_type!=2 or self.check_history(2):
          self.addInState(2)  # move into leaf state "Enabled.Green"
    elif common==3:
      if dest==3:
        if history_type!=2 or self.check_history(3):
          self.addInState(3)  # move into leaf state "Enabled.Red"

  def removeOutStates(self, common_state):

    s=self.state
    prev=None
    while s!=None:
      if self.isParent(common_state, s.StateID):
        if prev==None:
          self.state=self.state.Next
        else:
          prev.Next=s.Next
      else:
        prev=s
      s=s.Next

  def eventStr2Int(self, event):

    for i in range(2):
      if event==behaviour_generated_no_link_with_gui.EventNames[i]:
        return i
    return -1

  def stateInt2Str(self, state):

    if state==-1:
      return ""
    else:
      return behaviour_generated_no_link_with_gui.StateNames[state]

  def getCurrentStateList(self):

    sl=StringList()
    slend=sl
    s=self.state
    while s!=None:
      sm=self.Submodels[s.StateID]
      curstate=self.stateInt2Str(s.StateID)
      if sm!=None:
        slend.Next=sm.getCurrentStateList()
        while slend.Next!=None:
          slend.Next.str=curstate+"."+slend.Next.str
          slend=slend.Next
      else:
        slend.Next=StringList(curstate)
        slend=slend.Next
      s=s.Next
    return sl.Next

  def getCurrentState(self, states=None):

    if states==None:
      states=self.getCurrentStateList()
      if states!=None:
        strst="[%s'%s']" % (self.getCurrentState(states), states.str)
      else:
        strst="[]"
    else:
      if states.Next:
        strst="%s'%s', " % (self.getCurrentState(states.Next), states.Next.str)
      else:
        strst=""
    return strst

  def getParentState(self, state):

    return behaviour_generated_no_link_with_gui.ParentTable[state]

  def getSubstates(self, state):

    substates=None
    if state==-1: # substates of ""
      # add substate "Disabled"
      st=IntList()
      st.int=0
      st.Next=substates
      substates=st
      # add substate "Enabled"
      st=IntList()
      st.int=1
      st.Next=substates
      substates=st
    elif state==0: # substates of "Disabled"
      pass
    elif state==1: # substates of "Enabled"
      # add substate "Enabled.Green"
      st=IntList()
      st.int=2
      st.Next=substates
      substates=st
      # add substate "Enabled.Red"
      st=IntList()
      st.int=3
      st.Next=substates
      substates=st
    elif state==2: # substates of "Enabled.Green"
      pass
    elif state==3: # substates of "Enabled.Red"
      pass
    return substates

  def isHistoryState(self, state):

    return behaviour_generated_no_link_with_gui.HistoryStateTable[state]>0

  def isLeafState(self, state):

    if isinstance(state, int):
      return behaviour_generated_no_link_with_gui.LeafStateTable[state]!=None

    elif isinstance(state, str):
      for i in range(behaviour_generated_no_link_with_gui.StateNum):
        if behaviour_generated_no_link_with_gui.LeafStateTable[i]==None:
          continue
        if state==behaviour_generated_no_link_with_gui.LeafStateTable[i] and self.Submodels[i]==None:
          return 1
        elif startswith(state, behaviour_generated_no_link_with_gui.LeafStateTable[i]+".") and self.Submodels[i]!=None:
          SubmodelState=state[behaviour_generated_no_link_with_gui.LeafStateTable[i].length()+1:]
          return self.Submodels[i].isLeafState(SubmodelState)
    return 0

  def isHistoryUp2Date(self, state, time):

    for i in range(behaviour_generated_no_link_with_gui.StateNum):
      if self.history[state].Times[i]>=time:
        return 1
    return 0

  def mergeHistory(self, state, states, times):

    max=-1
    for i in range(behaviour_generated_no_link_with_gui.StateNum):
      if times[i]>max:
        max=times[i]
    if self.isHistoryUp2Date(state, max):
      for i in range(behaviour_generated_no_link_with_gui.StateNum):
        if times[i]>self.history[state].Times[i]:
          self.history[state].States[i]=states[i]
          self.history[state].Times[i]=times[i]
    else:
      self.history[state].States=copy.copy(states)
      self.history[state].Times=copy.copy(times)

  def recordHistory(self, top_state):

    curtime=time.time();
    s=self.state;
    while s!=None:
      child=s.StateID
      states=[]
      times=[]
      for i in range(behaviour_generated_no_link_with_gui.StateNum):
        states.append(-1)
        times.append(-1)
      states[child]=child
      times[child]=curtime
      if top_state<0 or self.isParent(top_state, child):
        parent=self.getParentState(child)
        if self.isHistoryState(child):
          self.history[child].Submodel=self.Submodels[child]
        while parent!=top_state and times[parent]!=curtime:
          states[parent]=child
          times[parent]=curtime
          if self.isHistoryState(parent):
            self.mergeHistory(parent, states, times)
          child=parent
          parent=self.getParentState(child)
      s=s.Next

  def hasHistoryRecorded(self, state):

    for i in range(behaviour_generated_no_link_with_gui.StateNum):
      if self.history[state].States[i]!=-1:
        return 1
      if self.Submodels[state]!=None:
        return 1
    return 0

  def hasOrthogonalStateInBetween(self, parent, leaf):

    return behaviour_generated_no_link_with_gui.OrthogonalInBetween[parent+1][leaf]

  def check_history(self, dest):

    s=self.state
    while s!=None:
      if self.isParent(dest, s.StateID) and not self.hasOrthogonalStateInBetween(dest, s.StateID):
        return 0
      s=s.Next
    return 1

  def getEnabledEvents(self):

    events=EventList()
    if self.isInState(1):
      events.Append("__INTERNAL_0_TIME_0")
    if self.isInState(3):
      events.Append("press")
    if self.isInState(2):
      events.Append("press")
    return events.Next

  def getHierarchy(self, start_level, state_prefix):

    h=Hierarchy()
    lasth=h
    # Generate state "Disabled" in the hierarchy table
    lasth.Next=Hierarchy()
    lasth.Next.StateName="Disabled"
    if state_prefix==None:
      lasth.Next.PathName="Disabled"
    else:
      lasth.Next.PathName=state_prefix+".Disabled"
    lasth.Next.StateNum=0
    lasth.Next.Level=start_level+0
    lasth=lasth.Next
    # Generate state "Enabled" in the hierarchy table
    lasth.Next=Hierarchy()
    lasth.Next.StateName="Enabled"
    if state_prefix==None:
      lasth.Next.PathName="Enabled"
    else:
      lasth.Next.PathName=state_prefix+".Enabled"
    lasth.Next.StateNum=1
    lasth.Next.Level=start_level+0
    lasth=lasth.Next
    # Generate state "Enabled.Green" in the hierarchy table
    lasth.Next=Hierarchy()
    lasth.Next.StateName="Green"
    if state_prefix==None:
      lasth.Next.PathName="Enabled.Green"
    else:
      lasth.Next.PathName=state_prefix+".Enabled.Green"
    lasth.Next.StateNum=2
    lasth.Next.Level=start_level+1
    lasth=lasth.Next
    # Generate state "Enabled.Red" in the hierarchy table
    lasth.Next=Hierarchy()
    lasth.Next.StateName="Red"
    if state_prefix==None:
      lasth.Next.PathName="Enabled.Red"
    else:
      lasth.Next.PathName=state_prefix+".Enabled.Red"
    lasth.Next.StateNum=3
    lasth.Next.Level=start_level+1
    lasth=lasth.Next
    return h.Next

  def topLevelHistory(self):

    s=self.state.StateID
    t=self.getParentState(s)
    while t!=-1:
      s=t
      t=self.getParentState(s)
    self.changeState(s, s)

  def runActionCode(self, code_num):

    if code_num==0: # model finalizer
      pass
    elif code_num==1: # model initializer
      pass
    elif code_num==2: # enter actions for state "Enabled"
      # a timed transition
      sched=Scheduler(self, "__INTERNAL_0_TIME_0", eval("10", self.DefaultInterpreter.locals), 1)
      sched.Next=self.TimedTransitions[1]
      self.TimedTransitions[1]=sched
      sched.start()
    elif code_num==3: # exit actions for state "Enabled"
      # clean up timed transitions
      if self.TimedTransitions[1]:
        self.TimedTransitions[1].clear()
        self.TimedTransitions[1]=None

  def testCondition(self, cond_num):

    if cond_num==0 and \
       self.DefaultInterpreter.runsource("eventhandler.TestResult=(1)")==0 and self.TestResult:
      return 1
    elif cond_num==1 and \
       self.DefaultInterpreter.runsource("eventhandler.TestResult=(1)")==0 and self.TestResult:
      return 1
    elif cond_num==2 and \
       self.DefaultInterpreter.runsource("eventhandler.TestResult=(1)")==0 and self.TestResult:
      return 1
    return 0

  def runEnterActionsForStates(self, states, recursive=0):

    if states:
      self.runEnterActionsForStates(states.Next, 0)
      self.runEnterActions(states.int)
    if recursive:
      for s in self.Submodels:
        if s:
          s.runEnterActionsForStates(s.StatesEntered, 1)

  def runEnterActions(self, state):

    if state==1: # enter action(s) for state "Enabled"
      self.runActionCode(2)

  def runExitActions(self, state):

    if state==1: # exit action(s) for state "Enabled"
      self.runActionCode(3)

  def runExitActionsForStates(self, common_state):

    substates=self.getSubstates(common_state)
    if substates==None:
      s=self.state
      while s!=None and s.StateID!=common_state:
        s=s.Next
      if s!=None and self.Submodels[s.StateID]:
        self.Submodels[s.StateID].runExitActionsForStates(-1)
      return s!=None
    else:
      has_current_substate=0
      while substates!=None:
        res=self.runExitActionsForStates(substates.int)
        has_current_substate=has_current_substate or res
        if res:
          self.runExitActions(substates.int)
        substates=substates.Next
      return has_current_substate

  def runInitializer(self):

    self.runActionCode(1)
    for s in self.Submodels:
      if s:
        s.runInitializer()

  def runFinalizer(self):
    if self.Started:
      for s in self.Submodels:
        if s:
          s.runFinalizer()
      self.runActionCode(0)
      self.Started=0

  def runInteractor(self):

    pass

  def clearEnteredStates(self):

    self.StatesEntered=None
    for s in self.Submodels:
      if s:
        s.clearEnteredStates()

  def runCode(self, c):
    if len(c)>0:
      l=""
      for i in string.split(c, "\n"):
        if len(l)==0:
          l=i
        elif string.find(i, " ")!=0 and not (string.find(i, "else")==0 and string.strip(i[4:])==":") and \
                               string.find(i, "elif ")!=0 and string.find(i, "elif\t")!=0 and \
                               not (string.find(i, "except")==0 and string.strip(i[6:])==":") and \
                               string.find(i, "except ")!=0 and string.find(i, "except\t")!=0:
          self.DefaultInterpreter.runsource(l+"\n")
          l=i
        else:
          l=l+"\n"+i
      if len(l)>0:
        self.DefaultInterpreter.runsource(l+"\n")

  def setupInterpreter(self):

    self.DefaultInterpreter.locals["eventhandler"]=self
    self.DefaultInterpreter.locals["dump_message"]=self.dump_message

  def start(self, run_enter_actions=1):
    if run_enter_actions:
      self.runEnterActionsForStates(self.StatesEntered, 1)
    self.Started=1
    if run_enter_actions:
      self.checkPendingEvents()

  def event(self, e, params=[], lock=None, call_submodels=1):

    self.EventsLock.acquire()
    running=self.HandleEventRunning
    if not running and self.Started:
      self.HandleEventRunning=1
    self.EventsLock.release()
    if not running:
      thread.start_new_thread(self.handleEvent, (e, params, lock, call_submodels))
    else:
      self.EventsLock.acquire()
      ev=EventList()
      ev.Event=[e, params, lock, call_submodels]
      if self.PendingEventsTail!=None:
        self.PendingEventsTail.Next=ev
      else:
        self.PendingEvents=ev
      self.PendingEventsTail=ev
      self.EventsLock.release()

  def checkPendingEvents(self):

    self.EventsLock.acquire()
    ev=self.PendingEvents
    if ev!=None:
      self.PendingEvents=ev.Next
      if self.PendingEvents==None:
        self.PendingEventsTail=None
    if ev:
      self.EventsLock.release()
      self.handleEvent(ev.Event[0], ev.Event[1], ev.Event[2], ev.Event[3])
    else:
      self.HandleEventRunning=0
      self.EventsLock.release()

  def get_event_params(self):

    return self.params

  def dump_message(self, msg):

    print msg

  def is_in_state(self, state, check_substate=0):

    i=0
    while i<behaviour_generated_no_link_with_gui.StateNum and behaviour_generated_no_link_with_gui.StateNames[i]!=state:
      i=i+1
    if i<behaviour_generated_no_link_with_gui.StateNum:
      return (not check_substate or self.isLeafState(i)) and self.isInState(i)
    else:
      return 0


# main
if __name__=="__main__":
  behaviour_generated_no_link_with_gui().main(sys.argv)