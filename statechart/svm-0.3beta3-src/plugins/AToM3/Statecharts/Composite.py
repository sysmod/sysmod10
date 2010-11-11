# __Composite.py_____________________________________________________
from ASGNode import *

from ATOM3Type import *

from ATOM3String import *
from ATOM3Boolean import *
from ATOM3Text import *
from graph_Composite import *
class Composite(ASGNode, ATOM3Type):

   def __init__(self, parent = None):
      ASGNode.__init__(self)
      ATOM3Type.__init__(self)
      self.graphClass_ = graph_Composite
      self.parent = parent
      self.name=ATOM3String('Composite')
      self.is_default=ATOM3Boolean()
      self.is_default.setValue((None, 0))
      self.is_default.config = 0
      self.visible=ATOM3Boolean()
      self.visible.setValue((None, 1))
      self.visible.config = 0
      self.auto_adjust=ATOM3Boolean()
      self.auto_adjust.setValue((None, 1))
      self.auto_adjust.config = 0
      self.enter_action=ATOM3Text('', 60,15 )
      self.exit_action=ATOM3Text('', 60,15 )
      self.generatedAttributes = {'name': ('ATOM3String', ),
                                  'is_default': ('ATOM3Boolean', ),
                                  'visible': ('ATOM3Boolean', ),
                                  'auto_adjust': ('ATOM3Boolean', ),
                                  'enter_action': ('ATOM3Text', ),
                                  'exit_action': ('ATOM3Text', )      }
      self.realOrder = ['name','is_default','visible','auto_adjust','enter_action','exit_action']
      self.directEditing = [1,1,1,1,1,1]
   def clone(self):
      cloneObject = Composite( self.parent )
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
         res = self.Composite_CREATE(params)
         if res: return res
      if actionID == self.DRAG:
         res = self.Composite_DRAG(params)
         if res: return res
      if actionID == self.MOVE:
         res = self.Composite_MOVE(params)
         if res: return res
      if actionID == self.DROP:
         res = self.Composite_DROP(params)
         if res: return res
      if actionID == self.EDIT:
         res = self.Composite_EDIT(params)
         if res: return res
      if self.graphObject_:
         return self.graphObject_.postCondition(actionID, params)
      else: return None
   def Composite_CREATE(self, params):
      import statechart_utils
      statechart_utils.Composite_CREATE(self)
      

   def Composite_DRAG(self, params):
      import statechart_utils
      statechart_utils.Composite_DRAG(self)
      

   def Composite_MOVE(self, params):
      import statechart_utils
      statechart_utils.Composite_MOVE(self)
      

   def Composite_DROP(self, params):
      import statechart_utils
      statechart_utils.Composite_DROP(self)
      

   def Composite_EDIT(self, params):
      import statechart_utils
      statechart_utils.Composite_EDIT(self)
      



