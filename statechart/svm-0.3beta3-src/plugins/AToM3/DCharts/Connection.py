# __Connection.py_____________________________________________________
from ASGNode import *

from ATOM3Type import *

from ATOM3String import *
from graph_Connection import *
class Connection(ASGNode, ATOM3Type):

   def __init__(self, parent = None):
      ASGNode.__init__(self)
      ATOM3Type.__init__(self)
      self.graphClass_ = graph_Connection
      self.parent = parent
      self.name=ATOM3String('Connection')
      self.keyword_= self.name
      self.port=ATOM3String('')
      self.server_port=ATOM3String('')
      self.generatedAttributes = {'name': ('ATOM3String', ),
                                  'port': ('ATOM3String', ),
                                  'server_port': ('ATOM3String', )      }
      self.realOrder = ['name','port','server_port']
      self.directEditing = [1,1,1]
   def clone(self):
      cloneObject = Connection( self.parent )
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


