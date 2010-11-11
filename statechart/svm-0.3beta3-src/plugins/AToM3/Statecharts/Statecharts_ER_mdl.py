from graph_ASG_ERmetaMetaModel import *
from stickylink import *
from widthXfillXdecoration import *
from ASG_ERmetaMetaModel import *
from ERentity import *
from ERrelationship import *
from ASG_ERmetaMetaModel import *
from ATOM3BottomType import *
from ATOM3String import *
from ATOM3Constraint import *
from ATOM3Attribute import *
from ATOM3Enum import *
from ATOM3Appearance import *
from ATOM3Float import *
from ATOM3Connection import *
from ATOM3Boolean import *
from ATOM3Link import *
from ATOM3Text import *
from ATOM3Integer import *
from ATOM3List import *
from ATOM3Port import *
from ATOM3MSEnum import *

def Statecharts_ER_mdl(self, rootNode):
    rootNode.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj1 =[]
    rootNode.attributes.setValue(lcobj1)
    rootNode.name.setValue('Statechart')
    rootNode.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj1 =[]
    rootNode.constraints.setValue(lcobj1)
    rootNode.graphClass_= graph_ASG_ERmetaMetaModel

    self.globalPrecondition( rootNode )

    self.obj31=ERentity(self)

    self.obj31.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('Composite')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('is_default', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Boolean()
    cobj2.initialValue.setValue((None, 0))
    cobj2.initialValue.config = 1
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('visible', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Boolean()
    cobj2.initialValue.setValue((None, 1))
    cobj2.initialValue.config = 1
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('auto_adjust', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Boolean()
    cobj2.initialValue.setValue((None, 1))
    cobj2.initialValue.config = 1
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('enter_action', 'Text', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Text('', 60,15 )
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('exit_action', 'Text', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Text('', 60,15 )
    lcobj2.append(cobj2)
    self.obj31.attributes.setValue(lcobj2)
    self.obj31.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('contains', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Hyperedge', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Hyperedge', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('orthogonality', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('contains', (('Source', 'Destination'), 1), '0', '1'))
    lcobj2.append(cobj2)
    self.obj31.cardinality.setValue(lcobj2)
    self.obj31.appearance.setValue( ('Composite', self.obj31))
    self.obj31.name.setValue('Composite')
    self.obj31.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Constraint()
    cobj2.setValue(('Composite_CREATE', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), 'import statechart_utils\nstatechart_utils.Composite_CREATE(self)\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Constraint()
    cobj2.setValue(('Composite_DRAG', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]), 'import statechart_utils\nstatechart_utils.Composite_DRAG(self)\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Constraint()
    cobj2.setValue(('Composite_MOVE', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]), 'import statechart_utils\nstatechart_utils.Composite_MOVE(self)\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Constraint()
    cobj2.setValue(('Composite_DROP', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]), 'import statechart_utils\nstatechart_utils.Composite_DROP(self)\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Constraint()
    cobj2.setValue(('Composite_EDIT', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'import statechart_utils\nstatechart_utils.Composite_EDIT(self)\n'))
    lcobj2.append(cobj2)
    self.obj31.constraints.setValue(lcobj2)
    self.obj31.graphClass_= graph_ERentity
    if self.genGraphics:
       from graph_ERentity import *
       new_obj = graph_ERentity(66.0,147.0,self.obj31)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ERentity", new_obj.tag)
    else: new_obj = None
    self.obj31.graphObject_ = new_obj
    rootNode.addNode(self.obj31)
    self.globalAndLocalPostcondition(self.obj31, rootNode)

    self.globalPrecondition( rootNode )

    self.obj32=ERentity(self)

    self.obj32.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('Basic')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('is_default', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Boolean()
    cobj2.initialValue.setValue((None, 0))
    cobj2.initialValue.config = 1
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('enter_action', 'Text', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Text('\n', 60,15 )
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('exit_action', 'Text', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Text('\n', 60,15 )
    lcobj2.append(cobj2)
    self.obj32.attributes.setValue(lcobj2)
    self.obj32.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('contains', (('Source', 'Destination'), 1), '0', '1'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Hyperedge', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Hyperedge', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj32.cardinality.setValue(lcobj2)
    self.obj32.appearance.setValue( ('Basic', self.obj32))
    self.obj32.name.setValue('Basic')
    self.obj32.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Constraint()
    cobj2.setValue(('Basic_CREATE', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), 'import statechart_utils\nstatechart_utils.Basic_CREATE(self)\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Constraint()
    cobj2.setValue(('Basic_DRAG', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]), 'import statechart_utils\nstatechart_utils.Basic_DRAG(self)\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Constraint()
    cobj2.setValue(('Basic_DROP', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]), 'import statechart_utils\nstatechart_utils.Basic_DROP(self)\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Constraint()
    cobj2.setValue(('Basic_MOVE', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]), 'import statechart_utils\nstatechart_utils.Basic_MOVE(self)\n'))
    lcobj2.append(cobj2)
    self.obj32.constraints.setValue(lcobj2)
    self.obj32.graphClass_= graph_ERentity
    if self.genGraphics:
       from graph_ERentity import *
       new_obj = graph_ERentity(453.0,173.0,self.obj32)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ERentity", new_obj.tag)
    else: new_obj = None
    self.obj32.graphObject_ = new_obj
    rootNode.addNode(self.obj32)
    self.globalAndLocalPostcondition(self.obj32, rootNode)

    self.globalPrecondition( rootNode )

    self.obj33=ERentity(self)

    self.obj33.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('is_default', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Boolean()
    cobj2.initialValue.setValue((None, 0))
    cobj2.initialValue.config = 1
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('star', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Boolean()
    cobj2.initialValue.setValue((None, 0))
    cobj2.initialValue.config = 1
    lcobj2.append(cobj2)
    self.obj33.attributes.setValue(lcobj2)
    self.obj33.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('contains', (('Source', 'Destination'), 1), '0', '1'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Hyperedge', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Hyperedge', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj33.cardinality.setValue(lcobj2)
    self.obj33.appearance.setValue( ('History', self.obj33))
    self.obj33.name.setValue('History')
    self.obj33.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Constraint()
    cobj2.setValue(('History_CREATE', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), 'import statechart_utils\nstatechart_utils.History_CREATE(self)\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Constraint()
    cobj2.setValue(('History_DRAG', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]), 'import statechart_utils\nstatechart_utils.History_DRAG(self)\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Constraint()
    cobj2.setValue(('History_DROP', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]), 'import statechart_utils\nstatechart_utils.History_DROP(self)\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Constraint()
    cobj2.setValue(('History_MOVE', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]), 'import statechart_utils\nstatechart_utils.History_MOVE(self)\n'))
    lcobj2.append(cobj2)
    self.obj33.constraints.setValue(lcobj2)
    self.obj33.graphClass_= graph_ERentity
    if self.genGraphics:
       from graph_ERentity import *
       new_obj = graph_ERentity(453.0,269.0,self.obj33)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ERentity", new_obj.tag)
    else: new_obj = None
    self.obj33.graphObject_ = new_obj
    rootNode.addNode(self.obj33)
    self.globalAndLocalPostcondition(self.obj33, rootNode)

    self.globalPrecondition( rootNode )

    self.obj34=ERentity(self)

    self.obj34.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('Orthogonal')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('visible', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Boolean()
    cobj2.initialValue.setValue((None, 1))
    cobj2.initialValue.config = 1
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('auto_adjust', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Boolean()
    cobj2.initialValue.setValue((None, 1))
    cobj2.initialValue.config = 1
    lcobj2.append(cobj2)
    self.obj34.attributes.setValue(lcobj2)
    self.obj34.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('orthogonality', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('contains', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj34.cardinality.setValue(lcobj2)
    self.obj34.appearance.setValue( ('Orthogonal', self.obj34))
    self.obj34.name.setValue('Orthogonal')
    self.obj34.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Constraint()
    cobj2.setValue(('Orthogonal_CREATE', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), 'import statechart_utils\nstatechart_utils.Orthogonal_CREATE(self)\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Constraint()
    cobj2.setValue(('Orthogonal_DRAG', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]), 'import statechart_utils\nstatechart_utils.Orthogonal_DRAG(self)\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Constraint()
    cobj2.setValue(('Orthogonal_MOVE', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]), 'import statechart_utils\nstatechart_utils.Orthogonal_MOVE(self)\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Constraint()
    cobj2.setValue(('Orthogonal_DROP', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]), 'import statechart_utils\nstatechart_utils.Orthogonal_DROP(self)\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Constraint()
    cobj2.setValue(('Orthogonal_EDIT', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'import statechart_utils\nstatechart_utils.Orthogonal_EDIT(self)\n'))
    lcobj2.append(cobj2)
    self.obj34.constraints.setValue(lcobj2)
    self.obj34.graphClass_= graph_ERentity
    if self.genGraphics:
       from graph_ERentity import *
       new_obj = graph_ERentity(453.0,384.0,self.obj34)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ERentity", new_obj.tag)
    else: new_obj = None
    self.obj34.graphObject_ = new_obj
    rootNode.addNode(self.obj34)
    self.globalAndLocalPostcondition(self.obj34, rootNode)

    self.globalPrecondition( rootNode )

    self.obj35=ERentity(self)

    self.obj35.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('contains_links_visible', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Boolean()
    cobj2.initialValue.setValue((None, 0))
    cobj2.initialValue.config = 1
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('Composite_default_height', 'Float', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Float(50.0)
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('Composite_default_width', 'Float', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Float(50.0)
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('contains_color', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('pink')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('orthogonality_links_visible', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Boolean()
    cobj2.initialValue.setValue((None, 0))
    cobj2.initialValue.config = 1
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('orthogonality_color', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('lightblue')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('Hyperedge_links_visible', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Boolean()
    cobj2.initialValue.setValue((None, 1))
    cobj2.initialValue.config = 1
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('Hyperedge_color', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('darkblue')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('Composite_color', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('darkblue')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('Orthogonal_color', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('darkgray')
    lcobj2.append(cobj2)
    self.obj35.attributes.setValue(lcobj2)
    self.obj35.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj35.cardinality.setValue(lcobj2)
    self.obj35.appearance.setValue( ('visual_settings', self.obj35))
    self.obj35.name.setValue('visual_settings')
    self.obj35.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Constraint()
    cobj2.setValue(('apply_settings', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), 'import statechart_utils\nstatechart_utils.visual_settings_EDIT_CREATE(self)\n'))
    lcobj2.append(cobj2)
    self.obj35.constraints.setValue(lcobj2)
    self.obj35.graphClass_= graph_ERentity
    if self.genGraphics:
       from graph_ERentity import *
       new_obj = graph_ERentity(546.0,32.0,self.obj35)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ERentity", new_obj.tag)
    else: new_obj = None
    self.obj35.graphObject_ = new_obj
    rootNode.addNode(self.obj35)
    self.globalAndLocalPostcondition(self.obj35, rootNode)

    self.globalPrecondition( rootNode )

    self.obj36=ERrelationship(self)

    self.obj36.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj36.attributes.setValue(lcobj2)
    self.obj36.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Composite', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Basic', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('History', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Orthogonal', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Composite', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj36.cardinality.setValue(lcobj2)
    self.obj36.appearance.setValue( ('contains', self.obj36))
    self.obj36.appearance.linkInfo=linkEditor(self,self.obj36.appearance.semObject, "contains")
    self.obj36.appearance.linkInfo.FirstLink= stickylink()
    self.obj36.appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj36.appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj36.appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj36.appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(0)
    self.obj36.appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(0)
    self.obj36.appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(0)
    self.obj36.appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj36.appearance.linkInfo.FirstLink.decoration.setValue( ('contains_1stLink', self.obj36.appearance.linkInfo.FirstLink))
    self.obj36.appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj36.appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj36.appearance.linkInfo.FirstSegment.fill=ATOM3String('orange')
    self.obj36.appearance.linkInfo.FirstSegment.stipple=ATOM3String('')
    self.obj36.appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj36.appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj36.appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj36.appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(0)
    self.obj36.appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(0)
    self.obj36.appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(0)
    self.obj36.appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj36.appearance.linkInfo.FirstSegment.decoration.setValue( ('contains_1stSegment', self.obj36.appearance.linkInfo.FirstSegment))
    self.obj36.appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj36.appearance.linkInfo.Center=ATOM3Appearance()
    self.obj36.appearance.linkInfo.Center.setValue( ('contains_Center', self.obj36.appearance.linkInfo))
    self.obj36.appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj36.appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj36.appearance.linkInfo.SecondSegment.fill=ATOM3String('orange')
    self.obj36.appearance.linkInfo.SecondSegment.stipple=ATOM3String('')
    self.obj36.appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj36.appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj36.appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj36.appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(0)
    self.obj36.appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(0)
    self.obj36.appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(0)
    self.obj36.appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj36.appearance.linkInfo.SecondSegment.decoration.setValue( ('contains_2ndSegment', self.obj36.appearance.linkInfo.SecondSegment))
    self.obj36.appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj36.appearance.linkInfo.SecondLink= stickylink()
    self.obj36.appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj36.appearance.linkInfo.SecondLink.arrow.setValue((' ', 0))
    self.obj36.appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj36.appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(0)
    self.obj36.appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(0)
    self.obj36.appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(0)
    self.obj36.appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj36.appearance.linkInfo.SecondLink.decoration.setValue( ('contains_2ndLink', self.obj36.appearance.linkInfo.SecondLink))
    self.obj36.appearance.linkInfo.FirstLink.decoration.semObject=self.obj36.appearance.semObject
    self.obj36.appearance.linkInfo.FirstSegment.decoration.semObject=self.obj36.appearance.semObject
    self.obj36.appearance.linkInfo.Center.semObject=self.obj36.appearance.semObject
    self.obj36.appearance.linkInfo.SecondSegment.decoration.semObject=self.obj36.appearance.semObject
    self.obj36.appearance.linkInfo.SecondLink.decoration.semObject=self.obj36.appearance.semObject
    self.obj36.name.setValue('contains')
    self.obj36.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Constraint()
    cobj2.setValue(('contains_CREATE', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), 'import statechart_utils\nstatechart_utils.contains_CREATE(self)\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Constraint()
    cobj2.setValue(('contains_CONNECT', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]), 'import statechart_utils\nstatechart_utils.contains_CONNECT(self)\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Constraint()
    cobj2.setValue(('contains_DELETE', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0]), 'import statechart_utils\nstatechart_utils.contains_DELETE(self)\n\n'))
    lcobj2.append(cobj2)
    self.obj36.constraints.setValue(lcobj2)
    self.obj36.graphClass_= graph_ERrelationship
    if self.genGraphics:
       from graph_ERrelationship import *
       new_obj = graph_ERrelationship(284.0,219.0,self.obj36)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ERrelationship", new_obj.tag)
    else: new_obj = None
    self.obj36.graphObject_ = new_obj
    rootNode.addNode(self.obj36)
    self.globalAndLocalPostcondition(self.obj36, rootNode)

    self.globalPrecondition( rootNode )

    self.obj37=ERrelationship(self)

    self.obj37.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('trigger', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('guard', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('action', 'Text', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Text('', 60,15 )
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('broadcast', 'Text', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Text('# return an instance of DEVSevent or None\nreturn None\n', 60,15 )
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('broadcast_to', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('display', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('')
    lcobj2.append(cobj2)
    self.obj37.attributes.setValue(lcobj2)
    self.obj37.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Composite', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Composite', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Basic', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('History', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Basic', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('History', (('Source', 'Destination'), 0), '0', '1'))
    lcobj2.append(cobj2)
    self.obj37.cardinality.setValue(lcobj2)
    self.obj37.appearance.setValue( ('Hyperedge', self.obj37))
    self.obj37.appearance.linkInfo=linkEditor(self,self.obj37.appearance.semObject, "Hyperedge")
    self.obj37.appearance.linkInfo.FirstLink= stickylink()
    self.obj37.appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj37.appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj37.appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj37.appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(3)
    self.obj37.appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(6)
    self.obj37.appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj37.appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj37.appearance.linkInfo.FirstLink.decoration.setValue( ('Hyperedge_1stLink', self.obj37.appearance.linkInfo.FirstLink))
    self.obj37.appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj37.appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj37.appearance.linkInfo.FirstSegment.fill=ATOM3String('black')
    self.obj37.appearance.linkInfo.FirstSegment.stipple=ATOM3String('')
    self.obj37.appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj37.appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj37.appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj37.appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(0)
    self.obj37.appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(0)
    self.obj37.appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(0)
    self.obj37.appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj37.appearance.linkInfo.FirstSegment.decoration.setValue( ('Hyperedge_1stSegment', self.obj37.appearance.linkInfo.FirstSegment))
    self.obj37.appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj37.appearance.linkInfo.Center=ATOM3Appearance()
    self.obj37.appearance.linkInfo.Center.setValue( ('Hyperedge_Center', self.obj37.appearance.linkInfo))
    self.obj37.appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj37.appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj37.appearance.linkInfo.SecondSegment.fill=ATOM3String('black')
    self.obj37.appearance.linkInfo.SecondSegment.stipple=ATOM3String('')
    self.obj37.appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj37.appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj37.appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj37.appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(0)
    self.obj37.appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(0)
    self.obj37.appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(0)
    self.obj37.appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj37.appearance.linkInfo.SecondSegment.decoration.setValue( ('Hyperedge_2ndSegment', self.obj37.appearance.linkInfo.SecondSegment))
    self.obj37.appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj37.appearance.linkInfo.SecondLink= stickylink()
    self.obj37.appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj37.appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj37.appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj37.appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(6)
    self.obj37.appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(9)
    self.obj37.appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(6)
    self.obj37.appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj37.appearance.linkInfo.SecondLink.decoration.setValue( ('Hyperedge_2ndLink', self.obj37.appearance.linkInfo.SecondLink))
    self.obj37.appearance.linkInfo.FirstLink.decoration.semObject=self.obj37.appearance.semObject
    self.obj37.appearance.linkInfo.FirstSegment.decoration.semObject=self.obj37.appearance.semObject
    self.obj37.appearance.linkInfo.Center.semObject=self.obj37.appearance.semObject
    self.obj37.appearance.linkInfo.SecondSegment.decoration.semObject=self.obj37.appearance.semObject
    self.obj37.appearance.linkInfo.SecondLink.decoration.semObject=self.obj37.appearance.semObject
    self.obj37.name.setValue('Hyperedge')
    self.obj37.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Constraint()
    cobj2.setValue(('Hyperedge_CREATE', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), 'import statechart_utils\nstatechart_utils.Hyperedge_CREATE(self)\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Constraint()
    cobj2.setValue(('Hyperedge_CONNECT', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]), 'import statechart_utils\nstatechart_utils.Hyperedge_CONNECT(self)\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Constraint()
    cobj2.setValue(('Hyperedge_DELETE', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]), 'import statechart_utils\nstatechart_utils.Hyperedge_DELETE(self)\n\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Constraint()
    cobj2.setValue(('Hyperedge_DROP', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]), 'import statechart_utils\nstatechart_utils.Hyperedge_DROP(self)\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Constraint()
    cobj2.setValue(('Hyperedge_MOVE', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]), 'import statechart_utils\nstatechart_utils.Hyperedge_MOVE(self)\n'))
    lcobj2.append(cobj2)
    self.obj37.constraints.setValue(lcobj2)
    self.obj37.graphClass_= graph_ERrelationship
    if self.genGraphics:
       from graph_ERrelationship import *
       new_obj = graph_ERrelationship(90.0,311.0,self.obj37)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ERrelationship", new_obj.tag)
    else: new_obj = None
    self.obj37.graphObject_ = new_obj
    rootNode.addNode(self.obj37)
    self.globalAndLocalPostcondition(self.obj37, rootNode)

    self.globalPrecondition( rootNode )

    self.obj38=ERrelationship(self)

    self.obj38.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj38.attributes.setValue(lcobj2)
    self.obj38.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Composite', (('Source', 'Destination'), 1), '1', '1'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Orthogonal', (('Source', 'Destination'), 0), '1', '1'))
    lcobj2.append(cobj2)
    self.obj38.cardinality.setValue(lcobj2)
    self.obj38.appearance.setValue( ('orthogonality', self.obj38))
    self.obj38.appearance.linkInfo=linkEditor(self,self.obj38.appearance.semObject, "orthogonality")
    self.obj38.appearance.linkInfo.FirstLink= stickylink()
    self.obj38.appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj38.appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj38.appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj38.appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(0)
    self.obj38.appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(0)
    self.obj38.appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(0)
    self.obj38.appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj38.appearance.linkInfo.FirstLink.decoration.setValue( ('orthogonality_1stLink', self.obj38.appearance.linkInfo.FirstLink))
    self.obj38.appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj38.appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj38.appearance.linkInfo.FirstSegment.fill=ATOM3String('red')
    self.obj38.appearance.linkInfo.FirstSegment.stipple=ATOM3String('')
    self.obj38.appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj38.appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj38.appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj38.appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(0)
    self.obj38.appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(0)
    self.obj38.appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(0)
    self.obj38.appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj38.appearance.linkInfo.FirstSegment.decoration.setValue( ('orthogonality_1stSegment', self.obj38.appearance.linkInfo.FirstSegment))
    self.obj38.appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj38.appearance.linkInfo.Center=ATOM3Appearance()
    self.obj38.appearance.linkInfo.Center.setValue( ('orthogonality_Center', self.obj38.appearance.linkInfo))
    self.obj38.appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj38.appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj38.appearance.linkInfo.SecondSegment.fill=ATOM3String('red')
    self.obj38.appearance.linkInfo.SecondSegment.stipple=ATOM3String('')
    self.obj38.appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj38.appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj38.appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj38.appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(0)
    self.obj38.appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(0)
    self.obj38.appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(0)
    self.obj38.appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj38.appearance.linkInfo.SecondSegment.decoration.setValue( ('orthogonality_2ndSegment', self.obj38.appearance.linkInfo.SecondSegment))
    self.obj38.appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj38.appearance.linkInfo.SecondLink= stickylink()
    self.obj38.appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj38.appearance.linkInfo.SecondLink.arrow.setValue((' ', 0))
    self.obj38.appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj38.appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(0)
    self.obj38.appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(0)
    self.obj38.appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(0)
    self.obj38.appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj38.appearance.linkInfo.SecondLink.decoration.setValue( ('orthogonality_2ndLink', self.obj38.appearance.linkInfo.SecondLink))
    self.obj38.appearance.linkInfo.FirstLink.decoration.semObject=self.obj38.appearance.semObject
    self.obj38.appearance.linkInfo.FirstSegment.decoration.semObject=self.obj38.appearance.semObject
    self.obj38.appearance.linkInfo.Center.semObject=self.obj38.appearance.semObject
    self.obj38.appearance.linkInfo.SecondSegment.decoration.semObject=self.obj38.appearance.semObject
    self.obj38.appearance.linkInfo.SecondLink.decoration.semObject=self.obj38.appearance.semObject
    self.obj38.name.setValue('orthogonality')
    self.obj38.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Constraint()
    cobj2.setValue(('orthogonality_CREATE', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), 'import statechart_utils\nstatechart_utils.orthogonality_CREATE(self)\n\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Constraint()
    cobj2.setValue(('orthogonality_CONNECT', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]), 'import statechart_utils\nstatechart_utils.orthogonality_CONNECT(self)\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Constraint()
    cobj2.setValue(('orthogonality_DELETE', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0]), 'import statechart_utils\nstatechart_utils.orthogonality_DELETE(self)\n'))
    lcobj2.append(cobj2)
    self.obj38.constraints.setValue(lcobj2)
    self.obj38.graphClass_= graph_ERrelationship
    if self.genGraphics:
       from graph_ERrelationship import *
       new_obj = graph_ERrelationship(239.0,381.0,self.obj38)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ERrelationship", new_obj.tag)
    else: new_obj = None
    self.obj38.graphObject_ = new_obj
    rootNode.addNode(self.obj38)
    self.globalAndLocalPostcondition(self.obj38, rootNode)
    self.drawConnections((self.obj31,self.obj36,[216.0, 173.0, 263.0, 173.0, 264.0, 268.0, 287.0, 267.0], 0, 4), (self.obj31,self.obj37,[188.0, 242.0, 189.0, 360.0, 183.0, 359.0], 0, 3), (self.obj31,self.obj38,[216.0, 220.0, 231.0, 220.0, 231.0, 429.0, 242.0, 429.0], 0, 4), (self.obj32,self.obj37,[603.0, 222.0, 654.0, 223.0, 654.0, 495.0, 137.0, 495.0, 136.0, 399.0], 0, 5), (self.obj33,self.obj37,[603.0, 318.0, 639.0, 319.0, 638.0, 486.0, 149.0, 485.0, 136.0, 399.0], 0, 5), (self.obj34,self.obj36,[456.0, 410.0, 330.0, 410.0, 330.0, 307.0], 0, 3), (self.obj36,self.obj32,[377.0, 267.0, 397.0, 266.0, 398.0, 217.0, 456.0, 218.0], 0, 4), (self.obj36,self.obj33,[377.0, 267.0, 398.0, 267.0, 397.0, 315.0, 456.0, 314.0], 0, 4), (self.obj36,self.obj31,[332.0, 222.0, 333.0, 78.0, 138.0, 78.0, 138.0, 150.0], 0, 4), (self.obj37,self.obj31,[93.0, 359.0, 89.0, 359.0, 90.0, 241.0], 0, 3), (self.obj37,self.obj32,[93.0, 359.0, 36.0, 358.0, 37.0, 46.0, 436.0, 46.0, 436.0, 245.0, 456.0, 245.0], 0, 6), (self.obj37,self.obj33,[93.0, 359.0, 50.0, 348.0, 50.0, 54.0, 412.0, 55.0, 411.0, 341.0, 456.0, 341.0], 0, 6), (self.obj38,self.obj34,[332.0, 429.0, 456.0, 429.0], 0, 2) )

newfunction = Statecharts_ER_mdl

loadedMMName = 'EntityRelationship'
