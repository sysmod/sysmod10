from graph_ASG_ERmetaMetaModel import *
from stickylink import *
from widthXfillXdecoration import *
from ASG_DCharts import *
from Composite import *
from Basic import *
from History import *
from Orthogonal import *
from visual_settings import *
from contains import *
from Hyperedge import *
from orthogonality import *
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

def m4_DCharts_mdl(self, rootNode):

    self.globalPrecondition( rootNode )

    self.obj73=Composite(self)

    self.obj73.auto_adjust.setValue((None, 1))
    self.obj73.auto_adjust.config = 0
    self.obj73.name.setValue('AB')
    self.obj73.is_default.setValue((None, 1))
    self.obj73.is_default.config = 0
    self.obj73.visible.setValue((None, 1))
    self.obj73.visible.config = 0
    self.obj73.exit_action.setValue('\n\n\n')
    self.obj73.enter_action.setValue('\n\n\n')
    self.obj73.graphClass_= graph_Composite
    if self.genGraphics:
       from graph_Composite import *
       new_obj = graph_Composite(49.0,76.0,self.obj73)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Composite", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(113.0, 162.0, 113.0, 162.0))
       self.UMLmodel.coords(new_obj.connectors[1],(285.0, 162.0, 285.0, 162.0))
       self.UMLmodel.coords(new_obj.connectors[2],(198.99999999999997, 113.0, 198.99999999999997, 113.0))
       self.UMLmodel.coords(new_obj.connectors[3],(198.99999999999997, 212.0, 198.99999999999997, 212.0))
       self.UMLmodel.coords(new_obj.gf2.handler,113.0,113.0,285.0,212.0)
       self.UMLmodel.itemconfig(new_obj.gf2.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, outline='darkgreen')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,113.0,106.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='AB')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj73.graphObject_ = new_obj
    rootNode.addNode(self.obj73)
    self.globalAndLocalPostcondition(self.obj73, rootNode)

    self.globalPrecondition( rootNode )

    self.obj74=Basic(self)

    self.obj74.is_default.setValue((None, 1))
    self.obj74.is_default.config = 0
    self.obj74.name.setValue('A')
    self.obj74.exit_action.setValue('[DUMP("exiting state A")]\n\n')
    self.obj74.enter_action.setValue('[DUMP("entering state A")]\n\n')
    self.obj74.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(107.0,147.0,self.obj74)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(127.99999999999997, 150.0, 127.99999999999997, 150.0))
       self.UMLmodel.coords(new_obj.connectors[1],(127.99999999999997, 168.0, 127.99999999999997, 168.0))
       self.UMLmodel.coords(new_obj.connectors[2],(136.99999999999997, 159.0, 136.99999999999997, 159.0))
       self.UMLmodel.coords(new_obj.connectors[3],(120.0, 159.0, 120.0, 159.0))
       self.UMLmodel.coords(new_obj.gf3.handler,119.0,150.0,137.0,168.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,130.0,177.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='A')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj74.graphObject_ = new_obj
    rootNode.addNode(self.obj74)
    self.globalAndLocalPostcondition(self.obj74, rootNode)

    self.globalPrecondition( rootNode )

    self.obj75=Basic(self)

    self.obj75.is_default.setValue((None, 0))
    self.obj75.is_default.config = 0
    self.obj75.name.setValue('B')
    self.obj75.exit_action.setValue('\n\n')
    self.obj75.enter_action.setValue('\n\n')
    self.obj75.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(248.0,149.0,self.obj75)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(269.0, 152.0, 269.0, 152.0))
       self.UMLmodel.coords(new_obj.connectors[1],(269.0, 170.0, 269.0, 170.0))
       self.UMLmodel.coords(new_obj.connectors[2],(278.0, 161.0, 278.0, 161.0))
       self.UMLmodel.coords(new_obj.connectors[3],(261.0, 161.0, 261.0, 161.0))
       self.UMLmodel.coords(new_obj.gf3.handler,260.0,152.0,278.0,170.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,271.0,179.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='B')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj75.graphObject_ = new_obj
    rootNode.addNode(self.obj75)
    self.globalAndLocalPostcondition(self.obj75, rootNode)

    self.globalPrecondition( rootNode )

    self.obj76=Basic(self)

    self.obj76.is_default.setValue((None, 0))
    self.obj76.is_default.config = 0
    self.obj76.name.setValue('C')
    self.obj76.exit_action.setValue('[DUMP("exiting state C")]\n\n')
    self.obj76.enter_action.setValue('[DUMP("entering state C")]\n')
    self.obj76.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(353.0,150.0,self.obj76)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(373.99999999999994, 153.0, 373.99999999999994, 153.0))
       self.UMLmodel.coords(new_obj.connectors[1],(373.99999999999994, 171.0, 373.99999999999994, 171.0))
       self.UMLmodel.coords(new_obj.connectors[2],(383.0, 162.0, 383.0, 162.0))
       self.UMLmodel.coords(new_obj.connectors[3],(366.00000000000006, 162.0, 366.00000000000006, 162.0))
       self.UMLmodel.coords(new_obj.gf3.handler,365.0,153.0,383.0,171.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,376.0,180.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='C')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj76.graphObject_ = new_obj
    rootNode.addNode(self.obj76)
    self.globalAndLocalPostcondition(self.obj76, rootNode)

    self.globalPrecondition( rootNode )

    self.obj94=Basic(self)

    self.obj94.is_default.setValue((None, 1))
    self.obj94.is_default.config = 0
    self.obj94.name.setValue('X')
    self.obj94.exit_action.setValue('\n\n')
    self.obj94.enter_action.setValue('\n\n')
    self.obj94.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(434.0,98.0,self.obj94)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(455.0, 101.0, 455.0, 101.0))
       self.UMLmodel.coords(new_obj.connectors[1],(455.0, 119.0, 455.0, 119.0))
       self.UMLmodel.coords(new_obj.connectors[2],(464.0, 110.0, 464.0, 110.0))
       self.UMLmodel.coords(new_obj.connectors[3],(447.0, 110.0, 447.0, 110.0))
       self.UMLmodel.coords(new_obj.gf3.handler,446.0,101.0,464.0,119.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,457.0,128.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='X')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj94.graphObject_ = new_obj
    rootNode.addNode(self.obj94)
    self.globalAndLocalPostcondition(self.obj94, rootNode)

    self.globalPrecondition( rootNode )

    self.obj95=Basic(self)

    self.obj95.is_default.setValue((None, 0))
    self.obj95.is_default.config = 0
    self.obj95.name.setValue('Y')
    self.obj95.exit_action.setValue('\n\n')
    self.obj95.enter_action.setValue('\n\n')
    self.obj95.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(482.0,175.0,self.obj95)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(503.0, 177.99999999999997, 503.0, 177.99999999999997))
       self.UMLmodel.coords(new_obj.connectors[1],(503.0, 196.00000000000003, 503.0, 196.00000000000003))
       self.UMLmodel.coords(new_obj.connectors[2],(512.0, 186.99999999999997, 512.0, 186.99999999999997))
       self.UMLmodel.coords(new_obj.connectors[3],(495.0, 186.99999999999997, 495.0, 186.99999999999997))
       self.UMLmodel.coords(new_obj.gf3.handler,494.0,178.0,512.0,196.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,505.0,205.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Y')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj95.graphObject_ = new_obj
    rootNode.addNode(self.obj95)
    self.globalAndLocalPostcondition(self.obj95, rootNode)

    self.globalPrecondition( rootNode )

    self.obj82=Orthogonal(self)

    self.obj82.visible.setValue((None, 1))
    self.obj82.visible.config = 0
    self.obj82.name.setValue('O1')
    self.obj82.auto_adjust.setValue((None, 1))
    self.obj82.auto_adjust.config = 0
    self.obj82.graphClass_= graph_Orthogonal
    if self.genGraphics:
       from graph_Orthogonal import *
       new_obj = graph_Orthogonal(20.0,69.0,self.obj82)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Orthogonal", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(99.0, 156.0, 99.0, 156.0))
       self.UMLmodel.coords(new_obj.connectors[1],(390.00000000000006, 156.0, 390.00000000000006, 156.0))
       self.UMLmodel.coords(new_obj.connectors[2],(244.0, 94.0, 244.0, 94.0))
       self.UMLmodel.coords(new_obj.connectors[3],(244.0, 219.0, 244.0, 219.0))
       self.UMLmodel.coords(new_obj.gf5.handler,99.0,94.0,390.0,219.0)
       self.UMLmodel.itemconfig(new_obj.gf5.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, outline='darkgray')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,99.0,87.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='O1')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj82.graphObject_ = new_obj
    rootNode.addNode(self.obj82)
    self.globalAndLocalPostcondition(self.obj82, rootNode)

    self.globalPrecondition( rootNode )

    self.obj91=Orthogonal(self)

    self.obj91.visible.setValue((None, 1))
    self.obj91.visible.config = 0
    self.obj91.name.setValue('O2')
    self.obj91.auto_adjust.setValue((None, 1))
    self.obj91.auto_adjust.config = 0
    self.obj91.graphClass_= graph_Orthogonal
    if self.genGraphics:
       from graph_Orthogonal import *
       new_obj = graph_Orthogonal(324.0,64.0,self.obj91)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Orthogonal", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(426.0, 156.0, 426.0, 156.0))
       self.UMLmodel.coords(new_obj.connectors[1],(560.0, 156.0, 560.0, 156.0))
       self.UMLmodel.coords(new_obj.connectors[2],(493.0, 95.0, 493.0, 95.0))
       self.UMLmodel.coords(new_obj.connectors[3],(493.0, 217.0, 493.0, 217.0))
       self.UMLmodel.coords(new_obj.gf5.handler,426.0,95.0,560.0,217.0)
       self.UMLmodel.itemconfig(new_obj.gf5.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, outline='darkgray')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,426.0,88.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='O2')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj91.graphObject_ = new_obj
    rootNode.addNode(self.obj91)
    self.globalAndLocalPostcondition(self.obj91, rootNode)

    self.globalPrecondition( rootNode )

    self.obj77=contains(self)

    self.obj77.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(106.5,138.0,self.obj77)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj77.graphObject_ = new_obj
    rootNode.addNode(self.obj77)
    self.globalAndLocalPostcondition(self.obj77, rootNode)

    self.globalPrecondition( rootNode )

    self.obj78=contains(self)

    self.obj78.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(165.0,138.5,self.obj78)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj78.graphObject_ = new_obj
    rootNode.addNode(self.obj78)
    self.globalAndLocalPostcondition(self.obj78, rootNode)

    self.globalPrecondition( rootNode )

    self.obj85=contains(self)

    self.obj85.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(-3.5,106.5,self.obj85)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj85.graphObject_ = new_obj
    rootNode.addNode(self.obj85)
    self.globalAndLocalPostcondition(self.obj85, rootNode)

    self.globalPrecondition( rootNode )

    self.obj86=contains(self)

    self.obj86.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(157.0,135.0,self.obj86)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj86.graphObject_ = new_obj
    rootNode.addNode(self.obj86)
    self.globalAndLocalPostcondition(self.obj86, rootNode)

    self.globalPrecondition( rootNode )

    self.obj102=contains(self)

    self.obj102.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(269.5,87.5,self.obj102)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj102.graphObject_ = new_obj
    rootNode.addNode(self.obj102)
    self.globalAndLocalPostcondition(self.obj102, rootNode)

    self.globalPrecondition( rootNode )

    self.obj104=contains(self)

    self.obj104.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(293.5,126.0,self.obj104)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj104.graphObject_ = new_obj
    rootNode.addNode(self.obj104)
    self.globalAndLocalPostcondition(self.obj104, rootNode)

    self.globalPrecondition( rootNode )

    self.obj79=Hyperedge(self)

    self.obj79.name.setValue('')
    self.obj79.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj79.guard.setValue('1')
    self.obj79.trigger.setValue('e1')
    self.obj79.action.setValue('[DUMP("triggered by e1")]\n')
    self.obj79.broadcast_to.setValue('')
    self.obj79.display.setValue('e1')
    self.obj79.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(181.5,120.5,self.obj79)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj79.graphObject_ = new_obj
    rootNode.addNode(self.obj79)
    self.globalAndLocalPostcondition(self.obj79, rootNode)

    self.globalPrecondition( rootNode )

    self.obj80=Hyperedge(self)

    self.obj80.name.setValue('')
    self.obj80.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj80.guard.setValue('1')
    self.obj80.trigger.setValue('e2')
    self.obj80.action.setValue('[DUMP("triggered by e2")]\n')
    self.obj80.broadcast_to.setValue('')
    self.obj80.display.setValue('e2')
    self.obj80.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(188.5,192.5,self.obj80)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj80.graphObject_ = new_obj
    rootNode.addNode(self.obj80)
    self.globalAndLocalPostcondition(self.obj80, rootNode)

    self.globalPrecondition( rootNode )

    self.obj81=Hyperedge(self)

    self.obj81.name.setValue('')
    self.obj81.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj81.guard.setValue('1')
    self.obj81.trigger.setValue('e1')
    self.obj81.action.setValue('\n')
    self.obj81.broadcast_to.setValue('')
    self.obj81.display.setValue('e1')
    self.obj81.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(294.0,160.5,self.obj81)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj81.graphObject_ = new_obj
    rootNode.addNode(self.obj81)
    self.globalAndLocalPostcondition(self.obj81, rootNode)

    self.globalPrecondition( rootNode )

    self.obj100=Hyperedge(self)

    self.obj100.name.setValue('')
    self.obj100.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj100.guard.setValue('1')
    self.obj100.trigger.setValue('AFTER(1)')
    self.obj100.action.setValue('\n')
    self.obj100.broadcast_to.setValue('')
    self.obj100.display.setValue('tm(1)')
    self.obj100.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(526.0,131.5,self.obj100)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj100.graphObject_ = new_obj
    rootNode.addNode(self.obj100)
    self.globalAndLocalPostcondition(self.obj100, rootNode)

    self.globalPrecondition( rootNode )

    self.obj101=Hyperedge(self)

    self.obj101.name.setValue('')
    self.obj101.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj101.guard.setValue('1')
    self.obj101.trigger.setValue('AFTER(2)')
    self.obj101.action.setValue('\n')
    self.obj101.broadcast_to.setValue('')
    self.obj101.display.setValue('tm(2)')
    self.obj101.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(434.0,169.5,self.obj101)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj101.graphObject_ = new_obj
    rootNode.addNode(self.obj101)
    self.globalAndLocalPostcondition(self.obj101, rootNode)
    self.drawConnections((self.obj73,self.obj77,[113.0, 162.0, 106.5, 138.0], 0, 2), (self.obj73,self.obj78,[198.99999999999997, 113.0, 165.0, 138.5], 0, 2), (self.obj73,self.obj81,[285.0, 162.0, 294.0, 160.5], 0, 2), (self.obj74,self.obj79,[137.0, 159.0, 181.5, 120.5], 0, 2), (self.obj75,self.obj80,[261.0, 161.0, 188.5, 192.49999999999997], 0, 2), (self.obj94,self.obj100,[464.0, 110.00000000000001, 526.0, 131.5], 0, 2), (self.obj95,self.obj101,[495.0, 187.0, 434.00000000000006, 169.5], 0, 2), (self.obj82,self.obj85,[390.00000000000006, 156.0, -3.4999999999999996, 106.5], 0, 2), (self.obj82,self.obj86,[244.0, 94.0, 157.0, 135.0], 0, 2), (self.obj91,self.obj102,[560.0, 156.0, 269.5, 87.5], 0, 2), (self.obj91,self.obj104,[426.0, 156.0, 293.5, 125.99999999999999], 0, 2), (self.obj77,self.obj74,[106.5, 138.0, 128.0, 150.0], 0, 2), (self.obj78,self.obj75,[165.0, 138.5, 261.0, 161.0], 0, 2), (self.obj85,self.obj73,[-3.4999999999999996, 106.5, 113.0, 162.0], 0, 2), (self.obj86,self.obj76,[157.0, 135.0, 366.0, 162.0], 0, 2), (self.obj102,self.obj94,[269.5, 87.5, 446.99999999999994, 110.00000000000001], 0, 2), (self.obj104,self.obj95,[293.5, 125.99999999999999, 495.0, 187.0], 0, 2), (self.obj79,self.obj75,[181.5, 120.5, 261.0, 161.0], 0, 2), (self.obj80,self.obj74,[188.5, 192.49999999999997, 137.0, 159.0], 0, 2), (self.obj81,self.obj76,[294.0, 160.5, 366.0, 162.0], 0, 2), (self.obj100,self.obj95,[526.0, 131.5, 512.0, 187.0], 0, 2), (self.obj101,self.obj94,[434.00000000000006, 169.5, 446.99999999999994, 110.00000000000001], 0, 2) )

newfunction = m4_DCharts_mdl

loadedMMName = 'DCharts'
