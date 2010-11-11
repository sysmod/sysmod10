from graph_ASG_ERmetaMetaModel import *
from stickylink import *
from widthXfillXdecoration import *
from ASG_DCharts import *
from ASG_DCharts import *
from Composite import *
from Basic import *
from History import *
from Orthogonal import *
from visual_settings import *
from Port import *
from Server import *
from contains import *
from Hyperedge import *
from orthogonality import *
from connection import *
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

def m9_Statecharts_mdl(self, rootNode):

    self.globalPrecondition( rootNode )

    self.obj355=Composite(self)

    self.obj355.auto_adjust.setValue((None, 1))
    self.obj355.auto_adjust.config = 0
    self.obj355.name.setValue('AB')
    self.obj355.is_default.setValue((None, 1))
    self.obj355.is_default.config = 0
    self.obj355.visible.setValue((None, 1))
    self.obj355.visible.config = 0
    self.obj355.exit_action.setValue('\n\n\n')
    self.obj355.enter_action.setValue('\n\n\n')
    self.obj355.graphClass_= graph_Composite
    if self.genGraphics:
       from graph_Composite import *
       new_obj = graph_Composite(49.0,76.0,self.obj355)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Composite", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(112.99999999999999, 191.0, 112.99999999999999, 191.0))
       self.UMLmodel.coords(new_obj.connectors[1],(285.0, 191.0, 285.0, 191.0))
       self.UMLmodel.coords(new_obj.connectors[2],(199.0, 111.99999999999999, 199.0, 111.99999999999999))
       self.UMLmodel.coords(new_obj.connectors[3],(199.0, 270.0, 199.0, 270.0))
       self.UMLmodel.coords(new_obj.gf2.handler,113.0,112.0,285.0,270.0)
       self.UMLmodel.itemconfig(new_obj.gf2.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,113.0,105.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='AB')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj355.graphObject_ = new_obj
    rootNode.addNode(self.obj355)
    self.globalAndLocalPostcondition(self.obj355, rootNode)

    self.globalPrecondition( rootNode )

    self.obj356=Composite(self)

    self.obj356.auto_adjust.setValue((None, 1))
    self.obj356.auto_adjust.config = 0
    self.obj356.name.setValue('active')
    self.obj356.is_default.setValue((None, 1))
    self.obj356.is_default.config = 0
    self.obj356.visible.setValue((None, 1))
    self.obj356.visible.config = 0
    self.obj356.exit_action.setValue('\n\n')
    self.obj356.enter_action.setValue('\n\n')
    self.obj356.graphClass_= graph_Composite
    if self.genGraphics:
       from graph_Composite import *
       new_obj = graph_Composite(40.0,38.0,self.obj356)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Composite", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(85.0, 170.0, 85.0, 170.0))
       self.UMLmodel.coords(new_obj.connectors[1],(766.0, 170.0, 766.0, 170.0))
       self.UMLmodel.coords(new_obj.connectors[2],(425.0, 56.999999999999993, 425.0, 56.999999999999993))
       self.UMLmodel.coords(new_obj.connectors[3],(425.0, 284.0, 425.0, 284.0))
       self.UMLmodel.coords(new_obj.gf2.handler,85.0,57.0,766.0,284.0)
       self.UMLmodel.itemconfig(new_obj.gf2.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,85.0,50.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='active')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj356.graphObject_ = new_obj
    rootNode.addNode(self.obj356)
    self.globalAndLocalPostcondition(self.obj356, rootNode)

    self.globalPrecondition( rootNode )

    self.obj357=Basic(self)

    self.obj357.is_default.setValue((None, 1))
    self.obj357.is_default.config = 0
    self.obj357.name.setValue('A')
    self.obj357.exit_action.setValue('[DUMP("exiting state A")]\n\n')
    self.obj357.enter_action.setValue('[DUMP("entering state A")]\n\n')
    self.obj357.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(107.0,147.0,self.obj357)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(127.99999999999999, 150.0, 127.99999999999999, 150.0))
       self.UMLmodel.coords(new_obj.connectors[1],(127.99999999999999, 168.0, 127.99999999999999, 168.0))
       self.UMLmodel.coords(new_obj.connectors[2],(137.0, 159.0, 137.0, 159.0))
       self.UMLmodel.coords(new_obj.connectors[3],(119.99999999999999, 159.0, 119.99999999999999, 159.0))
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
    self.obj357.graphObject_ = new_obj
    rootNode.addNode(self.obj357)
    self.globalAndLocalPostcondition(self.obj357, rootNode)

    self.globalPrecondition( rootNode )

    self.obj358=Basic(self)

    self.obj358.is_default.setValue((None, 0))
    self.obj358.is_default.config = 0
    self.obj358.name.setValue('B')
    self.obj358.exit_action.setValue('\n\n')
    self.obj358.enter_action.setValue('\n\n')
    self.obj358.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(248.0,149.0,self.obj358)
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
    self.obj358.graphObject_ = new_obj
    rootNode.addNode(self.obj358)
    self.globalAndLocalPostcondition(self.obj358, rootNode)

    self.globalPrecondition( rootNode )

    self.obj359=Basic(self)

    self.obj359.is_default.setValue((None, 0))
    self.obj359.is_default.config = 0
    self.obj359.name.setValue('C')
    self.obj359.exit_action.setValue('[DUMP("exiting state C")]\n\n')
    self.obj359.enter_action.setValue('[DUMP("entering state C")]\n')
    self.obj359.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(352.0,179.0,self.obj359)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(373.0, 182.0, 373.0, 182.0))
       self.UMLmodel.coords(new_obj.connectors[1],(373.0, 200.0, 373.0, 200.0))
       self.UMLmodel.coords(new_obj.connectors[2],(382.0, 191.0, 382.0, 191.0))
       self.UMLmodel.coords(new_obj.connectors[3],(365.0, 191.0, 365.0, 191.0))
       self.UMLmodel.coords(new_obj.gf3.handler,364.0,182.0,382.0,200.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,375.0,209.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='C')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj359.graphObject_ = new_obj
    rootNode.addNode(self.obj359)
    self.globalAndLocalPostcondition(self.obj359, rootNode)

    self.globalPrecondition( rootNode )

    self.obj360=Basic(self)

    self.obj360.is_default.setValue((None, 1))
    self.obj360.is_default.config = 0
    self.obj360.name.setValue('X')
    self.obj360.exit_action.setValue('\n\n')
    self.obj360.enter_action.setValue('\n\n')
    self.obj360.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(435.0,80.0,self.obj360)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(455.99999999999994, 83.0, 455.99999999999994, 83.0))
       self.UMLmodel.coords(new_obj.connectors[1],(455.99999999999994, 101.0, 455.99999999999994, 101.0))
       self.UMLmodel.coords(new_obj.connectors[2],(464.99999999999994, 92.0, 464.99999999999994, 92.0))
       self.UMLmodel.coords(new_obj.connectors[3],(447.99999999999994, 92.0, 447.99999999999994, 92.0))
       self.UMLmodel.coords(new_obj.gf3.handler,447.0,83.0,465.0,101.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,458.0,110.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='X')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj360.graphObject_ = new_obj
    rootNode.addNode(self.obj360)
    self.globalAndLocalPostcondition(self.obj360, rootNode)

    self.globalPrecondition( rootNode )

    self.obj361=Basic(self)

    self.obj361.is_default.setValue((None, 0))
    self.obj361.is_default.config = 0
    self.obj361.name.setValue('Y')
    self.obj361.exit_action.setValue('\n\n')
    self.obj361.enter_action.setValue('\n\n')
    self.obj361.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(483.0,157.0,self.obj361)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(503.99999999999994, 160.0, 503.99999999999994, 160.0))
       self.UMLmodel.coords(new_obj.connectors[1],(503.99999999999994, 178.0, 503.99999999999994, 178.0))
       self.UMLmodel.coords(new_obj.connectors[2],(513.0, 169.0, 513.0, 169.0))
       self.UMLmodel.coords(new_obj.connectors[3],(495.99999999999994, 169.0, 495.99999999999994, 169.0))
       self.UMLmodel.coords(new_obj.gf3.handler,495.0,160.0,513.0,178.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,506.0,187.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Y')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj361.graphObject_ = new_obj
    rootNode.addNode(self.obj361)
    self.globalAndLocalPostcondition(self.obj361, rootNode)

    self.globalPrecondition( rootNode )

    self.obj362=Basic(self)

    self.obj362.is_default.setValue((None, 1))
    self.obj362.is_default.config = 0
    self.obj362.name.setValue('t1')
    self.obj362.exit_action.setValue('\n\n\n')
    self.obj362.enter_action.setValue('\n\n\n')
    self.obj362.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(625.0,80.0,self.obj362)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(646.0, 83.0, 646.0, 83.0))
       self.UMLmodel.coords(new_obj.connectors[1],(646.0, 101.0, 646.0, 101.0))
       self.UMLmodel.coords(new_obj.connectors[2],(655.0, 92.0, 655.0, 92.0))
       self.UMLmodel.coords(new_obj.connectors[3],(638.0, 92.0, 638.0, 92.0))
       self.UMLmodel.coords(new_obj.gf3.handler,637.0,83.0,655.0,101.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,648.0,110.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='t1')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj362.graphObject_ = new_obj
    rootNode.addNode(self.obj362)
    self.globalAndLocalPostcondition(self.obj362, rootNode)

    self.globalPrecondition( rootNode )

    self.obj363=Basic(self)

    self.obj363.is_default.setValue((None, 0))
    self.obj363.is_default.config = 0
    self.obj363.name.setValue('t2')
    self.obj363.exit_action.setValue('\n\n')
    self.obj363.enter_action.setValue('\n\n')
    self.obj363.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(644.0,179.0,self.obj363)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(665.0, 182.0, 665.0, 182.0))
       self.UMLmodel.coords(new_obj.connectors[1],(665.0, 200.0, 665.0, 200.0))
       self.UMLmodel.coords(new_obj.connectors[2],(674.0, 191.0, 674.0, 191.0))
       self.UMLmodel.coords(new_obj.connectors[3],(657.0, 191.0, 657.0, 191.0))
       self.UMLmodel.coords(new_obj.gf3.handler,656.0,182.0,674.0,200.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,667.0,209.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='t2')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj363.graphObject_ = new_obj
    rootNode.addNode(self.obj363)
    self.globalAndLocalPostcondition(self.obj363, rootNode)

    self.globalPrecondition( rootNode )

    self.obj364=Basic(self)

    self.obj364.is_default.setValue((None, 0))
    self.obj364.is_default.config = 0
    self.obj364.name.setValue('inactive')
    self.obj364.exit_action.setValue('\n\n')
    self.obj364.enter_action.setValue('\n\n')
    self.obj364.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(406.0,363.0,self.obj364)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(427.0, 366.0, 427.0, 366.0))
       self.UMLmodel.coords(new_obj.connectors[1],(427.0, 384.0, 427.0, 384.0))
       self.UMLmodel.coords(new_obj.connectors[2],(435.99999999999994, 375.0, 435.99999999999994, 375.0))
       self.UMLmodel.coords(new_obj.connectors[3],(419.0, 375.0, 419.0, 375.0))
       self.UMLmodel.coords(new_obj.gf3.handler,418.0,366.0,436.0,384.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,429.0,393.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='inactive')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj364.graphObject_ = new_obj
    rootNode.addNode(self.obj364)
    self.globalAndLocalPostcondition(self.obj364, rootNode)

    self.globalPrecondition( rootNode )

    self.obj365=History(self)

    self.obj365.is_default.setValue((None, 0))
    self.obj365.is_default.config = 0
    self.obj365.star.setValue((None, 0))
    self.obj365.star.config = 0
    self.obj365.name.setValue('')
    self.obj365.graphClass_= graph_History
    if self.genGraphics:
       from graph_History import *
       new_obj = graph_History(140.0,211.0,self.obj365)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("History", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(162.0, 214.0, 162.0, 214.0))
       self.UMLmodel.coords(new_obj.connectors[1],(179.0, 231.99999999999997, 179.0, 231.99999999999997))
       self.UMLmodel.coords(new_obj.connectors[2],(162.0, 248.99999999999997, 162.0, 248.99999999999997))
       self.UMLmodel.coords(new_obj.connectors[3],(144.0, 232.99999999999997, 144.0, 232.99999999999997))
       self.UMLmodel.coords(new_obj.gf0.handler,144.0,214.0,180.0,249.0)
       self.UMLmodel.itemconfig(new_obj.gf0.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf0.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf0.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf0.handler, fill='lightblue')
       self.UMLmodel.coords(new_obj.gf1.handler,161.0,233.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='H')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       self.UMLmodel.coords(new_obj.gf2.handler,169.0,233.0)
       self.UMLmodel.itemconfig(new_obj.gf2.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, fill='')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, text='*')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, justify='left')
       self.UMLmodel.coords(new_obj.gf3.handler,163.0,258.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='blue')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, text='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, justify='left')
    else: new_obj = None
    self.obj365.graphObject_ = new_obj
    rootNode.addNode(self.obj365)
    self.globalAndLocalPostcondition(self.obj365, rootNode)

    self.globalPrecondition( rootNode )

    self.obj366=Orthogonal(self)

    self.obj366.visible.setValue((None, 1))
    self.obj366.visible.config = 0
    self.obj366.name.setValue('O1')
    self.obj366.auto_adjust.setValue((None, 1))
    self.obj366.auto_adjust.config = 0
    self.obj366.graphClass_= graph_Orthogonal
    if self.genGraphics:
       from graph_Orthogonal import *
       new_obj = graph_Orthogonal(20.0,69.0,self.obj366)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Orthogonal", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(99.0, 176.0, 99.0, 176.0))
       self.UMLmodel.coords(new_obj.connectors[1],(405.0, 176.0, 405.0, 176.0))
       self.UMLmodel.coords(new_obj.connectors[2],(251.99999999999997, 76.0, 251.99999999999997, 76.0))
       self.UMLmodel.coords(new_obj.connectors[3],(251.99999999999997, 277.0, 251.99999999999997, 277.0))
       self.UMLmodel.coords(new_obj.gf5.handler,99.0,76.0,405.0,277.0)
       self.UMLmodel.itemconfig(new_obj.gf5.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, outline='DARKGRAY')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,99.0,69.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='O1')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj366.graphObject_ = new_obj
    rootNode.addNode(self.obj366)
    self.globalAndLocalPostcondition(self.obj366, rootNode)

    self.globalPrecondition( rootNode )

    self.obj367=Orthogonal(self)

    self.obj367.visible.setValue((None, 1))
    self.obj367.visible.config = 0
    self.obj367.name.setValue('O2')
    self.obj367.auto_adjust.setValue((None, 1))
    self.obj367.auto_adjust.config = 0
    self.obj367.graphClass_= graph_Orthogonal
    if self.genGraphics:
       from graph_Orthogonal import *
       new_obj = graph_Orthogonal(325.0,46.0,self.obj367)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Orthogonal", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(434.0, 138.0, 434.0, 138.0))
       self.UMLmodel.coords(new_obj.connectors[1],(573.0, 138.0, 573.0, 138.0))
       self.UMLmodel.coords(new_obj.connectors[2],(502.99999999999994, 77.0, 502.99999999999994, 77.0))
       self.UMLmodel.coords(new_obj.connectors[3],(502.99999999999994, 199.0, 502.99999999999994, 199.0))
       self.UMLmodel.coords(new_obj.gf5.handler,434.0,77.0,573.0,199.0)
       self.UMLmodel.itemconfig(new_obj.gf5.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, outline='DARKGRAY')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,434.0,70.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='O2')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj367.graphObject_ = new_obj
    rootNode.addNode(self.obj367)
    self.globalAndLocalPostcondition(self.obj367, rootNode)

    self.globalPrecondition( rootNode )

    self.obj368=Orthogonal(self)

    self.obj368.visible.setValue((None, 1))
    self.obj368.visible.config = 0
    self.obj368.name.setValue('O3')
    self.obj368.auto_adjust.setValue((None, 1))
    self.obj368.auto_adjust.config = 0
    self.obj368.graphClass_= graph_Orthogonal
    if self.genGraphics:
       from graph_Orthogonal import *
       new_obj = graph_Orthogonal(570.0,76.0,self.obj368)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Orthogonal", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(600.0, 149.0, 600.0, 149.0))
       self.UMLmodel.coords(new_obj.connectors[1],(759.0, 149.0, 759.0, 149.0))
       self.UMLmodel.coords(new_obj.connectors[2],(679.0, 77.0, 679.0, 77.0))
       self.UMLmodel.coords(new_obj.connectors[3],(679.0, 220.99999999999997, 679.0, 220.99999999999997))
       self.UMLmodel.coords(new_obj.gf5.handler,600.0,77.0,759.0,221.0)
       self.UMLmodel.itemconfig(new_obj.gf5.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, outline='DARKGRAY')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,600.0,70.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='O3')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj368.graphObject_ = new_obj
    rootNode.addNode(self.obj368)
    self.globalAndLocalPostcondition(self.obj368, rootNode)

    self.globalPrecondition( rootNode )

    self.obj369=contains(self)

    self.obj369.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(106.5,138.0,self.obj369)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj369.graphObject_ = new_obj
    rootNode.addNode(self.obj369)
    self.globalAndLocalPostcondition(self.obj369, rootNode)

    self.globalPrecondition( rootNode )

    self.obj370=contains(self)

    self.obj370.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(165.0,138.5,self.obj370)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj370.graphObject_ = new_obj
    rootNode.addNode(self.obj370)
    self.globalAndLocalPostcondition(self.obj370, rootNode)

    self.globalPrecondition( rootNode )

    self.obj371=contains(self)

    self.obj371.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(-3.5,106.5,self.obj371)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj371.graphObject_ = new_obj
    rootNode.addNode(self.obj371)
    self.globalAndLocalPostcondition(self.obj371, rootNode)

    self.globalPrecondition( rootNode )

    self.obj372=contains(self)

    self.obj372.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(157.0,135.0,self.obj372)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj372.graphObject_ = new_obj
    rootNode.addNode(self.obj372)
    self.globalAndLocalPostcondition(self.obj372, rootNode)

    self.globalPrecondition( rootNode )

    self.obj373=contains(self)

    self.obj373.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(271.5,51.5,self.obj373)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj373.graphObject_ = new_obj
    rootNode.addNode(self.obj373)
    self.globalAndLocalPostcondition(self.obj373, rootNode)

    self.globalPrecondition( rootNode )

    self.obj374=contains(self)

    self.obj374.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(295.5,90.0,self.obj374)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj374.graphObject_ = new_obj
    rootNode.addNode(self.obj374)
    self.globalAndLocalPostcondition(self.obj374, rootNode)

    self.globalPrecondition( rootNode )

    self.obj375=contains(self)

    self.obj375.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(174.0,166.5,self.obj375)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj375.graphObject_ = new_obj
    rootNode.addNode(self.obj375)
    self.globalAndLocalPostcondition(self.obj375, rootNode)

    self.globalPrecondition( rootNode )

    self.obj376=contains(self)

    self.obj376.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(579.0,90.5,self.obj376)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj376.graphObject_ = new_obj
    rootNode.addNode(self.obj376)
    self.globalAndLocalPostcondition(self.obj376, rootNode)

    self.globalPrecondition( rootNode )

    self.obj377=contains(self)

    self.obj377.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(588.5,140.0,self.obj377)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj377.graphObject_ = new_obj
    rootNode.addNode(self.obj377)
    self.globalAndLocalPostcondition(self.obj377, rootNode)

    self.globalPrecondition( rootNode )

    self.obj378=Hyperedge(self)

    self.obj378.name.setValue('')
    self.obj378.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj378.guard.setValue('1')
    self.obj378.trigger.setValue('e1')
    self.obj378.action.setValue('[DUMP("triggered by e1")]\n')
    self.obj378.broadcast_to.setValue('')
    self.obj378.display.setValue('e1')
    self.obj378.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(181.5,120.5,self.obj378)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj378.graphObject_ = new_obj
    rootNode.addNode(self.obj378)
    self.globalAndLocalPostcondition(self.obj378, rootNode)

    self.globalPrecondition( rootNode )

    self.obj379=Hyperedge(self)

    self.obj379.name.setValue('')
    self.obj379.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj379.guard.setValue('1')
    self.obj379.trigger.setValue('e2')
    self.obj379.action.setValue('[DUMP("triggered by e2")]\n')
    self.obj379.broadcast_to.setValue('')
    self.obj379.display.setValue('e2')
    self.obj379.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(188.5,192.5,self.obj379)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj379.graphObject_ = new_obj
    rootNode.addNode(self.obj379)
    self.globalAndLocalPostcondition(self.obj379, rootNode)

    self.globalPrecondition( rootNode )

    self.obj380=Hyperedge(self)

    self.obj380.name.setValue('')
    self.obj380.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n\n')
    self.obj380.guard.setValue('1')
    self.obj380.trigger.setValue('e3')
    self.obj380.action.setValue('\n\n')
    self.obj380.broadcast_to.setValue('')
    self.obj380.display.setValue('e3')
    self.obj380.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(309.0,191.5,self.obj380)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj380.graphObject_ = new_obj
    rootNode.addNode(self.obj380)
    self.globalAndLocalPostcondition(self.obj380, rootNode)

    self.globalPrecondition( rootNode )

    self.obj381=Hyperedge(self)

    self.obj381.name.setValue('')
    self.obj381.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n\n')
    self.obj381.guard.setValue('1')
    self.obj381.trigger.setValue('trig1')
    self.obj381.action.setValue('\n\n')
    self.obj381.broadcast_to.setValue('')
    self.obj381.display.setValue('trig1')
    self.obj381.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(527.0,113.5,self.obj381)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj381.graphObject_ = new_obj
    rootNode.addNode(self.obj381)
    self.globalAndLocalPostcondition(self.obj381, rootNode)

    self.globalPrecondition( rootNode )

    self.obj382=Hyperedge(self)

    self.obj382.name.setValue('')
    self.obj382.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n\n\n\n')
    self.obj382.guard.setValue('[INSTATE("active.O3.t1",0)]')
    self.obj382.trigger.setValue('')
    self.obj382.action.setValue('\n\n\n\n')
    self.obj382.broadcast_to.setValue('')
    self.obj382.display.setValue('[O3 in t1]')
    self.obj382.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(444.0,139.5,self.obj382)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj382.graphObject_ = new_obj
    rootNode.addNode(self.obj382)
    self.globalAndLocalPostcondition(self.obj382, rootNode)

    self.globalPrecondition( rootNode )

    self.obj383=Hyperedge(self)

    self.obj383.name.setValue('')
    self.obj383.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj383.guard.setValue('1')
    self.obj383.trigger.setValue('back')
    self.obj383.action.setValue('\n')
    self.obj383.broadcast_to.setValue('')
    self.obj383.display.setValue('back')
    self.obj383.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(202.5,83.5,self.obj383)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj383.graphObject_ = new_obj
    rootNode.addNode(self.obj383)
    self.globalAndLocalPostcondition(self.obj383, rootNode)

    self.globalPrecondition( rootNode )

    self.obj384=Hyperedge(self)

    self.obj384.name.setValue('')
    self.obj384.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj384.guard.setValue('1')
    self.obj384.trigger.setValue('hist')
    self.obj384.action.setValue('\n')
    self.obj384.broadcast_to.setValue('')
    self.obj384.display.setValue('hist')
    self.obj384.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(361.0,231.5,self.obj384)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj384.graphObject_ = new_obj
    rootNode.addNode(self.obj384)
    self.globalAndLocalPostcondition(self.obj384, rootNode)

    self.globalPrecondition( rootNode )

    self.obj385=Hyperedge(self)

    self.obj385.name.setValue('')
    self.obj385.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj385.guard.setValue('1')
    self.obj385.trigger.setValue('AFTER(0.5)')
    self.obj385.action.setValue('\n')
    self.obj385.broadcast_to.setValue('')
    self.obj385.display.setValue('tm(0.5)')
    self.obj385.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(607.5,135.5,self.obj385)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj385.graphObject_ = new_obj
    rootNode.addNode(self.obj385)
    self.globalAndLocalPostcondition(self.obj385, rootNode)

    self.globalPrecondition( rootNode )

    self.obj386=Hyperedge(self)

    self.obj386.name.setValue('')
    self.obj386.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n\n\n\n')
    self.obj386.guard.setValue('1')
    self.obj386.trigger.setValue('AFTER(3)')
    self.obj386.action.setValue('[EVENT("trig1",None)]\n\n\n\n')
    self.obj386.broadcast_to.setValue('')
    self.obj386.display.setValue('tm(3)/trig1')
    self.obj386.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(696.5,138.5,self.obj386)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj386.graphObject_ = new_obj
    rootNode.addNode(self.obj386)
    self.globalAndLocalPostcondition(self.obj386, rootNode)

    self.globalPrecondition( rootNode )

    self.obj387=Hyperedge(self)

    self.obj387.name.setValue('')
    self.obj387.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj387.guard.setValue('1')
    self.obj387.trigger.setValue('activate')
    self.obj387.action.setValue('\n')
    self.obj387.broadcast_to.setValue('')
    self.obj387.display.setValue('activate')
    self.obj387.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(427.5,336.5,self.obj387)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj387.graphObject_ = new_obj
    rootNode.addNode(self.obj387)
    self.globalAndLocalPostcondition(self.obj387, rootNode)

    self.globalPrecondition( rootNode )

    self.obj388=Hyperedge(self)

    self.obj388.name.setValue('')
    self.obj388.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj388.guard.setValue('1')
    self.obj388.trigger.setValue('deactivate')
    self.obj388.action.setValue('\n')
    self.obj388.broadcast_to.setValue('')
    self.obj388.display.setValue('deactivate')
    self.obj388.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(17.5,168.5,self.obj388)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj388.graphObject_ = new_obj
    rootNode.addNode(self.obj388)
    self.globalAndLocalPostcondition(self.obj388, rootNode)

    self.globalPrecondition( rootNode )

    self.obj389=orthogonality(self)

    self.obj389.graphClass_= graph_orthogonality
    if self.genGraphics:
       from graph_orthogonality import *
       new_obj = graph_orthogonality(92.0,66.5,self.obj389)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("orthogonality", new_obj.tag)
    else: new_obj = None
    self.obj389.graphObject_ = new_obj
    rootNode.addNode(self.obj389)
    self.globalAndLocalPostcondition(self.obj389, rootNode)

    self.globalPrecondition( rootNode )

    self.obj390=orthogonality(self)

    self.obj390.graphClass_= graph_orthogonality
    if self.genGraphics:
       from graph_orthogonality import *
       new_obj = graph_orthogonality(256.0,67.0,self.obj390)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("orthogonality", new_obj.tag)
    else: new_obj = None
    self.obj390.graphObject_ = new_obj
    rootNode.addNode(self.obj390)
    self.globalAndLocalPostcondition(self.obj390, rootNode)

    self.globalPrecondition( rootNode )

    self.obj391=orthogonality(self)

    self.obj391.graphClass_= graph_orthogonality
    if self.genGraphics:
       from graph_orthogonality import *
       new_obj = graph_orthogonality(342.5,67.0,self.obj391)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("orthogonality", new_obj.tag)
    else: new_obj = None
    self.obj391.graphObject_ = new_obj
    rootNode.addNode(self.obj391)
    self.globalAndLocalPostcondition(self.obj391, rootNode)
    self.drawConnections((self.obj355,self.obj369,[112.99999999999999, 191.0, 106.5, 138.0], 0, 2), (self.obj355,self.obj370,[199.0, 111.99999999999999, 165.0, 138.5], 0, 2), (self.obj355,self.obj380,[285.0, 191.0, 309.0, 191.5], 0, 2), (self.obj355,self.obj375,[199.0, 270.0, 174.0, 166.5], 0, 2), (self.obj356,self.obj389,[85.0, 170.0, 92.0, 66.5], 0, 2), (self.obj356,self.obj390,[425.0, 56.999999999999993, 255.99999999999997, 67.0], 0, 2), (self.obj356,self.obj391,[425.0, 56.999999999999993, 342.5, 67.0], 0, 2), (self.obj356,self.obj388,[85.0, 170.0, 17.5, 168.5], 0, 2), (self.obj357,self.obj378,[137.0, 159.0, 181.5, 120.49999999999999], 0, 2), (self.obj358,self.obj379,[261.0, 161.0, 188.5, 192.5], 0, 2), (self.obj359,self.obj383,[373.0, 182.0, 364.0, 85.0, 202.5, 83.5], 0, 3), (self.obj359,self.obj384,[373.0, 200.0, 361.0, 231.49999999999997], 0, 2), (self.obj360,self.obj381,[464.99999999999994, 92.0, 527.0, 113.49999999999999], 0, 2), (self.obj361,self.obj382,[495.99999999999994, 169.0, 443.99999999999994, 139.5], 0, 2), (self.obj362,self.obj385,[638.0, 92.0, 607.5, 135.5], 0, 2), (self.obj363,self.obj386,[674.0, 191.0, 696.5, 138.5], 0, 2), (self.obj364,self.obj387,[427.0, 366.0, 427.5, 336.5], 0, 2), (self.obj366,self.obj371,[395.0, 176.0, -3.4999999999999996, 106.5], 0, 2), (self.obj366,self.obj372,[246.99999999999997, 76.0, 157.0, 135.0], 0, 2), (self.obj367,self.obj373,[561.0, 138.0, 271.5, 51.5], 0, 2), (self.obj367,self.obj374,[434.0, 138.0, 295.5, 90.0], 0, 2), (self.obj368,self.obj376,[764.0, 149.0, 579.0, 90.5], 0, 2), (self.obj368,self.obj377,[674.0, 220.99999999999997, 588.5, 140.0], 0, 2), (self.obj369,self.obj357,[106.5, 138.0, 127.99999999999999, 150.0], 0, 2), (self.obj370,self.obj358,[165.0, 138.5, 261.0, 161.0], 0, 2), (self.obj371,self.obj355,[-3.4999999999999996, 106.5, 112.99999999999999, 191.0], 0, 2), (self.obj372,self.obj359,[157.0, 135.0, 365.0, 191.0], 0, 2), (self.obj373,self.obj360,[271.5, 51.5, 447.99999999999994, 92.0], 0, 2), (self.obj374,self.obj361,[295.5, 90.0, 495.99999999999994, 169.0], 0, 2), (self.obj375,self.obj365,[174.0, 166.5, 144.0, 232.99999999999997], 0, 2), (self.obj376,self.obj362,[579.0, 90.5, 646.0, 101.0], 0, 2), (self.obj377,self.obj363,[588.5, 140.0, 665.0, 182.0], 0, 2), (self.obj378,self.obj358,[181.5, 120.49999999999999, 261.0, 161.0], 0, 2), (self.obj379,self.obj357,[188.5, 192.5, 137.0, 159.0], 0, 2), (self.obj380,self.obj359,[309.0, 191.5, 365.0, 191.0], 0, 2), (self.obj381,self.obj361,[527.0, 113.49999999999999, 513.0, 169.0], 0, 2), (self.obj382,self.obj360,[443.99999999999994, 139.5, 447.99999999999994, 92.0], 0, 2), (self.obj383,self.obj355,[202.5, 83.5, 199.0, 112.99999999999999], 0, 2), (self.obj384,self.obj365,[361.0, 231.49999999999997, 179.0, 231.99999999999997], 0, 2), (self.obj385,self.obj363,[607.5, 135.5, 657.0, 191.0], 0, 2), (self.obj386,self.obj362,[696.5, 138.5, 655.0, 92.0], 0, 2), (self.obj387,self.obj356,[427.5, 336.5, 425.0, 284.0], 0, 2), (self.obj388,self.obj364,[17.5, 168.5, 18.0, 375.0, 419.0, 375.0], 0, 3), (self.obj389,self.obj366,[92.0, 66.5, 99.0, 176.0], 0, 2), (self.obj390,self.obj367,[255.99999999999997, 67.0, 434.0, 138.0], 0, 2), (self.obj391,self.obj368,[342.5, 67.0, 600.0, 149.0], 0, 2) )

newfunction = m9_Statecharts_mdl

loadedMMName = 'DCharts'
