from ASG_Statechart import *
from graph_ASG_ERmetaMetaModel import *
from Tkinter         import *
from ATOM3TypeInfo   import *
from ATOM3String     import *
from StatusBar       import *
from ATOM3TypeDialog import *

from Composite       import *
from Basic       import *
from History       import *
from Orthogonal       import *
from visual_settings       import *
from contains       import *
from Hyperedge       import *
from orthogonality       import *
def createNewASGroot(self):
   return ASG_Statechart(self, None)

def createModelMenu(self, modelMenu):
    "Creates a customized Model Menu for the actual formalism"
    modelMenu = Menu(self.mmtoolMenu, tearoff=0)
    modelMenu.add_command(label="new Composite", command=lambda x=self: x.newModesComposite(x) )
    modelMenu.add_command(label="new Basic", command=lambda x=self: x.newModesBasic(x) )
    modelMenu.add_command(label="new History", command=lambda x=self: x.newModesHistory(x) )
    modelMenu.add_command(label="new Orthogonal", command=lambda x=self: x.newModesOrthogonal(x) )
    modelMenu.add_command(label="new visual_settings", command=lambda x=self: x.newModesvisual_settings(x) )
    modelMenu.add_command(label="new contains", command=lambda x=self: x.newModescontains(x) )
    modelMenu.add_command(label="new Hyperedge", command=lambda x=self: x.newModesHyperedge(x) )
    modelMenu.add_command(label="new orthogonality", command=lambda x=self: x.newModesorthogonality(x) )
def setConnectivity(self):
    self.ConnectivityMap['Basic']={
           'Hyperedge': []
          ,'Basic': [( 'Hyperedge', self.createNewHyperedge)]
          ,'visual_settings': []
          ,'Orthogonal': []
          ,'Composite': [( 'Hyperedge', self.createNewHyperedge)]
          ,'contains': []
          ,'orthogonality': []
          ,'History': [( 'Hyperedge', self.createNewHyperedge)] }
    self.ConnectivityMap['Hyperedge']={
           'Hyperedge': [( 'Composite', self.createNewComposite), ( 'Basic', self.createNewBasic), ( 'History', self.createNewHistory)]
          ,'Basic': []
          ,'visual_settings': []
          ,'Orthogonal': []
          ,'Composite': []
          ,'contains': [( 'Composite', self.createNewComposite)]
          ,'orthogonality': [( 'Composite', self.createNewComposite)]
          ,'History': [] }
    self.ConnectivityMap['visual_settings']={
           'Hyperedge': []
          ,'Basic': []
          ,'visual_settings': []
          ,'Orthogonal': []
          ,'Composite': []
          ,'contains': []
          ,'orthogonality': []
          ,'History': [] }
    self.ConnectivityMap['Orthogonal']={
           'Hyperedge': []
          ,'Basic': [( 'contains', self.createNewcontains)]
          ,'visual_settings': []
          ,'Orthogonal': []
          ,'Composite': [( 'contains', self.createNewcontains)]
          ,'contains': []
          ,'orthogonality': []
          ,'History': [( 'contains', self.createNewcontains)] }
    self.ConnectivityMap['Composite']={
           'Hyperedge': []
          ,'Basic': [( 'contains', self.createNewcontains), ( 'Hyperedge', self.createNewHyperedge)]
          ,'visual_settings': []
          ,'Orthogonal': [( 'orthogonality', self.createNeworthogonality)]
          ,'Composite': [( 'contains', self.createNewcontains), ( 'Hyperedge', self.createNewHyperedge)]
          ,'contains': []
          ,'orthogonality': []
          ,'History': [( 'contains', self.createNewcontains), ( 'Hyperedge', self.createNewHyperedge)] }
    self.ConnectivityMap['contains']={
           'Hyperedge': [( 'Composite', self.createNewComposite), ( 'Basic', self.createNewBasic), ( 'History', self.createNewHistory)]
          ,'Basic': []
          ,'visual_settings': []
          ,'Orthogonal': []
          ,'Composite': []
          ,'contains': [( 'Composite', self.createNewComposite)]
          ,'orthogonality': [( 'Composite', self.createNewComposite)]
          ,'History': [] }
    self.ConnectivityMap['orthogonality']={
           'Hyperedge': []
          ,'Basic': []
          ,'visual_settings': []
          ,'Orthogonal': []
          ,'Composite': []
          ,'contains': [( 'Orthogonal', self.createNewOrthogonal)]
          ,'orthogonality': []
          ,'History': [] }
    self.ConnectivityMap['History']={
           'Hyperedge': []
          ,'Basic': [( 'Hyperedge', self.createNewHyperedge)]
          ,'visual_settings': []
          ,'Orthogonal': []
          ,'Composite': [( 'Hyperedge', self.createNewHyperedge)]
          ,'contains': []
          ,'orthogonality': []
          ,'History': [( 'Hyperedge', self.createNewHyperedge)] }
    
    self.CardinalityTable['Composite']={
          'Composite': []
          ,'Basic': []
          ,'History': []
          ,'Orthogonal': []
          ,'visual_settings': []
          ,'contains': [('0', 'N', 'Source'), ('0', '1', 'Destination')]
          ,'Hyperedge': [('0', 'N', 'Destination'), ('0', 'N', 'Source')]
          ,'orthogonality': [('0', 'N', 'Source')] }
    self.CardinalityTable['Basic']={
          'Composite': []
          ,'Basic': []
          ,'History': []
          ,'Orthogonal': []
          ,'visual_settings': []
          ,'contains': [('0', '1', 'Destination')]
          ,'Hyperedge': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'orthogonality': [] }
    self.CardinalityTable['History']={
          'Composite': []
          ,'Basic': []
          ,'History': []
          ,'Orthogonal': []
          ,'visual_settings': []
          ,'contains': [('0', '1', 'Destination')]
          ,'Hyperedge': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'orthogonality': [] }
    self.CardinalityTable['Orthogonal']={
          'Composite': []
          ,'Basic': []
          ,'History': []
          ,'Orthogonal': []
          ,'visual_settings': []
          ,'contains': [('0', 'N', 'Source')]
          ,'Hyperedge': []
          ,'orthogonality': [('0', 'N', 'Destination')] }
    self.CardinalityTable['visual_settings']={
          'Composite': []
          ,'Basic': []
          ,'History': []
          ,'Orthogonal': []
          ,'visual_settings': []
          ,'contains': []
          ,'Hyperedge': []
          ,'orthogonality': [] }
    self.CardinalityTable['contains']={
          'Composite': [('0', 'N', 'Destination'), ('0', 'N', 'Source')]
          ,'Basic': [('0', 'N', 'Source')]
          ,'History': [('0', 'N', 'Source')]
          ,'Orthogonal': [('0', 'N', 'Destination')]
          ,'visual_settings': []
          ,'contains': []
          ,'Hyperedge': []
          ,'orthogonality': [] }
    self.CardinalityTable['Hyperedge']={
          'Composite': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'Basic': [('0', 'N', 'Destination'), ('0', 'N', 'Source')]
          ,'History': [('0', 'N', 'Destination'), ('0', '1', 'Source')]
          ,'Orthogonal': []
          ,'visual_settings': []
          ,'contains': []
          ,'Hyperedge': []
          ,'orthogonality': [] }
    self.CardinalityTable['orthogonality']={
          'Composite': [('1', '1', 'Destination')]
          ,'Basic': []
          ,'History': []
          ,'Orthogonal': [('1', '1', 'Source')]
          ,'visual_settings': []
          ,'contains': []
          ,'Hyperedge': []
          ,'orthogonality': [] }
    
    self.entitiesInMetaModel['Statechart']=["Composite", "Basic", "History", "Orthogonal", "visual_settings", "contains", "Hyperedge", "orthogonality"]

    
def createNewComposite(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = Composite(self)
   ne = len(self.ASGroot.listNodes["Composite"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_Composite(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_Composite(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("Composite", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewBasic(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = Basic(self)
   ne = len(self.ASGroot.listNodes["Basic"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_Basic(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_Basic(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewHistory(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = History(self)
   ne = len(self.ASGroot.listNodes["History"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_History(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_History(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("History", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewOrthogonal(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = Orthogonal(self)
   ne = len(self.ASGroot.listNodes["Orthogonal"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_Orthogonal(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_Orthogonal(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("Orthogonal", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewvisual_settings(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = visual_settings(self)
   ne = len(self.ASGroot.listNodes["visual_settings"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_visual_settings(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_visual_settings(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("visual_settings", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewcontains(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = contains(self)
   ne = len(self.ASGroot.listNodes["contains"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_contains(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_contains(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("contains", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewHyperedge(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = Hyperedge(self)
   ne = len(self.ASGroot.listNodes["Hyperedge"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_Hyperedge(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_Hyperedge(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNeworthogonality(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = orthogonality(self)
   ne = len(self.ASGroot.listNodes["orthogonality"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_orthogonality(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_orthogonality(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("orthogonality", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNew_Model(self, wherex, wherey, screenCoordinates = 1):
   self.toClass = None
   self.fromClass = None
   new_semantic_obj = ASG_Statechart(self)
   ne = len(self.ASGroot.listNodes["ASG_Statechart"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_ASG_ERmetaMetaModel(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_ASG_ERmetaMetaModel(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("ASG_Statechart", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def fillTypesInformation(self):
    objs = []
    obj = ATOM3TypeInfo(self)
    params  = []
    obj.setValue(("String", "ATOM3String", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    param = ATOM3String("None")
    params.append(param)
    param = ATOM3String("None")
    params.append(param)
    param = ATOM3String("1")
    params.append(param)
    obj.setValue(("Boolean", "ATOM3Boolean", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    obj.setValue(("Integer", "ATOM3Integer", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    obj.setValue(("Float", "ATOM3Float", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    param = ATOM3String("self.types")
    params.append(param)
    obj.setValue(("Attribute", "ATOM3Attribute", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    param = ATOM3String("[1,1,1,self.types]")
    params.append(param)
    param = ATOM3String("ATOM3Attribute")
    params.append(param)
    param = ATOM3String("self.types")
    params.append(param)
    obj.setValue(("List", "ATOM3List", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    param = ATOM3String("[]")
    params.append(param)
    param = ATOM3String("1")
    params.append(param)
    param = ATOM3String("1")
    params.append(param)
    obj.setValue(("Enum", "ATOM3Enum", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    obj.setValue(("Constraint", "ATOM3Constraint", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    param = ATOM3String("'class0'")
    params.append(param)
    param = ATOM3String("None")
    params.append(param)
    obj.setValue(("Appearance", "ATOM3Appearance", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    obj.setValue(("BottomType", "ATOM3BottomType", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    obj.setValue(("Link", "ATOM3Link", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    obj.setValue(("Port", "ATOM3Port", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    obj.setValue(("Connection", "ATOM3Connection", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    param = ATOM3String("None")
    params.append(param)
    param = ATOM3String("None")
    params.append(param)
    param = ATOM3String("1")
    params.append(param)
    obj.setValue(("MSEnum", "ATOM3MSEnum", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    obj.setValue(("Text", "ATOM3Text", params, (None, 0) ))
    objs.append(obj)
    self.typeList.setValue(objs)

