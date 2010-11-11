# __ASG_Statechart.py_____________________________________________________
from ASG import *
from ATOM3Type       import *
class ASG_Statechart(ASG, ATOM3Type):

   def __init__(self, parent= None, ASGroot = None):
      ASG.__init__(self, 'Statechart', ASGroot, ['ASG_Statechart' ,'Composite' ,'Basic' ,'History' ,'Orthogonal' ,'visual_settings' ,'contains' ,'Hyperedge' ,'orthogonality'])

      ATOM3Type.__init__(self)
      self.parent = parent
      self.generatedAttributes = {      }
      self.realOrder = []
      self.directEditing = []
   def clone(self):
      return self
   def copy(self, other):
      ATOM3Type.copy(self, other)
      for atr in self.realOrder:
         self.setAttrValue(atr, other.getAttrValue(atr) )
   def open(self, parent, topWindowParent):
       from ATOM3 import *
       a = ATOM3(topWindowParent, 'Statechart', 0, 1, self)
       #self.writeContents(a)
       return a
   def preCondition (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.preCondition(actionID, params)
      else: return None
   def postCondition (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.postCondition(actionID, params)
      else: return None


