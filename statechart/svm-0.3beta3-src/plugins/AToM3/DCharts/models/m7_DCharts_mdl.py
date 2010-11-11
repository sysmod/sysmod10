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

def m7_DCharts_mdl(self, rootNode):

    self.globalPrecondition( rootNode )

    self.obj437=Composite(self)

    self.obj437.auto_adjust.setValue((None, 1))
    self.obj437.auto_adjust.config = 0
    self.obj437.name.setValue('AB')
    self.obj437.is_default.setValue((None, 1))
    self.obj437.is_default.config = 0
    self.obj437.visible.setValue((None, 1))
    self.obj437.visible.config = 0
    self.obj437.exit_action.setValue('\n\n\n')
    self.obj437.enter_action.setValue('\n\n\n')
    self.obj437.graphClass_= graph_Composite
    if self.genGraphics:
       from graph_Composite import *
       new_obj = graph_Composite(49.0,76.0,self.obj437)
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
    self.obj437.graphObject_ = new_obj
    rootNode.addNode(self.obj437)
    self.globalAndLocalPostcondition(self.obj437, rootNode)

    self.globalPrecondition( rootNode )

    self.obj438=Composite(self)

    self.obj438.auto_adjust.setValue((None, 1))
    self.obj438.auto_adjust.config = 0
    self.obj438.name.setValue('active')
    self.obj438.is_default.setValue((None, 1))
    self.obj438.is_default.config = 0
    self.obj438.visible.setValue((None, 1))
    self.obj438.visible.config = 0
    self.obj438.exit_action.setValue('\n\n')
    self.obj438.enter_action.setValue('\n\n')
    self.obj438.graphClass_= graph_Composite
    if self.genGraphics:
       from graph_Composite import *
       new_obj = graph_Composite(40.0,38.0,self.obj438)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Composite", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(85.0, 170.0, 85.0, 170.0))
       self.UMLmodel.coords(new_obj.connectors[1],(755.0, 170.0, 755.0, 170.0))
       self.UMLmodel.coords(new_obj.connectors[2],(420.0, 57.0, 420.0, 57.0))
       self.UMLmodel.coords(new_obj.connectors[3],(420.0, 284.0, 420.0, 284.0))
       self.UMLmodel.coords(new_obj.gf2.handler,85.0,57.0,755.0,284.0)
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
    self.obj438.graphObject_ = new_obj
    rootNode.addNode(self.obj438)
    self.globalAndLocalPostcondition(self.obj438, rootNode)

    self.globalPrecondition( rootNode )

    self.obj439=Basic(self)

    self.obj439.is_default.setValue((None, 1))
    self.obj439.is_default.config = 0
    self.obj439.name.setValue('A')
    self.obj439.exit_action.setValue('[DUMP("exiting state A")]\n\n')
    self.obj439.enter_action.setValue('[DUMP("entering state A")]\n\n')
    self.obj439.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(107.0,147.0,self.obj439)
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
    self.obj439.graphObject_ = new_obj
    rootNode.addNode(self.obj439)
    self.globalAndLocalPostcondition(self.obj439, rootNode)

    self.globalPrecondition( rootNode )

    self.obj440=Basic(self)

    self.obj440.is_default.setValue((None, 0))
    self.obj440.is_default.config = 0
    self.obj440.name.setValue('B')
    self.obj440.exit_action.setValue('\n\n')
    self.obj440.enter_action.setValue('\n\n')
    self.obj440.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(248.0,149.0,self.obj440)
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
    self.obj440.graphObject_ = new_obj
    rootNode.addNode(self.obj440)
    self.globalAndLocalPostcondition(self.obj440, rootNode)

    self.globalPrecondition( rootNode )

    self.obj441=Basic(self)

    self.obj441.is_default.setValue((None, 0))
    self.obj441.is_default.config = 0
    self.obj441.name.setValue('C')
    self.obj441.exit_action.setValue('[DUMP("exiting state C")]\n\n')
    self.obj441.enter_action.setValue('[DUMP("entering state C")]\n')
    self.obj441.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(352.0,179.0,self.obj441)
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
    self.obj441.graphObject_ = new_obj
    rootNode.addNode(self.obj441)
    self.globalAndLocalPostcondition(self.obj441, rootNode)

    self.globalPrecondition( rootNode )

    self.obj442=Basic(self)

    self.obj442.is_default.setValue((None, 1))
    self.obj442.is_default.config = 0
    self.obj442.name.setValue('X')
    self.obj442.exit_action.setValue('\n\n')
    self.obj442.enter_action.setValue('\n\n')
    self.obj442.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(435.0,80.0,self.obj442)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(456.0, 82.999999999999986, 456.0, 82.999999999999986))
       self.UMLmodel.coords(new_obj.connectors[1],(456.0, 101.0, 456.0, 101.0))
       self.UMLmodel.coords(new_obj.connectors[2],(465.0, 92.000000000000014, 465.0, 92.000000000000014))
       self.UMLmodel.coords(new_obj.connectors[3],(447.99999999999994, 92.000000000000014, 447.99999999999994, 92.000000000000014))
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
    self.obj442.graphObject_ = new_obj
    rootNode.addNode(self.obj442)
    self.globalAndLocalPostcondition(self.obj442, rootNode)

    self.globalPrecondition( rootNode )

    self.obj443=Basic(self)

    self.obj443.is_default.setValue((None, 0))
    self.obj443.is_default.config = 0
    self.obj443.name.setValue('Y')
    self.obj443.exit_action.setValue('\n\n')
    self.obj443.enter_action.setValue('\n\n')
    self.obj443.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(483.0,157.0,self.obj443)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(504.00000000000006, 160.0, 504.00000000000006, 160.0))
       self.UMLmodel.coords(new_obj.connectors[1],(504.00000000000006, 178.0, 504.00000000000006, 178.0))
       self.UMLmodel.coords(new_obj.connectors[2],(513.0, 169.0, 513.0, 169.0))
       self.UMLmodel.coords(new_obj.connectors[3],(496.0, 169.0, 496.0, 169.0))
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
    self.obj443.graphObject_ = new_obj
    rootNode.addNode(self.obj443)
    self.globalAndLocalPostcondition(self.obj443, rootNode)

    self.globalPrecondition( rootNode )

    self.obj444=Basic(self)

    self.obj444.is_default.setValue((None, 1))
    self.obj444.is_default.config = 0
    self.obj444.name.setValue('t1')
    self.obj444.exit_action.setValue('\n\n\n')
    self.obj444.enter_action.setValue('\n\n\n')
    self.obj444.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(625.0,80.0,self.obj444)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(646.0, 83.0, 646.0, 83.0))
       self.UMLmodel.coords(new_obj.connectors[1],(646.0, 101.00000000000001, 646.0, 101.00000000000001))
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
    self.obj444.graphObject_ = new_obj
    rootNode.addNode(self.obj444)
    self.globalAndLocalPostcondition(self.obj444, rootNode)

    self.globalPrecondition( rootNode )

    self.obj445=Basic(self)

    self.obj445.is_default.setValue((None, 0))
    self.obj445.is_default.config = 0
    self.obj445.name.setValue('t2')
    self.obj445.exit_action.setValue('\n\n')
    self.obj445.enter_action.setValue('\n\n')
    self.obj445.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(644.0,179.0,self.obj445)
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
    self.obj445.graphObject_ = new_obj
    rootNode.addNode(self.obj445)
    self.globalAndLocalPostcondition(self.obj445, rootNode)

    self.globalPrecondition( rootNode )

    self.obj446=Basic(self)

    self.obj446.is_default.setValue((None, 0))
    self.obj446.is_default.config = 0
    self.obj446.name.setValue('inactive')
    self.obj446.exit_action.setValue('\n\n')
    self.obj446.enter_action.setValue('\n\n')
    self.obj446.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(398.0,363.0,self.obj446)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(419.0, 366.0, 419.0, 366.0))
       self.UMLmodel.coords(new_obj.connectors[1],(419.0, 383.99999999999994, 419.0, 383.99999999999994))
       self.UMLmodel.coords(new_obj.connectors[2],(428.0, 375.0, 428.0, 375.0))
       self.UMLmodel.coords(new_obj.connectors[3],(411.0, 375.0, 411.0, 375.0))
       self.UMLmodel.coords(new_obj.gf3.handler,410.0,366.0,428.0,384.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,421.0,393.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='inactive')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj446.graphObject_ = new_obj
    rootNode.addNode(self.obj446)
    self.globalAndLocalPostcondition(self.obj446, rootNode)

    self.globalPrecondition( rootNode )

    self.obj447=History(self)

    self.obj447.is_default.setValue((None, 0))
    self.obj447.is_default.config = 0
    self.obj447.star.setValue((None, 0))
    self.obj447.star.config = 0
    self.obj447.name.setValue('')
    self.obj447.graphClass_= graph_History
    if self.genGraphics:
       from graph_History import *
       new_obj = graph_History(140.0,211.0,self.obj447)
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
    self.obj447.graphObject_ = new_obj
    rootNode.addNode(self.obj447)
    self.globalAndLocalPostcondition(self.obj447, rootNode)

    self.globalPrecondition( rootNode )

    self.obj448=Orthogonal(self)

    self.obj448.visible.setValue((None, 1))
    self.obj448.visible.config = 0
    self.obj448.name.setValue('O1')
    self.obj448.auto_adjust.setValue((None, 1))
    self.obj448.auto_adjust.config = 0
    self.obj448.graphClass_= graph_Orthogonal
    if self.genGraphics:
       from graph_Orthogonal import *
       new_obj = graph_Orthogonal(20.0,69.0,self.obj448)
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
    self.obj448.graphObject_ = new_obj
    rootNode.addNode(self.obj448)
    self.globalAndLocalPostcondition(self.obj448, rootNode)

    self.globalPrecondition( rootNode )

    self.obj449=Orthogonal(self)

    self.obj449.visible.setValue((None, 1))
    self.obj449.visible.config = 0
    self.obj449.name.setValue('O2')
    self.obj449.auto_adjust.setValue((None, 1))
    self.obj449.auto_adjust.config = 0
    self.obj449.graphClass_= graph_Orthogonal
    if self.genGraphics:
       from graph_Orthogonal import *
       new_obj = graph_Orthogonal(325.0,46.0,self.obj449)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Orthogonal", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(427.0, 138.0, 427.0, 138.0))
       self.UMLmodel.coords(new_obj.connectors[1],(575.0, 138.0, 575.0, 138.0))
       self.UMLmodel.coords(new_obj.connectors[2],(501.0, 77.0, 501.0, 77.0))
       self.UMLmodel.coords(new_obj.connectors[3],(501.0, 199.00000000000003, 501.0, 199.00000000000003))
       self.UMLmodel.coords(new_obj.gf5.handler,427.0,77.0,575.0,199.0)
       self.UMLmodel.itemconfig(new_obj.gf5.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, outline='DARKGRAY')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,427.0,70.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='O2')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj449.graphObject_ = new_obj
    rootNode.addNode(self.obj449)
    self.globalAndLocalPostcondition(self.obj449, rootNode)

    self.globalPrecondition( rootNode )

    self.obj450=Orthogonal(self)

    self.obj450.visible.setValue((None, 1))
    self.obj450.visible.config = 0
    self.obj450.name.setValue('O3')
    self.obj450.auto_adjust.setValue((None, 1))
    self.obj450.auto_adjust.config = 0
    self.obj450.graphClass_= graph_Orthogonal
    if self.genGraphics:
       from graph_Orthogonal import *
       new_obj = graph_Orthogonal(570.0,76.0,self.obj450)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Orthogonal", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(600.0, 149.0, 600.0, 149.0))
       self.UMLmodel.coords(new_obj.connectors[1],(748.0, 149.0, 748.0, 149.0))
       self.UMLmodel.coords(new_obj.connectors[2],(674.0, 77.0, 674.0, 77.0))
       self.UMLmodel.coords(new_obj.connectors[3],(674.0, 220.99999999999997, 674.0, 220.99999999999997))
       self.UMLmodel.coords(new_obj.gf5.handler,600.0,77.0,748.0,221.0)
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
    self.obj450.graphObject_ = new_obj
    rootNode.addNode(self.obj450)
    self.globalAndLocalPostcondition(self.obj450, rootNode)

    self.globalPrecondition( rootNode )

    self.obj451=contains(self)

    self.obj451.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(106.5,138.0,self.obj451)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj451.graphObject_ = new_obj
    rootNode.addNode(self.obj451)
    self.globalAndLocalPostcondition(self.obj451, rootNode)

    self.globalPrecondition( rootNode )

    self.obj452=contains(self)

    self.obj452.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(165.0,138.5,self.obj452)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj452.graphObject_ = new_obj
    rootNode.addNode(self.obj452)
    self.globalAndLocalPostcondition(self.obj452, rootNode)

    self.globalPrecondition( rootNode )

    self.obj453=contains(self)

    self.obj453.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(-3.5,106.5,self.obj453)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj453.graphObject_ = new_obj
    rootNode.addNode(self.obj453)
    self.globalAndLocalPostcondition(self.obj453, rootNode)

    self.globalPrecondition( rootNode )

    self.obj454=contains(self)

    self.obj454.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(157.0,135.0,self.obj454)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj454.graphObject_ = new_obj
    rootNode.addNode(self.obj454)
    self.globalAndLocalPostcondition(self.obj454, rootNode)

    self.globalPrecondition( rootNode )

    self.obj455=contains(self)

    self.obj455.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(271.5,51.5,self.obj455)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj455.graphObject_ = new_obj
    rootNode.addNode(self.obj455)
    self.globalAndLocalPostcondition(self.obj455, rootNode)

    self.globalPrecondition( rootNode )

    self.obj456=contains(self)

    self.obj456.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(295.5,90.0,self.obj456)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj456.graphObject_ = new_obj
    rootNode.addNode(self.obj456)
    self.globalAndLocalPostcondition(self.obj456, rootNode)

    self.globalPrecondition( rootNode )

    self.obj457=contains(self)

    self.obj457.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(174.0,166.5,self.obj457)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj457.graphObject_ = new_obj
    rootNode.addNode(self.obj457)
    self.globalAndLocalPostcondition(self.obj457, rootNode)

    self.globalPrecondition( rootNode )

    self.obj458=contains(self)

    self.obj458.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(579.0,90.5,self.obj458)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj458.graphObject_ = new_obj
    rootNode.addNode(self.obj458)
    self.globalAndLocalPostcondition(self.obj458, rootNode)

    self.globalPrecondition( rootNode )

    self.obj459=contains(self)

    self.obj459.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(588.5,140.0,self.obj459)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj459.graphObject_ = new_obj
    rootNode.addNode(self.obj459)
    self.globalAndLocalPostcondition(self.obj459, rootNode)

    self.globalPrecondition( rootNode )

    self.obj460=Hyperedge(self)

    self.obj460.name.setValue('')
    self.obj460.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj460.guard.setValue('1')
    self.obj460.trigger.setValue('e1')
    self.obj460.action.setValue('[DUMP("triggered by e1")]\n')
    self.obj460.broadcast_to.setValue('')
    self.obj460.display.setValue('e1')
    self.obj460.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(181.5,120.5,self.obj460)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj460.graphObject_ = new_obj
    rootNode.addNode(self.obj460)
    self.globalAndLocalPostcondition(self.obj460, rootNode)

    self.globalPrecondition( rootNode )

    self.obj461=Hyperedge(self)

    self.obj461.name.setValue('')
    self.obj461.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj461.guard.setValue('1')
    self.obj461.trigger.setValue('e2')
    self.obj461.action.setValue('[DUMP("triggered by e2")]\n')
    self.obj461.broadcast_to.setValue('')
    self.obj461.display.setValue('e2')
    self.obj461.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(188.5,192.5,self.obj461)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj461.graphObject_ = new_obj
    rootNode.addNode(self.obj461)
    self.globalAndLocalPostcondition(self.obj461, rootNode)

    self.globalPrecondition( rootNode )

    self.obj462=Hyperedge(self)

    self.obj462.name.setValue('')
    self.obj462.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n\n')
    self.obj462.guard.setValue('1')
    self.obj462.trigger.setValue('e3')
    self.obj462.action.setValue('\n\n')
    self.obj462.broadcast_to.setValue('')
    self.obj462.display.setValue('e3')
    self.obj462.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(309.0,191.5,self.obj462)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj462.graphObject_ = new_obj
    rootNode.addNode(self.obj462)
    self.globalAndLocalPostcondition(self.obj462, rootNode)

    self.globalPrecondition( rootNode )

    self.obj463=Hyperedge(self)

    self.obj463.name.setValue('')
    self.obj463.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj463.guard.setValue('1')
    self.obj463.trigger.setValue('AFTER(1)')
    self.obj463.action.setValue('\n')
    self.obj463.broadcast_to.setValue('')
    self.obj463.display.setValue('tm(1)')
    self.obj463.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(527.0,113.5,self.obj463)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj463.graphObject_ = new_obj
    rootNode.addNode(self.obj463)
    self.globalAndLocalPostcondition(self.obj463, rootNode)

    self.globalPrecondition( rootNode )

    self.obj464=Hyperedge(self)

    self.obj464.name.setValue('')
    self.obj464.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj464.guard.setValue('1')
    self.obj464.trigger.setValue('AFTER(2)')
    self.obj464.action.setValue('\n')
    self.obj464.broadcast_to.setValue('')
    self.obj464.display.setValue('tm(2)')
    self.obj464.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(435.0,151.5,self.obj464)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj464.graphObject_ = new_obj
    rootNode.addNode(self.obj464)
    self.globalAndLocalPostcondition(self.obj464, rootNode)

    self.globalPrecondition( rootNode )

    self.obj465=Hyperedge(self)

    self.obj465.name.setValue('')
    self.obj465.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj465.guard.setValue('1')
    self.obj465.trigger.setValue('back')
    self.obj465.action.setValue('\n')
    self.obj465.broadcast_to.setValue('')
    self.obj465.display.setValue('back')
    self.obj465.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(202.5,83.5,self.obj465)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj465.graphObject_ = new_obj
    rootNode.addNode(self.obj465)
    self.globalAndLocalPostcondition(self.obj465, rootNode)

    self.globalPrecondition( rootNode )

    self.obj466=Hyperedge(self)

    self.obj466.name.setValue('')
    self.obj466.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj466.guard.setValue('1')
    self.obj466.trigger.setValue('hist')
    self.obj466.action.setValue('\n')
    self.obj466.broadcast_to.setValue('')
    self.obj466.display.setValue('hist')
    self.obj466.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(361.0,231.5,self.obj466)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj466.graphObject_ = new_obj
    rootNode.addNode(self.obj466)
    self.globalAndLocalPostcondition(self.obj466, rootNode)

    self.globalPrecondition( rootNode )

    self.obj467=Hyperedge(self)

    self.obj467.name.setValue('')
    self.obj467.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj467.guard.setValue('1')
    self.obj467.trigger.setValue('AFTER(0.5)')
    self.obj467.action.setValue('\n')
    self.obj467.broadcast_to.setValue('')
    self.obj467.display.setValue('tm(0.5)')
    self.obj467.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(607.5,135.5,self.obj467)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj467.graphObject_ = new_obj
    rootNode.addNode(self.obj467)
    self.globalAndLocalPostcondition(self.obj467, rootNode)

    self.globalPrecondition( rootNode )

    self.obj468=Hyperedge(self)

    self.obj468.name.setValue('')
    self.obj468.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj468.guard.setValue('1')
    self.obj468.trigger.setValue('AFTER(0.5)')
    self.obj468.action.setValue('\n')
    self.obj468.broadcast_to.setValue('')
    self.obj468.display.setValue('tm(0.5)')
    self.obj468.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(694.5,125.5,self.obj468)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj468.graphObject_ = new_obj
    rootNode.addNode(self.obj468)
    self.globalAndLocalPostcondition(self.obj468, rootNode)

    self.globalPrecondition( rootNode )

    self.obj469=Hyperedge(self)

    self.obj469.name.setValue('')
    self.obj469.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj469.guard.setValue('1')
    self.obj469.trigger.setValue('activate')
    self.obj469.action.setValue('\n')
    self.obj469.broadcast_to.setValue('')
    self.obj469.display.setValue('activate')
    self.obj469.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(419.5,337.5,self.obj469)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj469.graphObject_ = new_obj
    rootNode.addNode(self.obj469)
    self.globalAndLocalPostcondition(self.obj469, rootNode)

    self.globalPrecondition( rootNode )

    self.obj470=Hyperedge(self)

    self.obj470.name.setValue('')
    self.obj470.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj470.guard.setValue('1')
    self.obj470.trigger.setValue('deactivate')
    self.obj470.action.setValue('\n')
    self.obj470.broadcast_to.setValue('')
    self.obj470.display.setValue('deactivate')
    self.obj470.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(17.5,168.5,self.obj470)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj470.graphObject_ = new_obj
    rootNode.addNode(self.obj470)
    self.globalAndLocalPostcondition(self.obj470, rootNode)

    self.globalPrecondition( rootNode )

    self.obj471=orthogonality(self)

    self.obj471.graphClass_= graph_orthogonality
    if self.genGraphics:
       from graph_orthogonality import *
       new_obj = graph_orthogonality(92.0,66.5,self.obj471)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("orthogonality", new_obj.tag)
    else: new_obj = None
    self.obj471.graphObject_ = new_obj
    rootNode.addNode(self.obj471)
    self.globalAndLocalPostcondition(self.obj471, rootNode)

    self.globalPrecondition( rootNode )

    self.obj472=orthogonality(self)

    self.obj472.graphClass_= graph_orthogonality
    if self.genGraphics:
       from graph_orthogonality import *
       new_obj = graph_orthogonality(255.5,76.0,self.obj472)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("orthogonality", new_obj.tag)
    else: new_obj = None
    self.obj472.graphObject_ = new_obj
    rootNode.addNode(self.obj472)
    self.globalAndLocalPostcondition(self.obj472, rootNode)

    self.globalPrecondition( rootNode )

    self.obj473=orthogonality(self)

    self.obj473.graphClass_= graph_orthogonality
    if self.genGraphics:
       from graph_orthogonality import *
       new_obj = graph_orthogonality(343.5,70.0,self.obj473)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("orthogonality", new_obj.tag)
    else: new_obj = None
    self.obj473.graphObject_ = new_obj
    rootNode.addNode(self.obj473)
    self.globalAndLocalPostcondition(self.obj473, rootNode)
    self.drawConnections((self.obj437,self.obj451,[113.0, 191.0, 106.5, 138.0], 0, 2), (self.obj437,self.obj452,[198.99999999999997, 113.0, 165.0, 138.5], 0, 2), (self.obj437,self.obj462,[285.0, 191.0, 309.0, 191.5], 0, 2), (self.obj437,self.obj457,[198.99999999999997, 270.0, 174.0, 166.5], 0, 2), (self.obj438,self.obj471,[85.0, 170.0, 92.0, 66.5], 0, 2), (self.obj438,self.obj472,[420.0, 57.0, 255.5, 76.0], 0, 2), (self.obj438,self.obj473,[420.0, 57.0, 343.5, 70.0], 0, 2), (self.obj438,self.obj470,[85.0, 170.0, 17.5, 168.5], 0, 2), (self.obj439,self.obj460,[137.0, 159.0, 181.5, 120.5], 0, 2), (self.obj440,self.obj461,[261.0, 161.0, 188.5, 192.49999999999997], 0, 2), (self.obj441,self.obj465,[373.0, 182.0, 364.0, 85.0, 202.5, 83.5], 0, 3), (self.obj441,self.obj466,[373.0, 200.0, 361.0, 231.5], 0, 2), (self.obj442,self.obj463,[465.00000000000006, 92.0, 527.0, 113.49999999999999], 0, 2), (self.obj443,self.obj464,[496.0, 169.0, 434.99999999999994, 151.5], 0, 2), (self.obj444,self.obj467,[638.0, 92.0, 607.5, 135.5], 0, 2), (self.obj445,self.obj468,[674.0, 191.0, 694.5, 125.5], 0, 2), (self.obj446,self.obj469,[419.0, 366.0, 419.5, 337.5], 0, 2), (self.obj448,self.obj453,[395.0, 176.0, -3.4999999999999996, 106.5], 0, 2), (self.obj448,self.obj454,[247.0, 76.0, 157.0, 135.0], 0, 2), (self.obj449,self.obj455,[561.0, 138.0, 271.5, 51.5], 0, 2), (self.obj449,self.obj456,[427.0, 138.0, 295.5, 90.0], 0, 2), (self.obj450,self.obj458,[748.0, 149.0, 579.0, 90.5], 0, 2), (self.obj450,self.obj459,[674.0, 221.0, 588.5, 140.0], 0, 2), (self.obj451,self.obj439,[106.5, 138.0, 128.0, 150.0], 0, 2), (self.obj452,self.obj440,[165.0, 138.5, 261.0, 161.0], 0, 2), (self.obj453,self.obj437,[-3.4999999999999996, 106.5, 113.0, 191.0], 0, 2), (self.obj454,self.obj441,[157.0, 135.0, 365.0, 191.0], 0, 2), (self.obj455,self.obj442,[271.5, 51.5, 447.99999999999994, 92.0], 0, 2), (self.obj456,self.obj443,[295.5, 90.0, 496.0, 169.0], 0, 2), (self.obj457,self.obj447,[174.0, 166.5, 144.0, 232.99999999999997], 0, 2), (self.obj458,self.obj444,[579.0, 90.5, 646.0, 100.99999999999999], 0, 2), (self.obj459,self.obj445,[588.5, 140.0, 665.0, 182.0], 0, 2), (self.obj460,self.obj440,[181.5, 120.5, 261.0, 161.0], 0, 2), (self.obj461,self.obj439,[188.5, 192.49999999999997, 137.0, 159.0], 0, 2), (self.obj462,self.obj441,[309.0, 191.5, 365.0, 191.0], 0, 2), (self.obj463,self.obj443,[527.0, 113.49999999999999, 513.0, 169.0], 0, 2), (self.obj464,self.obj442,[434.99999999999994, 151.5, 447.99999999999994, 92.0], 0, 2), (self.obj465,self.obj437,[202.5, 83.5, 198.99999999999997, 113.0], 0, 2), (self.obj466,self.obj447,[361.0, 231.5, 179.0, 232.0], 0, 2), (self.obj467,self.obj445,[607.5, 135.5, 657.0, 191.0], 0, 2), (self.obj468,self.obj444,[694.5, 125.5, 655.0, 92.0], 0, 2), (self.obj469,self.obj438,[419.5, 337.5, 420.0, 284.0], 0, 2), (self.obj470,self.obj446,[17.5, 168.5, 18.0, 375.0, 411.0, 375.0], 0, 3), (self.obj471,self.obj448,[92.0, 66.5, 99.0, 176.0], 0, 2), (self.obj472,self.obj449,[255.5, 76.0, 427.0, 138.0], 0, 2), (self.obj473,self.obj450,[343.5, 70.0, 600.0, 149.0], 0, 2) )

newfunction = m7_DCharts_mdl

loadedMMName = 'DCharts'
