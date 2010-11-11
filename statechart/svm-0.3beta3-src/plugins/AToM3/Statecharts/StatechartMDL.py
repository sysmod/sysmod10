from ASG_Buttons import *
from ButtonConfig import *
from ATOM3Enum import *
from ATOM3List import *
from ATOM3Float import *
from ATOM3Integer import *
from ATOM3Attribute import *
from ATOM3Constraint import *
from ATOM3String import *
from ATOM3BottomType import *
from ATOM3Boolean import *
from ATOM3Appearance import *
from ATOM3Link import *
def StatechartMDL(self, rootNode):
   rootNode.Formalism_Name.setValue('StatechartMDL')
   rootNode.RowSize.setValue(1)
   rootNode.Formalism_File.setValue('Statecharts/StatechartMDL_MM.py')
   self.globalPrecondition(rootNode)

   self.objStatechart=ButtonConfig(self)
   self.objStatechart.Contents.Text.setValue('New Statechart')
   self.objStatechart.Contents.Image.setValue('')
   self.objStatechart.Contents.lastSelected= 'Text'
   self.objStatechart.Drawing_Mode.setValue(1)
   self.objStatechart.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewStatechart (self, wherex, wherey)\n'))
   self.objStatechart.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objStatechart)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objStatechart.graphObject_ = new_obj
   rootNode.addNode(self.objStatechart)
   self.globalAndLocalPostcondition(self.objStatechart, rootNode)
   self.globalPrecondition(rootNode)

   self.objBasic=ButtonConfig(self)
   self.objBasic.Contents.Text.setValue('New Basic')
   self.objBasic.Contents.Image.setValue('')
   self.objBasic.Contents.lastSelected= 'Text'
   self.objBasic.Drawing_Mode.setValue(1)
   self.objBasic.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewBasic (self, wherex, wherey)\n'))
   self.objBasic.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 10,self.objBasic)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objBasic.graphObject_ = new_obj
   rootNode.addNode(self.objBasic)
   self.globalAndLocalPostcondition(self.objBasic, rootNode)
   self.globalPrecondition(rootNode)

   self.objHistory=ButtonConfig(self)
   self.objHistory.Contents.Text.setValue('New History')
   self.objHistory.Contents.Image.setValue('')
   self.objHistory.Contents.lastSelected= 'Text'
   self.objHistory.Drawing_Mode.setValue(1)
   self.objHistory.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewHistory (self, wherex, wherey)\n'))
   self.objHistory.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 10,self.objHistory)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objHistory.graphObject_ = new_obj
   rootNode.addNode(self.objHistory)
   self.globalAndLocalPostcondition(self.objHistory, rootNode)
   self.globalPrecondition(rootNode)

   self.objConditional=ButtonConfig(self)
   self.objConditional.Contents.Text.setValue('New Conditional')
   self.objConditional.Contents.Image.setValue('')
   self.objConditional.Contents.lastSelected= 'Text'
   self.objConditional.Drawing_Mode.setValue(1)
   self.objConditional.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewConditional (self, wherex, wherey)\n'))
   self.objConditional.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 80,self.objConditional)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objConditional.graphObject_ = new_obj
   rootNode.addNode(self.objConditional)
   self.globalAndLocalPostcondition(self.objConditional, rootNode)
   self.globalPrecondition(rootNode)

   self.objcontains=ButtonConfig(self)
   self.objcontains.Contents.Text.setValue('New contains')
   self.objcontains.Contents.Image.setValue('')
   self.objcontains.Contents.lastSelected= 'Text'
   self.objcontains.Drawing_Mode.setValue(1)
   self.objcontains.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewcontains (self, wherex, wherey)\n'))
   self.objcontains.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objcontains)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objcontains.graphObject_ = new_obj
   rootNode.addNode(self.objcontains)
   self.globalAndLocalPostcondition(self.objcontains, rootNode)
   self.globalPrecondition(rootNode)

   self.objHyperedge=ButtonConfig(self)
   self.objHyperedge.Contents.Text.setValue('New Hyperedge')
   self.objHyperedge.Contents.Image.setValue('')
   self.objHyperedge.Contents.lastSelected= 'Text'
   self.objHyperedge.Drawing_Mode.setValue(1)
   self.objHyperedge.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewHyperedge (self, wherex, wherey)\n'))
   self.objHyperedge.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 80,self.objHyperedge)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objHyperedge.graphObject_ = new_obj
   rootNode.addNode(self.objHyperedge)
   self.globalAndLocalPostcondition(self.objHyperedge, rootNode)
newfunction = StatechartMDL
loadedMMName = 'Buttons'
