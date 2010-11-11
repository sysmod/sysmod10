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


#=========================================================#
# Data/Object Serialization (Thomas Huining Feng)         #
#                                                         #
# Supported types:                                        #
#   string, integer, long, float, none, list, tuple, dict #
# and instance                                            #
#=========================================================#

import types
import code
from string import *
from StringUtil import *

EXCLUDED_FIELDS=['__doc__', '__module__']

def loopfields(object):
  s=''
  for o in object:
    s=s+serialize(o)
  return s
  
def serialize(object):
  """
  s: string
  i: integer
  l: long
  f: float
  n: none
  L: list
  T: tuple
  D: dict
  I: instance
  """
  ot=type(object)
  if ot==types.StringType:
    return '(s('+replace(replace(replace(object, '/', '//'), '(', '/('), ')', '/)')+'))'
  elif ot==types.IntType:
    return '(i('+str(object)+'))'
  elif ot==types.LongType:
    return '(l('+str(object)+'))'
  elif ot==types.FloatType:
    return '(f('+str(object)+'))'
  elif ot==types.NoneType:
    return '(n)'
  elif ot==types.ListType:
    return '(L('+loopfields(object)+'))'
  elif ot==types.TupleType:
    return '(T('+loopfields(object)+'))'
  elif ot==types.DictType:
    s='(D('
    for k in object.keys():
      s=s+serialize(k)+serialize(object[k])
    s=s+'))'
    return s
  elif ot==types.InstanceType or ot==types.ComplexType:
    s='(I('
    for k in dir(object):
      if k in EXCLUDED_FIELDS:
	continue
      se=serialize(eval('object.'+k))
      if se!=None:
	s=s+k+se
    return s+'))'
  
  return None

def deserialize_error(pos):
  raise 'Error while deserializing object at position %s.'%pos

class EmptyClass:
  1

def deserialize(sobject, obj=EmptyClass()):
  """
  s: string
  i: integer
  l: long
  f: float
  n: none
  L: list
  T: tuple
  D: dict
  I: instance
  """
  if not sobject:
    return None
  match=FindLeftMatching(sobject, 0, '(', ')', '/')
  if not match:
    deserialize_error(0)
  else:
    l=len(match[1])
    if l<3 or l!=len(sobject):
      deserialize_error(l)
    elif match[1][0]!='(':
      deserialize_error(0)
    elif match[1][l-1]!=')':
      deserialize_error(l)
    else:
      ot=match[1][1]
      os=match[1][3:l-2]
      if ot=='s':
	os=replace(replace(replace(os, '/(', '('), '/)', ')'), '//', '/')
	return os
      elif ot=='i':
	return int(os)
      elif ot=='l':
	return long(os)
      elif ot=='f':
	return float(os)
      elif ot=='n':
	return None
      elif ot=='L' or ot=='T':
	if ot=='L':
	  list=[]
	else:
	  list=()
	pos=0
	while pos<len(os):
	  mat=FindLeftMatching(os, pos, '(', ')', '/')
	  if mat==None or mat[0]!=pos:
	    deserialize_error(pos+3)
	  else:
	    if ot=='L':
	      list=list+[deserialize(mat[1])]
	    else:
	      list=list+(deserialize(mat[1]),)
	    pos=pos+len(mat[1])
	return list
      elif ot=='D':
	dict={}
	dl=deserialize('(L('+os+'))')
	ldl=len(dl)
	if ldl%2==1:
	  deserialize_error(len(os)+3)
	pos=0
	while pos<len(dl):
	  dict[dl[pos]]=dl[pos+1]
	  pos=pos+2
	return dict
      elif ot=='I':
	pos=0
	while pos<len(os):
	  mat=FindLeftMatching(os, pos, '(', ')', '/')
	  if mat==None:
	    deserialize_error(pos+3)
	  else:
	    name=os[pos:mat[0]]
	    if name in dir(obj):
	      value=deserialize(mat[1], eval('obj.'+name))
	    else:
	      value=deserialize(mat[1], EmptyClass())
	    ii=code.InteractiveInterpreter(locals())
	    ii.runsource('obj.'+name+'=value')
	    pos=mat[0]+len(mat[1])
	return obj
