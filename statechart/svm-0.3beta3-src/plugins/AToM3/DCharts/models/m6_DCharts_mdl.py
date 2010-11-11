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

def m6_DCharts_mdl(self, rootNode):

    self.globalPrecondition( rootNode )

    self.obj236=Composite(self)

    self.obj236.auto_adjust.setValue((None, 1))
    self.obj236.auto_adjust.config = 0
    self.obj236.name.setValue('AB')
    self.obj236.is_default.setValue((None, 1))
    self.obj236.is_default.config = 0
    self.obj236.visible.setValue((None, 1))
    self.obj236.visible.config = 0
    self.obj236.exit_action.setValue('\n\n\n')
    self.obj236.enter_action.setValue('\n\n\n')
    self.obj236.graphClass_= graph_Composite
    if self.genGraphics:
       from graph_Composite import *
       new_obj = graph_Composite(49.0,76.0,self.obj236)
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
    self.obj236.graphObject_ = new_obj
    rootNode.addNode(self.obj236)
    self.globalAndLocalPostcondition(self.obj236, rootNode)

    self.globalPrecondition( rootNode )

    self.obj237=Basic(self)

    self.obj237.is_default.setValue((None, 1))
    self.obj237.is_default.config = 0
    self.obj237.name.setValue('A')
    self.obj237.exit_action.setValue('[DUMP("exiting state A")]\n\n')
    self.obj237.enter_action.setValue('[DUMP("entering state A")]\n\n')
    self.obj237.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(107.0,147.0,self.obj237)
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
    self.obj237.graphObject_ = new_obj
    rootNode.addNode(self.obj237)
    self.globalAndLocalPostcondition(self.obj237, rootNode)

    self.globalPrecondition( rootNode )

    self.obj238=Basic(self)

    self.obj238.is_default.setValue((None, 0))
    self.obj238.is_default.config = 0
    self.obj238.name.setValue('B')
    self.obj238.exit_action.setValue('\n\n')
    self.obj238.enter_action.setValue('\n\n')
    self.obj238.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(248.0,149.0,self.obj238)
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
    self.obj238.graphObject_ = new_obj
    rootNode.addNode(self.obj238)
    self.globalAndLocalPostcondition(self.obj238, rootNode)

    self.globalPrecondition( rootNode )

    self.obj239=Basic(self)

    self.obj239.is_default.setValue((None, 0))
    self.obj239.is_default.config = 0
    self.obj239.name.setValue('C')
    self.obj239.exit_action.setValue('[DUMP("exiting state C")]\n\n')
    self.obj239.enter_action.setValue('[DUMP("entering state C")]\n')
    self.obj239.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(352.0,179.0,self.obj239)
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
    self.obj239.graphObject_ = new_obj
    rootNode.addNode(self.obj239)
    self.globalAndLocalPostcondition(self.obj239, rootNode)

    self.globalPrecondition( rootNode )

    self.obj240=Basic(self)

    self.obj240.is_default.setValue((None, 1))
    self.obj240.is_default.config = 0
    self.obj240.name.setValue('X')
    self.obj240.exit_action.setValue('\n\n')
    self.obj240.enter_action.setValue('\n\n')
    self.obj240.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(434.0,98.0,self.obj240)
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
    self.obj240.graphObject_ = new_obj
    rootNode.addNode(self.obj240)
    self.globalAndLocalPostcondition(self.obj240, rootNode)

    self.globalPrecondition( rootNode )

    self.obj241=Basic(self)

    self.obj241.is_default.setValue((None, 0))
    self.obj241.is_default.config = 0
    self.obj241.name.setValue('Y')
    self.obj241.exit_action.setValue('\n\n')
    self.obj241.enter_action.setValue('\n\n')
    self.obj241.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(482.0,175.0,self.obj241)
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
    self.obj241.graphObject_ = new_obj
    rootNode.addNode(self.obj241)
    self.globalAndLocalPostcondition(self.obj241, rootNode)

    self.globalPrecondition( rootNode )

    self.obj242=History(self)

    self.obj242.is_default.setValue((None, 0))
    self.obj242.is_default.config = 0
    self.obj242.star.setValue((None, 0))
    self.obj242.star.config = 0
    self.obj242.name.setValue('')
    self.obj242.graphClass_= graph_History
    if self.genGraphics:
       from graph_History import *
       new_obj = graph_History(140.0,211.0,self.obj242)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("History", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(162.0, 214.00000000000003, 162.0, 214.00000000000003))
       self.UMLmodel.coords(new_obj.connectors[1],(179.0, 232.0, 179.0, 232.0))
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
    self.obj242.graphObject_ = new_obj
    rootNode.addNode(self.obj242)
    self.globalAndLocalPostcondition(self.obj242, rootNode)

    self.globalPrecondition( rootNode )

    self.obj243=Orthogonal(self)

    self.obj243.visible.setValue((None, 1))
    self.obj243.visible.config = 0
    self.obj243.name.setValue('O1')
    self.obj243.auto_adjust.setValue((None, 1))
    self.obj243.auto_adjust.config = 0
    self.obj243.graphClass_= graph_Orthogonal
    if self.genGraphics:
       from graph_Orthogonal import *
       new_obj = graph_Orthogonal(20.0,69.0,self.obj243)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Orthogonal", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(99.0, 176.0, 99.0, 176.0))
       self.UMLmodel.coords(new_obj.connectors[1],(405.0, 176.0, 405.0, 176.0))
       self.UMLmodel.coords(new_obj.connectors[2],(251.99999999999997, 76.0, 251.99999999999997, 76.0))
       self.UMLmodel.coords(new_obj.connectors[3],(251.99999999999997, 277.0, 251.99999999999997, 277.0))
       self.UMLmodel.coords(new_obj.gf5.handler,99.0,76.0,405.0,277.0)
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
    self.obj243.graphObject_ = new_obj
    rootNode.addNode(self.obj243)
    self.globalAndLocalPostcondition(self.obj243, rootNode)

    self.globalPrecondition( rootNode )

    self.obj244=Orthogonal(self)

    self.obj244.visible.setValue((None, 1))
    self.obj244.visible.config = 0
    self.obj244.name.setValue('O2')
    self.obj244.auto_adjust.setValue((None, 1))
    self.obj244.auto_adjust.config = 0
    self.obj244.graphClass_= graph_Orthogonal
    if self.genGraphics:
       from graph_Orthogonal import *
       new_obj = graph_Orthogonal(324.0,64.0,self.obj244)
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
    self.obj244.graphObject_ = new_obj
    rootNode.addNode(self.obj244)
    self.globalAndLocalPostcondition(self.obj244, rootNode)

    self.globalPrecondition( rootNode )

    self.obj245=contains(self)

    self.obj245.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(106.5,138.0,self.obj245)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj245.graphObject_ = new_obj
    rootNode.addNode(self.obj245)
    self.globalAndLocalPostcondition(self.obj245, rootNode)

    self.globalPrecondition( rootNode )

    self.obj246=contains(self)

    self.obj246.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(165.0,138.5,self.obj246)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj246.graphObject_ = new_obj
    rootNode.addNode(self.obj246)
    self.globalAndLocalPostcondition(self.obj246, rootNode)

    self.globalPrecondition( rootNode )

    self.obj247=contains(self)

    self.obj247.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(-3.5,106.5,self.obj247)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj247.graphObject_ = new_obj
    rootNode.addNode(self.obj247)
    self.globalAndLocalPostcondition(self.obj247, rootNode)

    self.globalPrecondition( rootNode )

    self.obj248=contains(self)

    self.obj248.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(157.0,135.0,self.obj248)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj248.graphObject_ = new_obj
    rootNode.addNode(self.obj248)
    self.globalAndLocalPostcondition(self.obj248, rootNode)

    self.globalPrecondition( rootNode )

    self.obj249=contains(self)

    self.obj249.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(269.5,87.5,self.obj249)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj249.graphObject_ = new_obj
    rootNode.addNode(self.obj249)
    self.globalAndLocalPostcondition(self.obj249, rootNode)

    self.globalPrecondition( rootNode )

    self.obj250=contains(self)

    self.obj250.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(293.5,126.0,self.obj250)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj250.graphObject_ = new_obj
    rootNode.addNode(self.obj250)
    self.globalAndLocalPostcondition(self.obj250, rootNode)

    self.globalPrecondition( rootNode )

    self.obj251=contains(self)

    self.obj251.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(174.0,166.5,self.obj251)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj251.graphObject_ = new_obj
    rootNode.addNode(self.obj251)
    self.globalAndLocalPostcondition(self.obj251, rootNode)

    self.globalPrecondition( rootNode )

    self.obj252=Hyperedge(self)

    self.obj252.name.setValue('')
    self.obj252.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj252.guard.setValue('1')
    self.obj252.trigger.setValue('e1')
    self.obj252.action.setValue('[DUMP("triggered by e1")]\n')
    self.obj252.broadcast_to.setValue('')
    self.obj252.display.setValue('e1')
    self.obj252.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(181.5,120.5,self.obj252)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj252.graphObject_ = new_obj
    rootNode.addNode(self.obj252)
    self.globalAndLocalPostcondition(self.obj252, rootNode)

    self.globalPrecondition( rootNode )

    self.obj253=Hyperedge(self)

    self.obj253.name.setValue('')
    self.obj253.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj253.guard.setValue('1')
    self.obj253.trigger.setValue('e2')
    self.obj253.action.setValue('[DUMP("triggered by e2")]\n')
    self.obj253.broadcast_to.setValue('')
    self.obj253.display.setValue('e2')
    self.obj253.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(188.5,192.5,self.obj253)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj253.graphObject_ = new_obj
    rootNode.addNode(self.obj253)
    self.globalAndLocalPostcondition(self.obj253, rootNode)

    self.globalPrecondition( rootNode )

    self.obj254=Hyperedge(self)

    self.obj254.name.setValue('')
    self.obj254.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n\n')
    self.obj254.guard.setValue('1')
    self.obj254.trigger.setValue('e3')
    self.obj254.action.setValue('\n\n')
    self.obj254.broadcast_to.setValue('')
    self.obj254.display.setValue('e3')
    self.obj254.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(309.0,191.5,self.obj254)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj254.graphObject_ = new_obj
    rootNode.addNode(self.obj254)
    self.globalAndLocalPostcondition(self.obj254, rootNode)

    self.globalPrecondition( rootNode )

    self.obj255=Hyperedge(self)

    self.obj255.name.setValue('')
    self.obj255.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj255.guard.setValue('1')
    self.obj255.trigger.setValue('AFTER(1)')
    self.obj255.action.setValue('\n')
    self.obj255.broadcast_to.setValue('')
    self.obj255.display.setValue('tm(1)')
    self.obj255.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(526.0,131.5,self.obj255)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj255.graphObject_ = new_obj
    rootNode.addNode(self.obj255)
    self.globalAndLocalPostcondition(self.obj255, rootNode)

    self.globalPrecondition( rootNode )

    self.obj256=Hyperedge(self)

    self.obj256.name.setValue('')
    self.obj256.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj256.guard.setValue('1')
    self.obj256.trigger.setValue('AFTER(2)')
    self.obj256.action.setValue('\n')
    self.obj256.broadcast_to.setValue('')
    self.obj256.display.setValue('tm(2)')
    self.obj256.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(434.0,169.5,self.obj256)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj256.graphObject_ = new_obj
    rootNode.addNode(self.obj256)
    self.globalAndLocalPostcondition(self.obj256, rootNode)

    self.globalPrecondition( rootNode )

    self.obj257=Hyperedge(self)

    self.obj257.name.setValue('')
    self.obj257.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj257.guard.setValue('1')
    self.obj257.trigger.setValue('back')
    self.obj257.action.setValue('\n')
    self.obj257.broadcast_to.setValue('')
    self.obj257.display.setValue('back')
    self.obj257.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(202.5,83.5,self.obj257)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj257.graphObject_ = new_obj
    rootNode.addNode(self.obj257)
    self.globalAndLocalPostcondition(self.obj257, rootNode)

    self.globalPrecondition( rootNode )

    self.obj258=Hyperedge(self)

    self.obj258.name.setValue('')
    self.obj258.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj258.guard.setValue('1')
    self.obj258.trigger.setValue('hist')
    self.obj258.action.setValue('\n')
    self.obj258.broadcast_to.setValue('')
    self.obj258.display.setValue('hist')
    self.obj258.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(361.0,231.5,self.obj258)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj258.graphObject_ = new_obj
    rootNode.addNode(self.obj258)
    self.globalAndLocalPostcondition(self.obj258, rootNode)
    self.drawConnections((self.obj236,self.obj245,[113.0, 191.0, 106.5, 138.0], 0, 2), (self.obj236,self.obj246,[198.99999999999997, 113.0, 165.0, 138.5], 0, 2), (self.obj236,self.obj254,[285.0, 191.0, 309.0, 191.5], 0, 2), (self.obj236,self.obj251,[198.99999999999997, 270.0, 174.0, 166.5], 0, 2), (self.obj237,self.obj252,[137.0, 159.0, 181.5, 120.5], 0, 2), (self.obj238,self.obj253,[261.0, 161.0, 188.5, 192.49999999999997], 0, 2), (self.obj239,self.obj257,[373.0, 182.0, 364.0, 85.0, 202.5, 83.5], 0, 3), (self.obj239,self.obj258,[373.0, 200.0, 361.0, 231.5], 0, 2), (self.obj240,self.obj255,[464.0, 110.00000000000001, 526.0, 131.5], 0, 2), (self.obj241,self.obj256,[495.0, 187.0, 434.00000000000006, 169.5], 0, 2), (self.obj243,self.obj247,[395.0, 176.0, -3.4999999999999996, 106.5], 0, 2), (self.obj243,self.obj248,[247.0, 76.0, 157.0, 135.0], 0, 2), (self.obj244,self.obj249,[560.0, 156.0, 269.5, 87.5], 0, 2), (self.obj244,self.obj250,[426.0, 156.0, 293.5, 125.99999999999999], 0, 2), (self.obj245,self.obj237,[106.5, 138.0, 128.0, 150.0], 0, 2), (self.obj246,self.obj238,[165.0, 138.5, 261.0, 161.0], 0, 2), (self.obj247,self.obj236,[-3.4999999999999996, 106.5, 113.0, 191.0], 0, 2), (self.obj248,self.obj239,[157.0, 135.0, 365.0, 191.0], 0, 2), (self.obj249,self.obj240,[269.5, 87.5, 446.99999999999994, 110.00000000000001], 0, 2), (self.obj250,self.obj241,[293.5, 125.99999999999999, 495.0, 187.0], 0, 2), (self.obj251,self.obj242,[174.0, 166.5, 144.0, 232.99999999999997], 0, 2), (self.obj252,self.obj238,[181.5, 120.5, 261.0, 161.0], 0, 2), (self.obj253,self.obj237,[188.5, 192.49999999999997, 137.0, 159.0], 0, 2), (self.obj254,self.obj239,[309.0, 191.5, 365.0, 191.0], 0, 2), (self.obj255,self.obj241,[526.0, 131.5, 512.0, 187.0], 0, 2), (self.obj256,self.obj240,[434.00000000000006, 169.5, 446.99999999999994, 110.00000000000001], 0, 2), (self.obj257,self.obj236,[202.5, 83.5, 198.99999999999997, 113.0], 0, 2), (self.obj258,self.obj242,[361.0, 231.5, 179.0, 232.0], 0, 2) )

newfunction = m6_DCharts_mdl

loadedMMName = 'DCharts'
