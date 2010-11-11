# __Orthogonal.py_____________________________________________________
from ASGNode import *

from ATOM3Type import *

from ATOM3String import *
from ATOM3Boolean import *
from graph_Orthogonal import *
class Orthogonal(ASGNode, ATOM3Type):

   def __init__(self, parent = None):
      ASGNode.__init__(self)
      ATOM3Type.__init__(self)
      self.graphClass_ = graph_Orthogonal
      self.parent = parent
      self.name=ATOM3String('Orthogonal')
      self.keyword_= self.name
      self.visible=ATOM3Boolean()
      self.visible.setValue((None, 1))
      self.visible.config = 0
      self.auto_adjust=ATOM3Boolean()
      self.auto_adjust.setValue((None, 1))
      self.auto_adjust.config = 0
      self.generatedAttributes = {'name': ('ATOM3String', ),
                                  'visible': ('ATOM3Boolean', ),
                                  'auto_adjust': ('ATOM3Boolean', )      }
      self.realOrder = ['name','visible','auto_adjust']
      self.directEditing = [1,1,1]
   def clone(self):
      cloneObject = Orthogonal( self.parent )
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
         res = self.Orthogonal_CREATE(params)
         if res: return res
      if actionID == self.DRAG:
         res = self.Orthogonal_DRAG(params)
         if res: return res
      if actionID == self.MOVE:
         res = self.Orthogonal_MOVE(params)
         if res: return res
      if actionID == self.DROP:
         res = self.Orthogonal_DROP(params)
         if res: return res
      if actionID == self.EDIT:
         res = self.Orthogonal_EDIT(params)
         if res: return res
      if self.graphObject_:
         return self.graphObject_.postCondition(actionID, params)
      else: return None
   def Orthogonal_CREATE(self, params):
      import DCharts_utils
      DCharts_utils.Orthogonal_CREATE(self)
      

   def Orthogonal_DRAG(self, params):
      import DCharts_utils
      DCharts_utils.Orthogonal_DRAG(self)
      

   def Orthogonal_MOVE(self, params):
      import DCharts_utils
      DCharts_utils.Orthogonal_MOVE(self)
      

   def Orthogonal_DROP(self, params):
      import DCharts_utils
      DCharts_utils.Orthogonal_DROP(self)
      

   def Orthogonal_EDIT(self, params):
      import DCharts_utils
      DCharts_utils.Orthogonal_EDIT(self)
      



