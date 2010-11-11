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

def m5_DCharts_mdl(self, rootNode):

    self.globalPrecondition( rootNode )

    self.obj169=Composite(self)

    self.obj169.auto_adjust.setValue((None, 1))
    self.obj169.auto_adjust.config = 0
    self.obj169.name.setValue('AB')
    self.obj169.is_default.setValue((None, 1))
    self.obj169.is_default.config = 0
    self.obj169.visible.setValue((None, 1))
    self.obj169.visible.config = 0
    self.obj169.exit_action.setValue('\n\n\n')
    self.obj169.enter_action.setValue('\n\n\n')
    self.obj169.graphClass_= graph_Composite
    if self.genGraphics:
       from graph_Composite import *
       new_obj = graph_Composite(49.0,76.0,self.obj169)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Composite", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(113.0, 191.0, 113.0, 191.0))
       self.UMLmodel.coords(new_obj.connectors[1],(285.0, 191.0, 285.0, 191.0))
       self.UMLmodel.coords(new_obj.connectors[2],(198.99999999999997, 113.0, 198.99999999999997, 113.0))
       self.UMLmodel.coords(new_obj.connectors[3],(198.99999999999997, 270.0, 198.99999999999997, 270.0))
       self.UMLmodel.coords(new_obj.gf2.handler,113.0,113.0,285.0,270.0)
       self.UMLmodel.itemconfig(new_obj.gf2.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, outline='DARKGREEN')
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
    self.obj169.graphObject_ = new_obj
    rootNode.addNode(self.obj169)
    self.globalAndLocalPostcondition(self.obj169, rootNode)

    self.globalPrecondition( rootNode )

    self.obj170=Basic(self)

    self.obj170.is_default.setValue((None, 1))
    self.obj170.is_default.config = 0
    self.obj170.name.setValue('A')
    self.obj170.exit_action.setValue('[DUMP("exiting state A")]\n\n')
    self.obj170.enter_action.setValue('[DUMP("entering state A")]\n\n')
    self.obj170.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(107.0,147.0,self.obj170)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(128.0, 150.0, 128.0, 150.0))
       self.UMLmodel.coords(new_obj.connectors[1],(128.0, 168.0, 128.0, 168.0))
       self.UMLmodel.coords(new_obj.connectors[2],(137.0, 159.0, 137.0, 159.0))
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
    self.obj170.graphObject_ = new_obj
    rootNode.addNode(self.obj170)
    self.globalAndLocalPostcondition(self.obj170, rootNode)

    self.globalPrecondition( rootNode )

    self.obj171=Basic(self)

    self.obj171.is_default.setValue((None, 0))
    self.obj171.is_default.config = 0
    self.obj171.name.setValue('B')
    self.obj171.exit_action.setValue('\n\n')
    self.obj171.enter_action.setValue('\n\n')
    self.obj171.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(248.0,149.0,self.obj171)
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
    self.obj171.graphObject_ = new_obj
    rootNode.addNode(self.obj171)
    self.globalAndLocalPostcondition(self.obj171, rootNode)

    self.globalPrecondition( rootNode )

    self.obj172=Basic(self)

    self.obj172.is_default.setValue((None, 0))
    self.obj172.is_default.config = 0
    self.obj172.name.setValue('C')
    self.obj172.exit_action.setValue('[DUMP("exiting state C")]\n\n')
    self.obj172.enter_action.setValue('[DUMP("entering state C")]\n')
    self.obj172.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(352.0,179.0,self.obj172)
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
    self.obj172.graphObject_ = new_obj
    rootNode.addNode(self.obj172)
    self.globalAndLocalPostcondition(self.obj172, rootNode)

    self.globalPrecondition( rootNode )

    self.obj173=Basic(self)

    self.obj173.is_default.setValue((None, 1))
    self.obj173.is_default.config = 0
    self.obj173.name.setValue('X')
    self.obj173.exit_action.setValue('\n\n')
    self.obj173.enter_action.setValue('\n\n')
    self.obj173.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(434.0,98.0,self.obj173)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(455.0, 100.99999999999999, 455.0, 100.99999999999999))
       self.UMLmodel.coords(new_obj.connectors[1],(455.0, 119.0, 455.0, 119.0))
       self.UMLmodel.coords(new_obj.connectors[2],(464.0, 110.00000000000001, 464.0, 110.00000000000001))
       self.UMLmodel.coords(new_obj.connectors[3],(446.99999999999994, 110.00000000000001, 446.99999999999994, 110.00000000000001))
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
    self.obj173.graphObject_ = new_obj
    rootNode.addNode(self.obj173)
    self.globalAndLocalPostcondition(self.obj173, rootNode)

    self.globalPrecondition( rootNode )

    self.obj174=Basic(self)

    self.obj174.is_default.setValue((None, 0))
    self.obj174.is_default.config = 0
    self.obj174.name.setValue('Y')
    self.obj174.exit_action.setValue('\n\n')
    self.obj174.enter_action.setValue('\n\n')
    self.obj174.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(482.0,175.0,self.obj174)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(503.00000000000006, 178.0, 503.00000000000006, 178.0))
       self.UMLmodel.coords(new_obj.connectors[1],(503.00000000000006, 196.0, 503.00000000000006, 196.0))
       self.UMLmodel.coords(new_obj.connectors[2],(512.0, 187.0, 512.0, 187.0))
       self.UMLmodel.coords(new_obj.connectors[3],(495.0, 187.0, 495.0, 187.0))
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
    self.obj174.graphObject_ = new_obj
    rootNode.addNode(self.obj174)
    self.globalAndLocalPostcondition(self.obj174, rootNode)

    self.globalPrecondition( rootNode )

    self.obj191=History(self)

    self.obj191.is_default.setValue((None, 0))
    self.obj191.is_default.config = 0
    self.obj191.star.setValue((None, 0))
    self.obj191.star.config = 0
    self.obj191.name.setValue('')
    self.obj191.graphClass_= graph_History
    if self.genGraphics:
       from graph_History import *
       new_obj = graph_History(140.0,211.0,self.obj191)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("History", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(162.0, 214.0, 162.0, 214.0))
       self.UMLmodel.coords(new_obj.connectors[1],(179.0, 232.0, 179.0, 232.0))
       self.UMLmodel.coords(new_obj.connectors[2],(162.0, 248.99999999999997, 162.0, 248.99999999999997))
       self.UMLmodel.coords(new_obj.connectors[3],(144.0, 233.00000000000003, 144.0, 233.00000000000003))
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
    self.obj191.graphObject_ = new_obj
    rootNode.addNode(self.obj191)
    self.globalAndLocalPostcondition(self.obj191, rootNode)

    self.globalPrecondition( rootNode )

    self.obj175=Orthogonal(self)

    self.obj175.visible.setValue((None, 1))
    self.obj175.visible.config = 0
    self.obj175.name.setValue('O1')
    self.obj175.auto_adjust.setValue((None, 1))
    self.obj175.auto_adjust.config = 0
    self.obj175.graphClass_= graph_Orthogonal
    if self.genGraphics:
       from graph_Orthogonal import *
       new_obj = graph_Orthogonal(20.0,69.0,self.obj175)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Orthogonal", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(99.0, 176.0, 99.0, 176.0))
       self.UMLmodel.coords(new_obj.connectors[1],(395.0, 176.0, 395.0, 176.0))
       self.UMLmodel.coords(new_obj.connectors[2],(247.0, 76.0, 247.0, 76.0))
       self.UMLmodel.coords(new_obj.connectors[3],(247.0, 277.0, 247.0, 277.0))
       self.UMLmodel.coords(new_obj.gf5.handler,99.0,76.0,395.0,277.0)
       self.UMLmodel.itemconfig(new_obj.gf5.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, outline='darkgray')
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
    self.obj175.graphObject_ = new_obj
    rootNode.addNode(self.obj175)
    self.globalAndLocalPostcondition(self.obj175, rootNode)

    self.globalPrecondition( rootNode )

    self.obj176=Orthogonal(self)

    self.obj176.visible.setValue((None, 1))
    self.obj176.visible.config = 0
    self.obj176.name.setValue('O2')
    self.obj176.auto_adjust.setValue((None, 1))
    self.obj176.auto_adjust.config = 0
    self.obj176.graphClass_= graph_Orthogonal
    if self.genGraphics:
       from graph_Orthogonal import *
       new_obj = graph_Orthogonal(324.0,64.0,self.obj176)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Orthogonal", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(426.0, 156.0, 426.0, 156.0))
       self.UMLmodel.coords(new_obj.connectors[1],(574.0, 156.0, 574.0, 156.0))
       self.UMLmodel.coords(new_obj.connectors[2],(500.0, 95.0, 500.0, 95.0))
       self.UMLmodel.coords(new_obj.connectors[3],(500.0, 217.00000000000003, 500.0, 217.00000000000003))
       self.UMLmodel.coords(new_obj.gf5.handler,426.0,95.0,574.0,217.0)
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
    self.obj176.graphObject_ = new_obj
    rootNode.addNode(self.obj176)
    self.globalAndLocalPostcondition(self.obj176, rootNode)

    self.globalPrecondition( rootNode )

    self.obj177=contains(self)

    self.obj177.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(106.5,138.0,self.obj177)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj177.graphObject_ = new_obj
    rootNode.addNode(self.obj177)
    self.globalAndLocalPostcondition(self.obj177, rootNode)

    self.globalPrecondition( rootNode )

    self.obj178=contains(self)

    self.obj178.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(165.0,138.5,self.obj178)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj178.graphObject_ = new_obj
    rootNode.addNode(self.obj178)
    self.globalAndLocalPostcondition(self.obj178, rootNode)

    self.globalPrecondition( rootNode )

    self.obj179=contains(self)

    self.obj179.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(-3.5,106.5,self.obj179)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj179.graphObject_ = new_obj
    rootNode.addNode(self.obj179)
    self.globalAndLocalPostcondition(self.obj179, rootNode)

    self.globalPrecondition( rootNode )

    self.obj180=contains(self)

    self.obj180.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(157.0,135.0,self.obj180)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj180.graphObject_ = new_obj
    rootNode.addNode(self.obj180)
    self.globalAndLocalPostcondition(self.obj180, rootNode)

    self.globalPrecondition( rootNode )

    self.obj181=contains(self)

    self.obj181.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(269.5,87.5,self.obj181)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj181.graphObject_ = new_obj
    rootNode.addNode(self.obj181)
    self.globalAndLocalPostcondition(self.obj181, rootNode)

    self.globalPrecondition( rootNode )

    self.obj182=contains(self)

    self.obj182.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(293.5,126.0,self.obj182)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj182.graphObject_ = new_obj
    rootNode.addNode(self.obj182)
    self.globalAndLocalPostcondition(self.obj182, rootNode)

    self.globalPrecondition( rootNode )

    self.obj192=contains(self)

    self.obj192.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(174.0,166.5,self.obj192)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj192.graphObject_ = new_obj
    rootNode.addNode(self.obj192)
    self.globalAndLocalPostcondition(self.obj192, rootNode)

    self.globalPrecondition( rootNode )

    self.obj183=Hyperedge(self)

    self.obj183.name.setValue('')
    self.obj183.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj183.guard.setValue('1')
    self.obj183.trigger.setValue('e1')
    self.obj183.action.setValue('[DUMP("triggered by e1")]\n')
    self.obj183.broadcast_to.setValue('')
    self.obj183.display.setValue('e1')
    self.obj183.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(181.5,120.5,self.obj183)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj183.graphObject_ = new_obj
    rootNode.addNode(self.obj183)
    self.globalAndLocalPostcondition(self.obj183, rootNode)

    self.globalPrecondition( rootNode )

    self.obj184=Hyperedge(self)

    self.obj184.name.setValue('')
    self.obj184.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj184.guard.setValue('1')
    self.obj184.trigger.setValue('e2')
    self.obj184.action.setValue('[DUMP("triggered by e2")]\n')
    self.obj184.broadcast_to.setValue('')
    self.obj184.display.setValue('e2')
    self.obj184.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(188.5,192.5,self.obj184)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj184.graphObject_ = new_obj
    rootNode.addNode(self.obj184)
    self.globalAndLocalPostcondition(self.obj184, rootNode)

    self.globalPrecondition( rootNode )

    self.obj185=Hyperedge(self)

    self.obj185.name.setValue('')
    self.obj185.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj185.guard.setValue('1')
    self.obj185.trigger.setValue('e1')
    self.obj185.action.setValue('\n')
    self.obj185.broadcast_to.setValue('')
    self.obj185.display.setValue('e1')
    self.obj185.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(309.0,191.5,self.obj185)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj185.graphObject_ = new_obj
    rootNode.addNode(self.obj185)
    self.globalAndLocalPostcondition(self.obj185, rootNode)

    self.globalPrecondition( rootNode )

    self.obj186=Hyperedge(self)

    self.obj186.name.setValue('')
    self.obj186.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj186.guard.setValue('1')
    self.obj186.trigger.setValue('AFTER(1)')
    self.obj186.action.setValue('\n')
    self.obj186.broadcast_to.setValue('')
    self.obj186.display.setValue('tm(1)')
    self.obj186.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(526.0,131.5,self.obj186)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj186.graphObject_ = new_obj
    rootNode.addNode(self.obj186)
    self.globalAndLocalPostcondition(self.obj186, rootNode)

    self.globalPrecondition( rootNode )

    self.obj187=Hyperedge(self)

    self.obj187.name.setValue('')
    self.obj187.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj187.guard.setValue('1')
    self.obj187.trigger.setValue('AFTER(2)')
    self.obj187.action.setValue('\n')
    self.obj187.broadcast_to.setValue('')
    self.obj187.display.setValue('tm(2)')
    self.obj187.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(434.0,169.5,self.obj187)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj187.graphObject_ = new_obj
    rootNode.addNode(self.obj187)
    self.globalAndLocalPostcondition(self.obj187, rootNode)

    self.globalPrecondition( rootNode )

    self.obj188=Hyperedge(self)

    self.obj188.name.setValue('')
    self.obj188.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj188.guard.setValue('1')
    self.obj188.trigger.setValue('back')
    self.obj188.action.setValue('\n')
    self.obj188.broadcast_to.setValue('')
    self.obj188.display.setValue('back')
    self.obj188.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(202.5,83.5,self.obj188)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj188.graphObject_ = new_obj
    rootNode.addNode(self.obj188)
    self.globalAndLocalPostcondition(self.obj188, rootNode)

    self.globalPrecondition( rootNode )

    self.obj193=Hyperedge(self)

    self.obj193.name.setValue('')
    self.obj193.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj193.guard.setValue('1')
    self.obj193.trigger.setValue('hist')
    self.obj193.action.setValue('\n')
    self.obj193.broadcast_to.setValue('')
    self.obj193.display.setValue('hist')
    self.obj193.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(361.0,231.5,self.obj193)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj193.graphObject_ = new_obj
    rootNode.addNode(self.obj193)
    self.globalAndLocalPostcondition(self.obj193, rootNode)
    self.drawConnections((self.obj169,self.obj177,[113.0, 191.0, 106.5, 138.0], 0, 2), (self.obj169,self.obj178,[198.99999999999997, 113.0, 165.0, 138.5], 0, 2), (self.obj169,self.obj185,[285.0, 191.0, 309.0, 191.5], 0, 2), (self.obj169,self.obj192,[198.99999999999997, 270.0, 174.0, 166.5], 0, 2), (self.obj170,self.obj183,[137.0, 159.0, 181.5, 120.5], 0, 2), (self.obj171,self.obj184,[261.0, 161.0, 188.5, 192.49999999999997], 0, 2), (self.obj172,self.obj188,[373.0, 182.0, 364.0, 85.0, 202.5, 83.5], 0, 3), (self.obj172,self.obj193,[373.0, 200.0, 361.0, 231.5], 0, 2), (self.obj173,self.obj186,[464.0, 110.00000000000001, 526.0, 131.5], 0, 2), (self.obj174,self.obj187,[495.0, 187.0, 434.00000000000006, 169.5], 0, 2), (self.obj175,self.obj179,[395.0, 176.0, -3.4999999999999996, 106.5], 0, 2), (self.obj175,self.obj180,[247.0, 76.0, 157.0, 135.0], 0, 2), (self.obj176,self.obj181,[560.0, 156.0, 269.5, 87.5], 0, 2), (self.obj176,self.obj182,[426.0, 156.0, 293.5, 125.99999999999999], 0, 2), (self.obj177,self.obj170,[106.5, 138.0, 128.0, 150.0], 0, 2), (self.obj178,self.obj171,[165.0, 138.5, 261.0, 161.0], 0, 2), (self.obj179,self.obj169,[-3.4999999999999996, 106.5, 113.0, 191.0], 0, 2), (self.obj180,self.obj172,[157.0, 135.0, 365.0, 191.0], 0, 2), (self.obj181,self.obj173,[269.5, 87.5, 446.99999999999994, 110.00000000000001], 0, 2), (self.obj182,self.obj174,[293.5, 125.99999999999999, 495.0, 187.0], 0, 2), (self.obj192,self.obj191,[174.0, 166.5, 144.0, 232.99999999999997], 0, 2), (self.obj183,self.obj171,[181.5, 120.5, 261.0, 161.0], 0, 2), (self.obj184,self.obj170,[188.5, 192.49999999999997, 137.0, 159.0], 0, 2), (self.obj185,self.obj172,[309.0, 191.5, 365.0, 191.0], 0, 2), (self.obj186,self.obj174,[526.0, 131.5, 512.0, 187.0], 0, 2), (self.obj187,self.obj173,[434.00000000000006, 169.5, 446.99999999999994, 110.00000000000001], 0, 2), (self.obj188,self.obj169,[202.5, 83.5, 198.99999999999997, 113.0], 0, 2), (self.obj193,self.obj191,[361.0, 231.5, 179.0, 232.0], 0, 2) )

newfunction = m5_DCharts_mdl

loadedMMName = 'DCharts'
