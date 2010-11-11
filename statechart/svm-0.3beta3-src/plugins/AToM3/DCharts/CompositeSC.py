# __CompositeSC.py_____________________________________________________
from ASGNode import *

from ATOM3Type import *

from ATOM3Boolean import *
from ATOM3Integer import *
from ATOM3String import *
from graph_CompositeSC import *
class CompositeSC(ASGNode, ATOM3Type):

   def __init__(self, parent = None):
      ASGNode.__init__(self)
      ATOM3Type.__init__(self)
      self.graphClass_ = graph_CompositeSC
      self.parent = parent
      self.isOrthogonal=ATOM3Boolean()
      self.isOrthogonal.setValue((None, 0))
      self.isOrthogonal.config = 0
      self.numOrthComponents=ATOM3Integer(0)
      self.name=ATOM3String('')
      self.isDefault=ATOM3Boolean()
      self.isDefault.setValue(('', 0))
      self.isDefault.config = 0
      self.generatedAttributes = {'isOrthogonal': ('ATOM3Boolean', ),
                                  'numOrthComponents': ('ATOM3Integer', ),
                                  'name': ('ATOM3String', ),
                                  'isDefault': ('ATOM3Boolean', )      }
      self.realOrder = ['isOrthogonal','numOrthComponents','name','isDefault']
   def clone(self):
      cloneObject = CompositeSC( self.parent )
      for atr in self.realOrder:
         cloneObject.setAttrValue(atr, self.getAttrValue(atr).clone() )
      ASGNode.cloneActions(self, cloneObject)

      return cloneObject
   def copy(self, other):
      ATOM3Type.copy(self, other)
      for atr in self.realOrder:
         self.setAttrValue(atr, other.getAttrValue(atr) )
      ASGNode.copy(self, other)

   def preCondition (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.preCondition(actionID, params)
      else: return None
   def postCondition (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.postCondition(actionID, params)
      else: return None


