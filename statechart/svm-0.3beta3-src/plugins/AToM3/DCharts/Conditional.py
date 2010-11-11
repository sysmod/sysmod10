# __Conditional.py_____________________________________________________
from ASGNode import *

from ATOM3Type import *

from ATOM3String import *
from graph_Conditional import *
class Conditional(ASGNode, ATOM3Type):

   def __init__(self, parent = None):
      ASGNode.__init__(self)
      ATOM3Type.__init__(self)
      self.graphClass_ = graph_Conditional
      self.parent = parent
      self.name=ATOM3String('Conditional')
      self.generatedAttributes = {'name': ('ATOM3String', )      }
      self.realOrder = ['name']
      self.directEditing = [1]
   def clone(self):
      cloneObject = Conditional( self.parent )
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
      if actionID == self.CREATE:
         res = self.Conditional_CREATE(params)
         if res: return res
      if actionID == self.DRAG:
         res = self.Conditional_DRAG(params)
         if res: return res
      if actionID == self.DROP:
         res = self.Conditional_DROP(params)
         if res: return res
      if actionID == self.MOVE:
         res = self.Conditional_MOVE(params)
         if res: return res
      if self.graphObject_:
         return self.graphObject_.postCondition(actionID, params)
      else: return None
   def Conditional_CREATE(self, params):
      import DCharts_utils
      DCharts_utils.Conditional_CREATE(self)
      

   def Conditional_DRAG(self, params):
      import DCharts_utils
      DCharts_utils.Conditional_DRAG(self)
      

   def Conditional_DROP(self, params):
      import DCharts_utils
      DCharts_utils.Conditional_DROP(self)
      

   def Conditional_MOVE(self, params):
      import DCharts_utils
      DCharts_utils.Conditional_MOVE(self)
      



