from graph_ASG_ERmetaMetaModel import *
from stickylink import *
from widthXfillXdecoration import *
from ASG_Buttons import *
from ASG_Buttons import *
from ButtonConfig import *
from ATOM3Enum import *
from ATOM3String import *
from ATOM3BottomType import *
from ATOM3Constraint import *
from ATOM3Attribute import *
from ATOM3Float import *
from ATOM3List import *
from ATOM3Link import *
from ATOM3Connection import *
from ATOM3Boolean import *
from ATOM3Appearance import *
from ATOM3Text import *
from ATOM3Integer import *
from ATOM3Port import *
from ATOM3MSEnum import *

def StatechartMDL_MM(self, rootNode):
    rootNode.RowSize.setValue(1)
    rootNode.Formalism_File.setValue('Statecharts/Statechart_MM.py')
    rootNode.Formalism_Name.setValue('Statechart')

    self.globalPrecondition( rootNode )

    self.obj29=ButtonConfig(self)

    self.obj29.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewComposite (self, wherex, wherey)\n'))
    self.obj29.Drawing_Mode.setValue((' ', 1))
    self.obj29.Drawing_Mode.config = 0
    self.obj29.Contents.Text.setValue('New Composite')
    self.obj29.Contents.Image.setValue('')
    self.obj29.Contents.lastSelected= "Text"
    self.obj29.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       from graph_ButtonConfig import *
       new_obj = graph_ButtonConfig(10,10,self.obj29)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
    else: new_obj = None
    self.obj29.graphObject_ = new_obj
    rootNode.addNode(self.obj29)
    self.globalAndLocalPostcondition(self.obj29, rootNode)

    self.globalPrecondition( rootNode )

    self.obj30=ButtonConfig(self)

    self.obj30.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewBasic (self, wherex, wherey)\n'))
    self.obj30.Drawing_Mode.setValue((' ', 1))
    self.obj30.Drawing_Mode.config = 0
    self.obj30.Contents.Text.setValue('New Basic')
    self.obj30.Contents.Image.setValue('')
    self.obj30.Contents.lastSelected= "Text"
    self.obj30.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       from graph_ButtonConfig import *
       new_obj = graph_ButtonConfig(135,10,self.obj30)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
    else: new_obj = None
    self.obj30.graphObject_ = new_obj
    rootNode.addNode(self.obj30)
    self.globalAndLocalPostcondition(self.obj30, rootNode)

    self.globalPrecondition( rootNode )

    self.obj31=ButtonConfig(self)

    self.obj31.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewHistory (self, wherex, wherey)\n'))
    self.obj31.Drawing_Mode.setValue((' ', 1))
    self.obj31.Drawing_Mode.config = 0
    self.obj31.Contents.Text.setValue('New History')
    self.obj31.Contents.Image.setValue('')
    self.obj31.Contents.lastSelected= "Text"
    self.obj31.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       from graph_ButtonConfig import *
       new_obj = graph_ButtonConfig(260,10,self.obj31)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
    else: new_obj = None
    self.obj31.graphObject_ = new_obj
    rootNode.addNode(self.obj31)
    self.globalAndLocalPostcondition(self.obj31, rootNode)

    self.globalPrecondition( rootNode )

    self.obj32=ButtonConfig(self)

    self.obj32.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewOrthogonal (self, wherex, wherey)\n'))
    self.obj32.Drawing_Mode.setValue((' ', 1))
    self.obj32.Drawing_Mode.config = 0
    self.obj32.Contents.Text.setValue('New Orthogonal')
    self.obj32.Contents.Image.setValue('')
    self.obj32.Contents.lastSelected= "Text"
    self.obj32.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       from graph_ButtonConfig import *
       new_obj = graph_ButtonConfig(10,80,self.obj32)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
    else: new_obj = None
    self.obj32.graphObject_ = new_obj
    rootNode.addNode(self.obj32)
    self.globalAndLocalPostcondition(self.obj32, rootNode)

    self.globalPrecondition( rootNode )

    self.obj33=ButtonConfig(self)

    self.obj33.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewvisual_settings (self, wherex, wherey)\n'))
    self.obj33.Drawing_Mode.setValue((' ', 1))
    self.obj33.Drawing_Mode.config = 0
    self.obj33.Contents.Text.setValue('New visual_settings')
    self.obj33.Contents.Image.setValue('')
    self.obj33.Contents.lastSelected= "Text"
    self.obj33.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       from graph_ButtonConfig import *
       new_obj = graph_ButtonConfig(135,80,self.obj33)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
    else: new_obj = None
    self.obj33.graphObject_ = new_obj
    rootNode.addNode(self.obj33)
    self.globalAndLocalPostcondition(self.obj33, rootNode)

    self.globalPrecondition( rootNode )

    self.obj34=ButtonConfig(self)

    self.obj34.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewHyperedge (self, wherex, wherey)\n'))
    self.obj34.Drawing_Mode.setValue((' ', 1))
    self.obj34.Drawing_Mode.config = 0
    self.obj34.Contents.Text.setValue('New Hyperedge')
    self.obj34.Contents.Image.setValue('')
    self.obj34.Contents.lastSelected= "Text"
    self.obj34.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       from graph_ButtonConfig import *
       new_obj = graph_ButtonConfig(10,150,self.obj34)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
    else: new_obj = None
    self.obj34.graphObject_ = new_obj
    rootNode.addNode(self.obj34)
    self.globalAndLocalPostcondition(self.obj34, rootNode)

    self.globalPrecondition( rootNode )

    self.obj35=ButtonConfig(self)

    self.obj35.Action.setValue(('Action', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# The parameters of this method are:\n#   - wherex\n#   - wherey\nimport statechart_utils\nstatechart_utils.gen_pythonDEVSRT(self)\n'))
    self.obj35.Drawing_Mode.setValue((' ', 0))
    self.obj35.Drawing_Mode.config = 0
    self.obj35.Contents.Text.setValue('pythonDEVS-RT')
    self.obj35.Contents.Image.setValue('')
    self.obj35.Contents.lastSelected= "Text"
    self.obj35.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       from graph_ButtonConfig import *
       new_obj = graph_ButtonConfig(137.0,151.0,self.obj35)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
    else: new_obj = None
    self.obj35.graphObject_ = new_obj
    rootNode.addNode(self.obj35)
    self.globalAndLocalPostcondition(self.obj35, rootNode)

    self.globalPrecondition( rootNode )

    self.obj36=ButtonConfig(self)

    self.obj36.Action.setValue(('Action', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# The parameters of this method are:\n#   - wherex\n#   - wherey\n\nimport SVMAToM3Plugin\nSVMAToM3Plugin.generate_description(self)\n'))
    self.obj36.Drawing_Mode.setValue((' ', 1))
    self.obj36.Drawing_Mode.config = 0
    self.obj36.Contents.Text.setValue('to SVM Des.')
    self.obj36.Contents.Image.setValue('')
    self.obj36.Contents.lastSelected= "Text"
    self.obj36.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       from graph_ButtonConfig import *
       new_obj = graph_ButtonConfig(264.0,155.0,self.obj36)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
    else: new_obj = None
    self.obj36.graphObject_ = new_obj
    rootNode.addNode(self.obj36)
    self.globalAndLocalPostcondition(self.obj36, rootNode)
    self.drawConnections( )

newfunction = StatechartMDL_MM

loadedMMName = 'Buttons'
