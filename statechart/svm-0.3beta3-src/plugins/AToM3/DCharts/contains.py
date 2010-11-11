# __contains.py_____________________________________________________
from ASGNode import *

from ATOM3Type import *

from graph_contains import *
class contains(ASGNode, ATOM3Type):

   def __init__(self, parent = None):
      ASGNode.__init__(self)
      ATOM3Type.__init__(self)
      self.graphClass_ = graph_contains
      self.parent = parent
      self.generatedAttributes = {      }
      self.realOrder = []
      self.directEditing = []
   def clone(self):
      cloneObject = contains( self.parent )
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
      if actionID == self.DELETE or actionID == self.DISCONNECT:
         res = self.contains_DELETE(params)
         if res: return res
      if self.graphObject_:
         return self.graphObject_.preCondition(actionID, params)
      else: return None
   def postCondition (self, actionID, * params):
      if actionID == self.CREATE:
         res = self.contains_CREATE(params)
         if res: return res
      if actionID == self.CONNECT:
         res = self.contains_CONNECT(params)
         if res: return res
      if self.graphObject_:
         return self.graphObject_.postCondition(actionID, params)
      else: return None
   def contains_CREATE(self, params):
      import DCharts_utils
      DCharts_utils.contains_CREATE(self)
      

   def contains_CONNECT(self, params):
      import DCharts_utils
      DCharts_utils.contains_CONNECT(self)
      

   def contains_DELETE(self, params):
      import DCharts_utils
      DCharts_utils.contains_DELETE(self)
      
      



