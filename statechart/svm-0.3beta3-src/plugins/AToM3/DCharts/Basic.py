# __Basic.py_____________________________________________________
from ASGNode import *

from ATOM3Type import *

from ATOM3String import *
from ATOM3Boolean import *
from ATOM3Text import *
from graph_Basic import *
class Basic(ASGNode, ATOM3Type):

   def __init__(self, parent = None):
      ASGNode.__init__(self)
      ATOM3Type.__init__(self)
      self.graphClass_ = graph_Basic
      self.parent = parent
      self.name=ATOM3String('Basic')
      self.keyword_= self.name
      self.is_default=ATOM3Boolean()
      self.is_default.setValue((None, 0))
      self.is_default.config = 0
      self.enter_action=ATOM3Text('\n', 60,15 )
      self.exit_action=ATOM3Text('\n', 60,15 )
      self.generatedAttributes = {'name': ('ATOM3String', ),
                                  'is_default': ('ATOM3Boolean', ),
                                  'enter_action': ('ATOM3Text', ),
                                  'exit_action': ('ATOM3Text', )      }
      self.realOrder = ['name','is_default','enter_action','exit_action']
      self.directEditing = [1,1,1,1]
   def clone(self):
      cloneObject = Basic( self.parent )
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
      if actionID == self.CREATE:
         res = self.Basic_CREATE(params)
         if res: return res
      if actionID == self.DRAG:
         res = self.Basic_DRAG(params)
         if res: return res
      if actionID == self.DROP:
         res = self.Basic_DROP(params)
         if res: return res
      if actionID == self.MOVE:
         res = self.Basic_MOVE(params)
         if res: return res
      if self.graphObject_:
         return self.graphObject_.postCondition(actionID, params)
      else: return None
   def Basic_CREATE(self, params):
      import DCharts_utils
      DCharts_utils.Basic_CREATE(self)
      

   def Basic_DRAG(self, params):
      import DCharts_utils
      DCharts_utils.Basic_DRAG(self)
      

   def Basic_DROP(self, params):
      import DCharts_utils
      DCharts_utils.Basic_DROP(self)
      

   def Basic_MOVE(self, params):
      import DCharts_utils
      DCharts_utils.Basic_MOVE(self)
      



