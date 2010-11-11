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
from string import *
import code
import re

SVM_MODULE='SVMMODULE'
SVM_MODULE_RE='\A%s$'%SVM_MODULE

LEVEL_1_KEYWORDS=['AFTERSNAPSHOT', 'BEFORESNAPSHOT', 'Clock', 'DESCRIPTION',
                  'DUMP', 'Debugger', 'ENTER', 'EVENT', 'EXIT', 'Eventhandler',
                  'FINALIZER', 'IMPORTATION', 'INITIALIZER', 'INTERACTOR',
                  'InnerTransitionFirst', 'MACRO', 'None', 'OPTIONS', 'RESTORE',
                  'SNAPSHOT', 'STATECHART', 'TRANSITION', 'and', 'assert',
                  'break', 'class', 'continue', 'debugger', 'def', 'del', 'elif',
                  'else', 'except', 'exec', 'eventhandler', 'finally', 'for',
                  'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'map',
                  'not', 'or', 'pass', 'print', 'raise', 'range', 'return',
                  'try', 'while', 'Harel']
LEVEL_2_KEYWORDS=['CS', 'DS', 'EVAL', 'FS', 'HS', 'HS*', 'INSTATE', 'ITF', 'OTF',
                  'RTO', 'RTT', '__import__', 'abs', 'apply', 'callable', 'chr',
                  'cmp', 'coerce', 'compile', 'complex', 'delattr', 'dir',
                  'divmod', 'eval', 'execfile', 'filter', 'float', 'getattr',
                  'globals', 'group', 'hasattr', 'hash', 'hex', 'id', 'input',
                  'int', 'intern', 'isinstance', 'issubclass', 'joinfields', 'len',
                  'list', 'local', 'long', 'max', 'min', 'match', 'oct', 'open',
                  'ord', 'pow', 'raw_input', 'reduce', 'reload', 'repr', 'round',
                  'search', 'setattr', 'setdefault', 'slice', 'str', 'splitfields',
                  'tuple', 'type', 'unichr', 'unicode', 'vars', 'xrange', 'zip']
LEVEL_3_KEYWORDS=['<', '<=', '>', '>=', '<>', '!=', '==', '|', '^', '&', '<<', '>>',
                  '+', '-', '*', '/', '%', '~', '=', '+=', '-=', '*=', '/=', '%=',
                  '<<=', '>>=', '|=', '&=']
OPERATORS=r'<=>\!\|\^&+\-\*/%~:'
NONDEBUG_KEYWORDS=['debug', 'exit']
DEBUG_KEYWORDS=['exit']
KEYWORDS=[LEVEL_1_KEYWORDS, LEVEL_2_KEYWORDS, LEVEL_3_KEYWORDS]

TAB_SPACE=4
COMMENT_START='#'

STATECHART_DESCRIPTOR='STATECHART:'
TRANSITION_DESCRIPTOR='TRANSITION:'
PORT_DESCRIPTOR='PORT:'
DESCRIPTION_DESCRIPTOR='DESCRIPTION:'
OPTION_DESCRIPTOR='OPTIONS:'
IMPORTATION_DESCRIPTOR='IMPORTATION:'
INITIALIZER_DESCRIPTOR='INITIALIZER:'
FINALIZER_DESCRIPTOR='FINALIZER:'
INTERACTOR_DESCRIPTOR='INTERACTOR:'
MACRO_DESCRIPTOR='MACRO:'
ENTER_STATE_DESCRIPTOR='ENTER:'
EXIT_STATE_DESCRIPTOR='EXIT:'
SNAPSHOT_DESCRIPTOR='SNAPSHOT:'
RESTORE_DESCRIPTOR='RESTORE:'
COMPONENT_DESCRIPTOR='COMPONENT:'
BEFORE_SNAPSHOT_DESCRIPTOR='BEFORESNAPSHOT:'
AFTER_SNAPSHOT_DESCRIPTOR='AFTERSNAPSHOT:'
CONNECTIONS_DESCRIPTOR='CONNECTIONS:'
DESCRIPTORS=[STATECHART_DESCRIPTOR, TRANSITION_DESCRIPTOR, DESCRIPTION_DESCRIPTOR, \
             OPTION_DESCRIPTOR, IMPORTATION_DESCRIPTOR, INITIALIZER_DESCRIPTOR, \
             FINALIZER_DESCRIPTOR, INTERACTOR_DESCRIPTOR, MACRO_DESCRIPTOR, \
             ENTER_STATE_DESCRIPTOR, EXIT_STATE_DESCRIPTOR, SNAPSHOT_DESCRIPTOR, \
             RESTORE_DESCRIPTOR, BEFORE_SNAPSHOT_DESCRIPTOR, AFTER_SNAPSHOT_DESCRIPTOR, \
	     PORT_DESCRIPTOR, COMPONENT_DESCRIPTOR, CONNECTIONS_DESCRIPTOR]

COMPONENT_ID='id'
COMPONENT_NAME='name'
COMPONENT_TYPE='type'
COMPONENT_KEYS='keys'

COMPONENT_CHECKED='checked'  # not available to user

COMPONENT_PORTS='ports'

PORT_TYPE='type'
PORT_NAME='name'
PORT_BUFFER='buffer'
PORT_IN='in'
PORT_OUT='out'
PORT_INOUT='inout'

INNER_FIRST='InnerTransitionFirst'
HAREL='Harel'
ENCAPSULATED='Encapsulated'
TOP_LEVEL = 'TopLevel'
MODEL_NAME = 'ModelName'
TIMEWARP = 'Timewarp'  # timewarp toggle (MODEL_NAME must specified uniquely; IDLE_NOTIFIEE, TIME_VARIABLE and MESSAGE_TIME must be specified)
TIMEWARP_PORT = 'TimewarpPort'
TIME_VARIABLE = 'TimeVariable'  # used in timewarp
MESSAGE_TIME = 'MessageTime'  # used in timewarp
OPTION_NAMES=[INNER_FIRST, TOP_LEVEL, MODEL_NAME, TIMEWARP, TIMEWARP_PORT, TIME_VARIABLE, MESSAGE_TIME, HAREL]
DEFAULT_OPTIONS={INNER_FIRST:'0', TOP_LEVEL:'0', MODEL_NAME:None, TIMEWARP:'0', TIMEWARP_PORT:None, TIME_VARIABLE:None, MESSAGE_TIME:"None", HAREL:'1'}
ACCEPTABLE_VALUES={ENCAPSULATED:['0', '1'], INNER_FIRST:['0', '1'], TOP_LEVEL:['0', '1'], MODEL_NAME:None, TIMEWARP:['0', '1'], TIMEWARP_PORT:None, TIME_VARIABLE:None, MESSAGE_TIME:None, HAREL:['0', '1']}

INHERIT_GLOBAL_OPTIONS=[HAREL]

FINAL_STATE='[FS]'
CONCURRENT_STATE='[CS]'
DEFAULT_STATE='[DS]'
HISTORY_STATE='[HS]'
DEEP_HISTORY_STATE='[HS*]'
REVERSE_TRANSITION_ORDER='[RTO]'
INNER_TRANSITION_FIRST='[ITF]'
OUTER_TRANSITION_FIRST='[OTF]'
IMPORT_STATE='[IM]'
PARAMETERS='[PA]'
ENC_CONNECT='[EC]'
StateProperties=[FINAL_STATE, CONCURRENT_STATE, DEFAULT_STATE, HISTORY_STATE, DEEP_HISTORY_STATE,
                 REVERSE_TRANSITION_ORDER, INNER_TRANSITION_FIRST, OUTER_TRANSITION_FIRST,
                 IMPORT_STATE, PARAMETERS, ENC_CONNECT]

TRANSITION_PRIORITY='[TP]'
TransitionProperties=[HISTORY_STATE, TRANSITION_PRIORITY]

REPEATED_TIMED_TRANSITION='[RTT]'
ONCE_TIMED_TRANSITION='[OTT]'
TimedTransitionProperties=[REPEATED_TIMED_TRANSITION, ONCE_TIMED_TRANSITION]

EVALUATE_OPERATOR='EVAL'
SMALL_EVALUATE_OPERATOR='eval'
evalue=0

E_UNSNAPPABLE=['clocks', 'clock_threads', 'ttrans', 'future_events', 'event_list', 'seq_snapshots', 'event_log', 'skewed_event']
C_UNSNAPPABLE=['schedule_time', 'first_interval']

TDEFAULT_INTERACTOR="\
setup_tui_debugger(eventhandler, debugger)\n"

CDEFAULT_INTERACTOR="\
setup_cui_debugger(eventhandler, debugger)\n"

GDEFAULT_INTERACTOR="\
setup_gui_debugger(eventhandler, debugger)\n"
EVENT_MACRO={'[EVENT]': [[['[ev]', ''], ['[p]', '[]'], ['[lock]', 'None']], "eventhandler.event([ev], [p], 1, [lock])"],
	     '[EXTEVENT]': [[['[ev]', ''], ['[p]', ''], ['[rec]', '']], "eventhandler.external_event([ev], [p], [rec])"],
             '[DUMP]': [[['[msg]', '']], "dump_message([msg])"],
             '[DESCRIPTION]': [[], "eventhandler.description"],
             '[INSTATE]': [[['[state]', ''], ['[check_substate]', '1']], 'eventhandler.is_in_state([state], [check_substate])'],
	     '[PARAMS]': [[], "eventhandler.get_event_params()"],
	     '[SENDER]': [[], "eventhandler.get_event_sender()"],
	     '[SYNCALL]': [[['[event]', ''], ['[params]', ''], ['[listento]', '']], "eventhandler.synchronous_call([event], [params], [listento])"],
             '[CURRENTSTATE]': [[], "eventhandler.get_current_state()"],
	     '[SNAPSHOTREQ]': [[['[time]', '']], "eventhandler.request_snapshot([time])"],
	     '[SNAPSHOTRET]': [[['[time]', '']], "eventhandler.retrieve_snapshot([time])"]}

TPREDEFINED_MACROS=EVENT_MACRO
GPREDEFINED_MACROS=EVENT_MACRO

IMPORT_EVENT='__INTERNAL_IMPORT__'

class EventObject:
  def __init__(self, event='', sender=None):
    self.event=event
    self.sender=sender

  def __str__(self):
    return self.event

def GetSpace(num):
  return ljust('', num)

def TabToSpace(s):
  return expandtabs(s, TAB_SPACE)

def RemoveReturn(s):
  return rstrip(replace(s, '\n', ''))

def RemoveComment(s):
  pos=find(s, COMMENT_START)
  if pos>=0:
    return rstrip(s[0:pos])
  else:
    return s

def IsDescriptor(s):
  return s in DESCRIPTORS or IsTransitionDesc(s)

def IsStatechartDesc(s):
  return s==STATECHART_DESCRIPTOR

def IsTransitionDesc(s):
  s1=s;
  s2=RemoveTransitionProperty(s1);
  while s1!=s2:
    s1=s2;
    s2=RemoveTransitionProperty(s1);
  return s1==TRANSITION_DESCRIPTOR

def IsPortDesc(s):
  return s==PORT_DESCRIPTOR

def IsEnterStateDesc(s):
  return s==ENTER_STATE_DESCRIPTOR

def IsExitStateDesc(s):
  return s==EXIT_STATE_DESCRIPTOR

def IsDescriptionDesc(s):
  return s==DESCRIPTION_DESCRIPTOR

def IsOptionDesc(s):
  return s==OPTION_DESCRIPTOR

def IsImportationDesc(s):
  return s==IMPORTATION_DESCRIPTOR

def IsInitializerDesc(s):
  return s==INITIALIZER_DESCRIPTOR

def IsFinalizerDesc(s):
  return s==FINALIZER_DESCRIPTOR

def IsInteractorDesc(s):
  return s==INTERACTOR_DESCRIPTOR

def IsMacroDesc(s):
  return s==MACRO_DESCRIPTOR
  
def IsSnapshotDesc(s):
  return s==SNAPSHOT_DESCRIPTOR

def IsRestoreDesc(s):
  return s==RESTORE_DESCRIPTOR

def IsComponentDesc(s):
  return s==COMPONENT_DESCRIPTOR

def IsConnectionsDesc(s):
  return s==CONNECTIONS_DESCRIPTOR

def IsBeforeSnapshotDesc(s):
  return s==BEFORE_SNAPSHOT_DESCRIPTOR

def IsAfterSnapshotDesc(s):
  return s==AFTER_SNAPSHOT_DESCRIPTOR

def FindProperty(s, props):
  start=0
  while start<len(s):
    mc=FindLeftMatching(s, start, '[', ']')
    if mc!=None:
      for p in props:
	match=re.match('^\[[ \t]*([^\(\) \t"]+)[ \t]*<--[ \t]*([^\(\) \t"]+)[ \t]*\]$', mc[1])
	if match:
	  return [match.groups()[0], "--", match.groups()[1]]  # return a connection between ports
        ops=GetOperants(mc[1], p[1:len(p)-1])
        if ops!=None:
          return p
    else:
      break
    start=mc[0]+1
  return None

def RemoveProperty(s, props):
  start=0
  while start<len(s):
    mc=FindLeftMatching(s, start, '[', ']')
    if mc!=None:
      for p in props:
	stripit=0
	match=re.match('^\[[ \t]*([^\(\) \t"]+)[ \t]*<--[ \t]*([^\(\) \t"]+)[ \t]*\]$', mc[1])
	if match:
	  stripit=1
	else:
          ops=GetOperants(mc[1], p[1:len(p)-1])
          stripit = ops!=None
	if stripit:
          return rstrip(s[0:mc[0]]+s[mc[0]+len(mc[1]):len(s)])
    else:
      break
    start=mc[0]+1
  return rstrip(s)

def FindStateProperty(s, extra=[]):
  props=extra+StateProperties
  fsp=FindProperty(s, props)
  if fsp==None and len(s)>0:
    pos=len(s)-1
    if s[pos]==']':
      num=1
      pos=pos-1
      while pos>=0 and num>0:
        if s[pos]=='[':
	  num=num-1
        elif s[pos]==']':
	  num=num+1
        pos=pos-1
      if num==0:
        fsp=s[pos+2:len(s)-1]
        return ParseOption(fsp)
      else:
        return None
    else:
      return None
  else:
    return fsp

def RemoveStateProperty(s, extra=[]):
  props=extra+StateProperties
  rsp=RemoveProperty(s, props)
  if rsp==s and len(s)>0:
    pos=len(s)-1
    if s[pos]==']':
      num=1
      pos=pos-1
      while pos>=0 and num>0:
        if s[pos]=='[':
	  num=num-1
        elif s[pos]==']':
	  num=num+1
        pos=pos-1
      if num==0:
        rsp=rstrip(s[0:pos+1])
  return rsp

def FindTransitionProperty(s):
  ftp=FindProperty(s, TransitionProperties)
  if ftp==None:
    found=re.search('\[ *(\+|\-|)\d+ *\]$', s)
    if found!=None:
      ftp=strip(s[found.start():len(s)])
      return [TRANSITION_PRIORITY, int(ftp[1:len(ftp)-1])]
    else:
      return None
  else:
    return [ftp, 1]

def RemoveTransitionProperty(s):
  rtp=RemoveProperty(s, TransitionProperties)
  if rtp==s:
    found=re.search('\[ *(\+|\-|)\d+ *\]$', s)
    if found!=None:
      rtp=rstrip(s[0:found.start()])
  return rtp

def GetTabinSize(s):
  for i in range(len(s)):
    if s[i]!=' ':
      return i
  return len(s)

def ParseOption(s):
  s=strip(s)
  pn=0
  pos=-1
  lq1=0
  lq2=0
  esc=0
  for i in range(len(s)):
    if s[i]=='\\' and (lq1 or lq2):
      esc=not esc
    else:
      esc=0
    if s[i]=='"' and not lq2:
      if esc:
        esc=0
      else:
        lq1=not lq1
    elif s[i]=="'" and not lq1:
      if esc:
        esc=0
      else:
        lq2=not lq2
    elif s[i]=='=' and lq1==0 and lq2==0 and pn==0 and not (i<len(s)-1 and s[i+1]=='=') and not (i>0 and s[i-1]=='='):
      pos=i
      break;
    elif s[i]=='(' and lq1==0 and lq2==0:
      pn=pn+1
    elif s[i]==')' and lq1==0 and lq2==0 and pn>0:
      pn=pn-1
  if pos>=0:
    s1=s[0:pos]
    s2=s[pos+1:len(s)]
    return [strip(s1), strip(s2)]
  else:
    return None

def ParseSplit(s, c):
  lq1=0
  lq2=0
  l1=0
  l2=0
  l3=0
  i=0
  j=0
  l=len(s)
  sp=[]
  while i<l:
    if s[i]=='\\' and (lq1 or lq2):
      esc=not esc
    else:
      esc=0
    if s[i]=='"' and not lq2:
      if esc:
        esc=0
      else:
        lq1=not lq1
    elif s[i]=="'" and not lq1:
      if esc:
        esc=0
      else:
        lq2=not lq2
    elif s[i]=='(' and not lq1 and not lq2:
      l1=l1+1
    elif s[i]==')' and not lq1 and not lq2:
      l1=l1-1
    elif s[i]=='[' and not lq1 and not lq2:
      l2=l2+1
    elif s[i]==']' and not lq1 and not lq2:
      l2=l2-1
    elif s[i]=='{' and not lq1 and not lq2:
      l3=l3+1
    elif s[i]=='}' and not lq1 and not lq2:
      l3=l3-1
    elif s[i]==c and not lq1 and not lq2 and l1==0 and l2==0 and l3==0:
      sp.append(s[j:i])
      j=i+1
    i=i+1
  if j<i:
    sp.append(s[j:i])
  return sp

def ParseParameter(s):
  s=strip(s)
  found=find(s, '(')
  if s[len(s)-1]!=')' or found==-1:
    return ['['+s+']', []]
  else:
    name=strip(s[0:found])
    params=[]
    par=ParseSplit(s[found+1:len(s)-1], ',')
    for p in par:
      p=strip(p)
      if p!='':
        pp=ParseOption(p)
        if pp==None:
          params.append(['['+p+']', ''])
        else:
          params.append(['['+pp[0]+']', pp[1]])
    return ['['+name+']', params]

def ReplaceMacro(s, macro):
  import time
  t1=time.time()
  replaced=1
  start=0
  while replaced:
    replaced=0
    mc=FindLeftMatching(s, start, '[', ']')
    if mc!=None:
      start=mc[0]+1
      replaced=1
      for m in macro.keys():
        op=m[1:len(m)-1]
        ops=GetOperants(mc[1], op)
        if ops!=None:
          s=ReplaceMacroString(s, mc[0], mc[0]+len(mc[1]), macro[m])
          start=0
          break
  return s

def ReplaceMacroParam(s, param):
  for k in param.keys():
    found=find(s, k)
    while found>=0:
      s=join(split(s, k), param[k])
      found=find(s, k)
  return s

def ReplaceMacroString(s, start, end, macro):	# assume format: name [ ( ... ) ]
  sp=strip(s[start:end])
  body=macro[1]
  found=find(sp, '(')
  if found<0:
    params={}
    for p in range(len(macro[0])):
      n=macro[0][p][0]
      params['['+n+']']=macro[0][p][1]
    body=ReplaceMacroParam(body, params)
    return ReplaceMacroParam(s, {sp:body})
  else:
    name=sp[0:found]+']'
    par=ParseSplit(sp[found+1:rfind(sp, ')')], ',')
    k=0
    params={}
    l=len(macro[0])
    for p in par:
      p=strip(p)
      if p=='':
        k=k+1
        continue
      pp=ParseOption(p)
      if pp==None:
        if k<l:
          params[macro[0][k][0]]=p
          k=k+1
      else:
        params['['+pp[0]+']']=pp[1]
    for p in range(l):
      n=macro[0][p][0]
      if n!='' and not params.has_key(n):
        params[n]=macro[0][p][1]
    body=ReplaceMacroParam(body, params)
    return ReplaceMacroParam(s, {sp:body})

def EvaluateExpression(s):
  op=EVALUATE_OPERATOR
  found=1
  start=0
  while found:
    found=0
    lm=FindLeftMatching(s, start, '[', ']')
    if lm!=None:
      evalstr=GetOperants(lm[1], op)
      start=lm[0]+1
      found=1
      if evalstr!=None and evalstr!='':
        s=s[0:lm[0]]+str(eval(EvaluateExpression(evalstr)))+s[lm[0]+len(lm[1]):len(s)]
        start=0
        break
  return s

def DynamicEvaluateExpression(s):
  op=SMALL_EVALUATE_OPERATOR
  found=1
  start=0
  while found:
    found=0
    lm=FindLeftMatching(s, start, '[', ']')
    if lm!=None:
      es=GetOperants(lm[1], op)
      des=DynamicEvaluateExpression(es)
      if des==None:
        evalstr=es
      else:
        evalstr=des
      start=lm[0]+1
      found=1
      if evalstr!=None and evalstr!='':
        ii.runsource('StringUtil.evalue=('+evalstr+')')
        s=s[0:lm[0]]+str(evalue)+s[lm[0]+len(lm[1]):len(s)]
        start=0
        break
  return s

def FindInList(l, s):
  pos=0
  while pos<len(l) and l[pos]!=s:
    pos=pos+1
  if pos>=len(l):
    return -1
  else:
    return pos

def FindLeftMatching(s, start, c1, c2, esc=None):	# returns [pos, string]
  if s==None:
    return None
  pos=start
  isesc=0
  while pos<len(s) and (s[pos]!=c1 or (s[pos]==c1 and isesc)):
    if s[pos]==esc and not isesc:
      isesc=1
    else:
      isesc=0
    pos=pos+1
  if pos>=len(s):
    return None
  end=pos+1
  depth=1
  pp=-1
  isesc=0
  while end<len(s) and depth>0:
    if s[end]==esc:
      isesc=not isesc
    if s[end]==c1 and not isesc:
      depth=depth+1
    elif s[end]==c2 and not isesc:
      depth=depth-1
    if depth==2 and pp<0:	# remember the next start point
      pp=end
    if s[end]!=esc:
      isesc=0
    end=end+1
  if depth==0:
    return [pos, s[pos:end]]
  else:
    if pp>=0:
      return FindLeftMatching(s, pp, c1, c2, esc)
    else:
      return None

def GetOperants(s, op):
  s=strip(s)
  if s[0]!='[' or s[len(s)-1]!=']':
    return None
  s=strip(s[1:len(s)-1])
  if len(s)>=len(op) and s[0:len(op)]==op:
    s=strip(s[len(op):len(s)])
    if len(s)==0:
      return ''
    if s[0]!='(' or s[len(s)-1]!=')':
      return None
    else:
      return strip(s[1:len(s)-1])
  else:
    return None

def ParseArgv(s):
  sl=[]
  i=0
  inquote=0
  lastphrase=''
  while i<len(s):
    if s[i]==' ' and not inquote:
      if lastphrase:
	if len(lastphrase)>=2 and lastphrase[0]=='"' and lastphrase[len(lastphrase)-1]=='"':
	  lastphrase=lastphrase[1:len(lastphrase)-1]
	sl.append(lastphrase)
	lastphrase=''
    else:
      lastphrase=lastphrase+s[i]
    inquote=len(lastphrase)>=2 and lastphrase[0]=='"' and lastphrase[len(lastphrase)-1]!='"'
    i=i+1
  if lastphrase:
    if len(lastphrase)>=2 and lastphrase[0]=='"' and lastphrase[len(lastphrase)-1]=='"':
      lastphrase=lastphrase[1:len(lastphrase)-1]
    sl.append(lastphrase)
  return sl

def isint(s):
  try:
    int(s)
    return 1
  except:
    return None

def startswith(s, ss):
  return ss==None or (s!=None and len(s)>=len(ss) and s[0:len(ss)]==ss)
  
def endswith(s, se):
  return se==None or (s!=None and len(s)>=len(se) and s[len(s)-len(se):]==se)

def escape(s):
  dict=[['\\', '\\\\'],
        ['\n', '\\n'],
        ['"', '\\"'],
        ["'", "\\'"],
        ['\a', '\\a'],
        ['\b', '\\b'],
        ['\f', '\\f'],
        ['\r', '\\r'],
        ['\t', '\\t'],
        ['\v', '\\v']]
  for rep in dict:
    s=replace(s, rep[0], rep[1])
  s='"%s"' % s
  return s

ii=code.InteractiveInterpreter(sys.modules['__main__'].__dict__)
ii.runsource('import StringUtil')
