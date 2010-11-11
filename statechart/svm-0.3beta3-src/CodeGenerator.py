#---------------------------------------------------------------------
#      SCC (StateChart Compiler)
#           -- a compiler for an extended statechart formalism
#---------------------------------------------------------------------
#
# Copyright (C) 2003 Thomas Huining Feng
#
#---------------------------------------------------------------------
# Address:      MSDL, SOCS, McGill Univ., Montreal, Canada
# HomePage:     http://msdl.cs.mcgill.ca/people/tfeng/
# SCC HomePage: http://msdl.cs.mcgill.ca/people/tfeng/?research=scc
# Download:     http://savannah.nongnu.org/files/?group=svm
# CVS:          :pserver:anoncvs@subversions.gnu.org:/cvsroot/svm
#               (projects "svm" and "jsvm")
# Email:        hfeng2@cs.mcgill.ca
#---------------------------------------------------------------------
#
# This file is part of SCC.
#
#---------------------------------------------------------------------
# SCC is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your
# option) any later version.
#
# SCC is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public
# License for more details.
#
# You should have received a copy of the GNU General Public License
# along with SCC; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
#---------------------------------------------------------------------

from StringUtil import *
from EventHandler import EventHandler
import string

class CodeGenerator:
  
  def __init__(self, eventhandler, postfix):
    self.eventhandler=eventhandler
    self.required_models=[eventhandler]
    self.compiled_files={eventhandler.model_name:eventhandler.options[MODEL_NAME]}
    self.compiled_models={eventhandler.options[MODEL_NAME]:eventhandler}
    self.generated_models={eventhandler.options[MODEL_NAME]:self}
    self.submodels={}
    self.postfix=postfix

  def generate(self):
    jf=open(self.eventhandler.options[MODEL_NAME]+"."+self.postfix, "w")
    code=self.generate_code()
    jf.write(code)
    jf.close()

  def generate_code(self):  # must be overriden
    pass

  def init_generator(self):
    self.state_table1={}
    self.state_table2={}
    self.state_num=self.generate_state_table(self.eventhandler.stateH)

    self.event_table1={}
    self.event_table2={}
    self.event_num=self.generate_event_table(self.eventhandler.trans)
    
    self.check_import()

  def generate_state_table(self, stateH, start_num=0, start_path=''):
    keys=stateH.keys()
    keys.sort()
    for s in keys:
      if not s in StateProperties:
	path=self.eventhandler.append_path(start_path, s)
	self.state_table1[start_num]=path
	self.state_table2[path]=start_num
	start_num=start_num+1
	start_num=self.generate_state_table(stateH[s], start_num, path)
    return start_num

  def get_state_num(self, s):
    return self.state_table2[s]

  def generate_event_table(self, trans, start_num=0):
    keys=trans.keys()
    keys.sort()
    for e in keys:
      self.event_table1[start_num]=e
      self.event_table2[e]=start_num
      start_num=start_num+1
    return start_num

  def check_import(self, stateH=None, path=''):
    if stateH==None:
      stateH=self.eventhandler.stateH
    keys=stateH.keys()
    keys.sort()
    for s in keys:
      if not s in StateProperties:
	newstateH=stateH[s]
	newpath=self.eventhandler.append_path(path, s)
	self.check_import_mdl(path, s, newstateH)
	self.check_import(newstateH, newpath)

  def check_import_mdl(self, path, s, states):
    if states[IMPORT_STATE]!=None:
      keys=states.keys()
      keys.sort()
      for subs in keys:
        if not subs in StateProperties:
          print 'WARNING: Importation state has substate(s). This may cause unexpected error.'
          break
      filename=DynamicEvaluateExpression(states[IMPORT_STATE])
      params={}
      keys=states[PARAMETERS].keys()
      keys.sort()
      for k in keys:
        p=states[PARAMETERS][k]
        b=DynamicEvaluateExpression(p[1])
        params[k]=[p[0], b]
      stnum=self.get_state_num(self.eventhandler.append_path(path, s))
      if not self.compiled_files.has_key(filename):
        eh=EventHandler(filename, None, params, 0, 0, [], [], 0, None, self.eventhandler.options)
        self.required_models.append(eh)
	self.compiled_files[filename]=eh.options[MODEL_NAME]
        self.submodels[stnum]=eh.options[MODEL_NAME]
      else:
        self.submodels[stnum]=self.compiled_files[filename]

  def find_submodel_path(self, path):
    paths=split(path, ".")
    i=0
    p=""
    while i<len(paths):
      p2=self.eventhandler.append_path(p, paths[i])
      if self.state_table2.has_key(p2):
	p=p2
      else:
	break
      i=i+1
    sp=""
    while i<len(paths):
      sp=self.eventhandler.append_path(sp, paths[i])
      i=i+1
    return [p, sp]

  def has_orthogonal_substate(self, path):
    stateH=self.eventhandler.stateH
    paths=split(path, ".")
    for p in paths:
      stateH=stateH[p]
    keys=stateH.keys()
    keys.sort()
    for s in keys:
      if not s in StateProperties:
	if stateH[s][CONCURRENT_STATE]:
	  return 1
    return 0

  def is_leaf_state(self, path, consider_import=1):
    stateH=self.eventhandler.stateH
    paths=split(path, ".")
    for p in paths:
      stateH=stateH[p]
    if consider_import and stateH[IMPORT_STATE]:
      return 0
    keys=stateH.keys()
    for s in keys:
      if not s in StateProperties:
	return 0
    return 1

  def has_history_state(self, path):
    stateH=self.eventhandler.stateH
    paths=split(path, ".")
    for p in paths:
      stateH=stateH[p]
    if stateH[DEEP_HISTORY_STATE]:
      return 2
    elif stateH[HISTORY_STATE]:
      return 1
    return 0

  def is_final_state(self, s):
    path=split(s, '.')
    states=self.eventhandler.stateH
    for p in path:
      if states[p][FINAL_STATE]:
        return 1
      states=states[p]
    return 0


def replace_macros(text, priority_macros, macros):
  for m in priority_macros:
    text=string.replace(text, m, macros[m])
  for m in macros.keys():
    if not m in priority_macros:
      text=string.replace(text, m, macros[m])
  return text
