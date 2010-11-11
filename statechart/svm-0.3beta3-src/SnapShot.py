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


from string import *
import types
import code
import sys

def all_types():
  ts=[]
  for t in dir(types):
    l=len(t)
    if t[l-4:l]=='Type':
      ts.append(eval('types.'+t))
  return ts

def default_types():
  tn=['BufferType', 'ComplexType', 'DictProxyType', 'DictType', 'DictionaryType', 'EllipsisType', \
      'FloatType', 'IntType', 'LambdaType', 'ListType', 'LongType', 'NoneType', 'StringType', 'StringTypes', \
      'TupleType', 'TypeType', 'UnicodeType', 'XRangeType']
  ts=[]
  for t in tn:
    ts.append(eval('types.'+t))
  return ts

def make_string(e):
  se=str(e)
  if se==e:
    sse=replace(se, '\\', '\\\\')
    sse=replace(sse, '\n', '\\n')
    return '\''+replace(sse, '\'', '\\\'')+'\''
  else:
    return se
  
def take_snapshot(object, onames=None, otypes=None, append=None):
  if not otypes:
    otypes=default_types()
  if type(object) in otypes:
    e=make_string(object)
    s='/*/ = '+e+'\n'
  else:
    if not onames:
      onames=dir(object)
    s=''
    for n in onames:
      if eval('type(object.'+n+') in otypes'):
        e=make_string(eval('object.'+n))
        s=s+n+' = '+e+'\n'
    if append!=None:
      s=s+append+'\n'
  return s

def restore_snapshot(object, snapshot, obj_name=None):
  ss=split(snapshot, '\n')
  ii=code.InteractiveInterpreter(locals())
  gii=code.InteractiveInterpreter(sys.modules['__main__'].__dict__)
  for s in ss:
    if strip(s):
      pos=s.find('=')
      left=strip(s[0:pos])
      right=strip(s[pos+1:len(s)])
      if left=='/*/' and obj_name:
        gii.runsource(obj_name+'='+right)
      else:
        ii.runsource('object.'+left+'='+right)