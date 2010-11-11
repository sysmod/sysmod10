# __visual_settings.py_____________________________________________________
from ASGNode import *

from ATOM3Type import *

from ATOM3Boolean import *
from ATOM3Float import *
from ATOM3String import *
from graph_visual_settings import *
class visual_settings(ASGNode, ATOM3Type):

   def __init__(self, parent = None):
      ASGNode.__init__(self)
      ATOM3Type.__init__(self)
      self.graphClass_ = graph_visual_settings
      self.parent = parent
      self.contains_links_visible=ATOM3Boolean()
      self.contains_links_visible.setValue((None, 0))
      self.contains_links_visible.config = 0
      self.Composite_default_height=ATOM3Float(50.0)
      self.Composite_default_width=ATOM3Float(50.0)
      self.contains_color=ATOM3String('pink')
      self.orthogonality_links_visible=ATOM3Boolean()
      self.orthogonality_links_visible.setValue((None, 0))
      self.orthogonality_links_visible.config = 0
      self.orthogonality_color=ATOM3String('lightblue')
      self.Hyperedge_links_visible=ATOM3Boolean()
      self.Hyperedge_links_visible.setValue((None, 1))
      self.Hyperedge_links_visible.config = 0
      self.Hyperedge_color=ATOM3String('darkblue')
      self.Composite_color=ATOM3String('darkblue')
      self.Orthogonal_color=ATOM3String('darkgray')
      self.generatedAttributes = {'contains_links_visible': ('ATOM3Boolean', ),
                                  'Composite_default_height': ('ATOM3Float', ),
                                  'Composite_default_width': ('ATOM3Float', ),
                                  'contains_color': ('ATOM3String', ),
                                  'orthogonality_links_visible': ('ATOM3Boolean', ),
                                  'orthogonality_color': ('ATOM3String', ),
                                  'Hyperedge_links_visible': ('ATOM3Boolean', ),
                                  'Hyperedge_color': ('ATOM3String', ),
                                  'Composite_color': ('ATOM3String', ),
                                  'Orthogonal_color': ('ATOM3String', )      }
      self.realOrder = ['contains_links_visible','Composite_default_height','Composite_default_width','contains_color','orthogonality_links_visible','orthogonality_color','Hyperedge_links_visible','Hyperedge_color','Composite_color','Orthogonal_color']
      self.directEditing = [1,1,1,1,1,1,1,1,1,1]
   def clone(self):
      cloneObject = visual_settings( self.parent )
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
      if actionID == self.EDIT or actionID == self.CREATE:
         res = self.apply_settings(params)
         if res: return res
      if self.graphObject_:
         return self.graphObject_.postCondition(actionID, params)
      else: return None
   def apply_settings(self, params):
      import DCharts_utils
      DCharts_utils.visual_settings_EDIT_CREATE(self)
      



