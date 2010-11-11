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

def DCharts(self, rootNode):
    rootNode.RowSize.setValue(1)
    rootNode.Formalism_File.setValue('DCharts/DCharts_MM.py')
    rootNode.Formalism_Name.setValue('DCharts')

    self.globalPrecondition( rootNode )

    self.obj136=ButtonConfig(self)

    self.obj136.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewBasic (self, wherex, wherey)\n'))
    self.obj136.Drawing_Mode.setValue((' ', 1))
    self.obj136.Drawing_Mode.config = 0
    self.obj136.Contents.Text.setValue('New Basic')
    self.obj136.Contents.Image.setValue('DCharts/Basic.gif')
    self.obj136.Contents.lastSelected= "Image"
    self.obj136.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       from graph_ButtonConfig import *
       new_obj = graph_ButtonConfig(41.0,34.0,self.obj136)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
    else: new_obj = None
    self.obj136.graphObject_ = new_obj
    rootNode.addNode(self.obj136)
    self.globalAndLocalPostcondition(self.obj136, rootNode)

    self.globalPrecondition( rootNode )

    self.obj137=ButtonConfig(self)

    self.obj137.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewHistory (self, wherex, wherey)\n'))
    self.obj137.Drawing_Mode.setValue((' ', 1))
    self.obj137.Drawing_Mode.config = 0
    self.obj137.Contents.Text.setValue('New History')
    self.obj137.Contents.Image.setValue('DCharts/History.gif')
    self.obj137.Contents.lastSelected= "Image"
    self.obj137.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       from graph_ButtonConfig import *
       new_obj = graph_ButtonConfig(205.0,35.0,self.obj137)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
    else: new_obj = None
    self.obj137.graphObject_ = new_obj
    rootNode.addNode(self.obj137)
    self.globalAndLocalPostcondition(self.obj137, rootNode)

    self.globalPrecondition( rootNode )

    self.obj135=ButtonConfig(self)

    self.obj135.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewComposite (self, wherex, wherey)\n'))
    self.obj135.Drawing_Mode.setValue((' ', 1))
    self.obj135.Drawing_Mode.config = 0
    self.obj135.Contents.Text.setValue('New Composite')
    self.obj135.Contents.Image.setValue('DCharts/Composite.gif')
    self.obj135.Contents.lastSelected= "Image"
    self.obj135.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       from graph_ButtonConfig import *
       new_obj = graph_ButtonConfig(40.0,122.0,self.obj135)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
    else: new_obj = None
    self.obj135.graphObject_ = new_obj
    rootNode.addNode(self.obj135)
    self.globalAndLocalPostcondition(self.obj135, rootNode)

    self.globalPrecondition( rootNode )

    self.obj138=ButtonConfig(self)

    self.obj138.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewOrthogonal (self, wherex, wherey)\n'))
    self.obj138.Drawing_Mode.setValue((' ', 1))
    self.obj138.Drawing_Mode.config = 0
    self.obj138.Contents.Text.setValue('New Orthogonal')
    self.obj138.Contents.Image.setValue('DCharts/Orthogonal.gif')
    self.obj138.Contents.lastSelected= "Image"
    self.obj138.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       from graph_ButtonConfig import *
       new_obj = graph_ButtonConfig(204.0,119.0,self.obj138)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
    else: new_obj = None
    self.obj138.graphObject_ = new_obj
    rootNode.addNode(self.obj138)
    self.globalAndLocalPostcondition(self.obj138, rootNode)

    self.globalPrecondition( rootNode )

    self.obj140=ButtonConfig(self)

    self.obj140.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewPort (self, wherex, wherey)\n'))
    self.obj140.Drawing_Mode.setValue((' ', 1))
    self.obj140.Drawing_Mode.config = 0
    self.obj140.Contents.Text.setValue('New Port')
    self.obj140.Contents.Image.setValue('DCharts/Port.gif')
    self.obj140.Contents.lastSelected= "Image"
    self.obj140.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       from graph_ButtonConfig import *
       new_obj = graph_ButtonConfig(39.0,197.0,self.obj140)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
    else: new_obj = None
    self.obj140.graphObject_ = new_obj
    rootNode.addNode(self.obj140)
    self.globalAndLocalPostcondition(self.obj140, rootNode)

    self.globalPrecondition( rootNode )

    self.obj141=ButtonConfig(self)

    self.obj141.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewServer (self, wherex, wherey)\n'))
    self.obj141.Drawing_Mode.setValue((' ', 1))
    self.obj141.Drawing_Mode.config = 0
    self.obj141.Contents.Text.setValue('New Server')
    self.obj141.Contents.Image.setValue('DCharts/Server.gif')
    self.obj141.Contents.lastSelected= "Image"
    self.obj141.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       from graph_ButtonConfig import *
       new_obj = graph_ButtonConfig(204.0,197.0,self.obj141)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
    else: new_obj = None
    self.obj141.graphObject_ = new_obj
    rootNode.addNode(self.obj141)
    self.globalAndLocalPostcondition(self.obj141, rootNode)

    self.globalPrecondition( rootNode )

    self.obj139=ButtonConfig(self)

    self.obj139.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewvisual_settings (self, wherex, wherey)\n'))
    self.obj139.Drawing_Mode.setValue((' ', 1))
    self.obj139.Drawing_Mode.config = 0
    self.obj139.Contents.Text.setValue('New visual_settings')
    self.obj139.Contents.Image.setValue('DCharts/VisualSettings.gif')
    self.obj139.Contents.lastSelected= "Image"
    self.obj139.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       from graph_ButtonConfig import *
       new_obj = graph_ButtonConfig(38.0,332.0,self.obj139)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
    else: new_obj = None
    self.obj139.graphObject_ = new_obj
    rootNode.addNode(self.obj139)
    self.globalAndLocalPostcondition(self.obj139, rootNode)

    self.globalPrecondition( rootNode )

    self.obj142=ButtonConfig(self)

    self.obj142.Action.setValue(('Action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# The parameters of this method are:\n#   - wherex\n#   - wherey\n\nimport SVMAToM3Plugin\nSVMAToM3Plugin.simulate(self)\n'))
    self.obj142.Drawing_Mode.setValue((' ', 0))
    self.obj142.Drawing_Mode.config = 0
    self.obj142.Contents.Text.setValue('simulate in SVM')
    self.obj142.Contents.Image.setValue('')
    self.obj142.Contents.lastSelected= "Text"
    self.obj142.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       from graph_ButtonConfig import *
       new_obj = graph_ButtonConfig(38.0,265.0,self.obj142)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
    else: new_obj = None
    self.obj142.graphObject_ = new_obj
    rootNode.addNode(self.obj142)
    self.globalAndLocalPostcondition(self.obj142, rootNode)

    self.globalPrecondition( rootNode )

    self.obj143=ButtonConfig(self)

    self.obj143.Action.setValue(('Action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# The parameters of this method are:\n#   - wherex\n#   - wherey\n\nimport SVMAToM3Plugin\nSVMAToM3Plugin.generate_description(self)\n'))
    self.obj143.Drawing_Mode.setValue((' ', 0))
    self.obj143.Drawing_Mode.config = 0
    self.obj143.Contents.Text.setValue('generate .des')
    self.obj143.Contents.Image.setValue('')
    self.obj143.Contents.lastSelected= "Text"
    self.obj143.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       from graph_ButtonConfig import *
       new_obj = graph_ButtonConfig(204.0,266.0,self.obj143)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
    else: new_obj = None
    self.obj143.graphObject_ = new_obj
    rootNode.addNode(self.obj143)
    self.globalAndLocalPostcondition(self.obj143, rootNode)
    self.drawConnections( )

newfunction = DCharts

loadedMMName = 'Buttons'
