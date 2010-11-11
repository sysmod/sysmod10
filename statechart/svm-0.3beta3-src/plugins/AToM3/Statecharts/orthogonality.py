# __orthogonality.py_____________________________________________________
from ASGNode import *

from ATOM3Type import *

from graph_orthogonality import *
class orthogonality(ASGNode, ATOM3Type):

   def __init__(self, parent = None):
      ASGNode.__init__(self)
      ATOM3Type.__init__(self)
      self.graphClass_ = graph_orthogonality
      self.parent = parent
      self.generatedAttributes = {      }
      self.realOrder = []
      self.directEditing = []
   def clone(self):
      cloneObject = orthogonality( self.parent )
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
         res = self.orthogonality_DELETE(params)
         if res: return res
      if self.graphObject_:
         return self.graphObject_.preCondition(actionID, params)
      else: return None
   def postCondition (self, actionID, * params):
      if actionID == self.CREATE:
         res = self.orthogonality_CREATE(params)
         if res: return res
      if actionID == self.CONNECT:
         res = self.orthogonality_CONNECT(params)
         if res: return res
      if self.graphObject_:
         return self.graphObject_.postCondition(actionID, params)
      else: return None
   def orthogonality_CREATE(self, params):
      import statechart_utils
      statechart_utils.orthogonality_CREATE(self)
      
      

   def orthogonality_CONNECT(self, params):
      import statechart_utils
      statechart_utils.orthogonality_CONNECT(self)
      

   def orthogonality_DELETE(self, params):
      import statechart_utils
      statechart_utils.orthogonality_DELETE(self)
      



