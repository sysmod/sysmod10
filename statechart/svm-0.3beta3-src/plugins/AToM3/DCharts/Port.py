# __Port.py_____________________________________________________
from ASGNode import *

from ATOM3Type import *

from ATOM3String import *
from ATOM3Boolean import *
from graph_Port import *
class Port(ASGNode, ATOM3Type):

   def __init__(self, parent = None):
      ASGNode.__init__(self)
      ATOM3Type.__init__(self)
      self.graphClass_ = graph_Port
      self.parent = parent
      self.name=ATOM3String('Port')
      self.keyword_= self.name
      self.is_in=ATOM3Boolean()
      self.is_in.setValue((None, 1))
      self.is_in.config = 0
      self.is_out=ATOM3Boolean()
      self.is_out.setValue((None, 1))
      self.is_out.config = 0
      self.generatedAttributes = {'name': ('ATOM3String', ),
                                  'is_in': ('ATOM3Boolean', ),
                                  'is_out': ('ATOM3Boolean', )      }
      self.realOrder = ['name','is_in','is_out']
      self.directEditing = [1,1,1]
   def clone(self):
      cloneObject = Port( self.parent )
      for atr in self.realOrder:
         cloneObject.setAttrValue(atr, self.getAttrValue(atr).clone() )
      cloneObject.keyword_ = cloneObject.name
      ASGNode.cloneActions(self, cloneObject)

      return cloneObject
   def copy(self, other):
      ATOM3Type.copy(self, other)
      for atr in self.realOrder:
         self.setAttrValue(atr, other.getAttrValue(atr) )
      self.keyword_ = self.name
      ASGNode.copy(self, other)

   def preCondition (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.preCondition(actionID, params)
      else: return None
   def postCondition (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.postCondition(actionID, params)
      else: return None


