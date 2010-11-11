# __History.py_____________________________________________________
from ASGNode import *

from ATOM3Type import *

from ATOM3Boolean import *
from ATOM3String import *
from graph_History import *
class History(ASGNode, ATOM3Type):

   def __init__(self, parent = None):
      ASGNode.__init__(self)
      ATOM3Type.__init__(self)
      self.graphClass_ = graph_History
      self.parent = parent
      self.is_default=ATOM3Boolean()
      self.is_default.setValue((None, 0))
      self.is_default.config = 0
      self.name=ATOM3String('')
      self.star=ATOM3Boolean()
      self.star.setValue((None, 0))
      self.star.config = 0
      self.generatedAttributes = {'is_default': ('ATOM3Boolean', ),
                                  'name': ('ATOM3String', ),
                                  'star': ('ATOM3Boolean', )      }
      self.realOrder = ['is_default','name','star']
      self.directEditing = [1,1,1]
   def clone(self):
      cloneObject = History( self.parent )
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
         res = self.History_CREATE(params)
         if res: return res
      if actionID == self.DRAG:
         res = self.History_DRAG(params)
         if res: return res
      if actionID == self.DROP:
         res = self.History_DROP(params)
         if res: return res
      if actionID == self.MOVE:
         res = self.History_MOVE(params)
         if res: return res
      if self.graphObject_:
         return self.graphObject_.postCondition(actionID, params)
      else: return None
   def History_CREATE(self, params):
      import statechart_utils
      statechart_utils.History_CREATE(self)
      

   def History_DRAG(self, params):
      import statechart_utils
      statechart_utils.History_DRAG(self)
      

   def History_DROP(self, params):
      import statechart_utils
      statechart_utils.History_DROP(self)
      

   def History_MOVE(self, params):
      import statechart_utils
      statechart_utils.History_MOVE(self)
      



