from graph_ASG_ERmetaMetaModel import *
from stickylink import *
from widthXfillXdecoration import *
from ASG_Statechart import *
from ASG_Statechart import *
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

def testsvm(self, rootNode):

    self.globalPrecondition( rootNode )

    self.obj28=Composite(self)

    self.obj28.auto_adjust.setValue((None, 1))
    self.obj28.auto_adjust.config = 0
    self.obj28.name.setValue('A')
    self.obj28.is_default.setValue((None, 1))
    self.obj28.is_default.config = 0
    self.obj28.visible.setValue((None, 1))
    self.obj28.visible.config = 0
    self.obj28.exit_action.setValue('[DUMP("Leave A state")]\n')
    self.obj28.enter_action.setValue('[DUMP("Welcome to A state")]\n')
    self.obj28.graphClass_= graph_Composite
    if self.genGraphics:
       from graph_Composite import *
       new_obj = graph_Composite(108.0,202.0,self.obj28)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Composite", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(91.0, 201.0, 91.0, 201.0))
       self.UMLmodel.coords(new_obj.connectors[1],(471.99999999999994, 201.0, 471.99999999999994, 201.0))
       self.UMLmodel.coords(new_obj.connectors[2],(281.0, 50.0, 281.0, 50.0))
       self.UMLmodel.coords(new_obj.connectors[3],(281.0, 352.0, 281.0, 352.0))
       self.UMLmodel.coords(new_obj.gf2.handler,91.0,50.0,472.0,352.0)
       self.UMLmodel.itemconfig(new_obj.gf2.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,91.0,43.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='A')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj28.graphObject_ = new_obj
    rootNode.addNode(self.obj28)
    self.globalAndLocalPostcondition(self.obj28, rootNode)

    self.globalPrecondition( rootNode )

    self.obj29=Composite(self)

    self.obj29.auto_adjust.setValue((None, 1))
    self.obj29.auto_adjust.config = 0
    self.obj29.name.setValue('B')
    self.obj29.is_default.setValue((None, 1))
    self.obj29.is_default.config = 0
    self.obj29.visible.setValue((None, 1))
    self.obj29.visible.config = 0
    self.obj29.exit_action.setValue('[DUMP("Leave B state")]\n')
    self.obj29.enter_action.setValue('[DUMP("Welcome to B state")]\n')
    self.obj29.graphClass_= graph_Composite
    if self.genGraphics:
       from graph_Composite import *
       new_obj = graph_Composite(122.0,49.0,self.obj29)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Composite", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(102.0, 147.0, 102.0, 147.0))
       self.UMLmodel.coords(new_obj.connectors[1],(283.0, 147.0, 283.0, 147.0))
       self.UMLmodel.coords(new_obj.connectors[2],(192.0, 103.0, 192.0, 103.0))
       self.UMLmodel.coords(new_obj.connectors[3],(192.0, 192.0, 192.0, 192.0))
       self.UMLmodel.coords(new_obj.gf2.handler,102.0,103.0,283.0,192.0)
       self.UMLmodel.itemconfig(new_obj.gf2.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,102.0,96.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='B')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj29.graphObject_ = new_obj
    rootNode.addNode(self.obj29)
    self.globalAndLocalPostcondition(self.obj29, rootNode)

    self.globalPrecondition( rootNode )

    self.obj30=Composite(self)

    self.obj30.auto_adjust.setValue((None, 1))
    self.obj30.auto_adjust.config = 0
    self.obj30.name.setValue('F')
    self.obj30.is_default.setValue((None, 0))
    self.obj30.is_default.config = 0
    self.obj30.visible.setValue((None, 1))
    self.obj30.visible.config = 0
    self.obj30.exit_action.setValue('\n')
    self.obj30.enter_action.setValue('\n')
    self.obj30.graphClass_= graph_Composite
    if self.genGraphics:
       from graph_Composite import *
       new_obj = graph_Composite(71.0,278.0,self.obj30)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Composite", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(101.0, 289.0, 101.0, 289.0))
       self.UMLmodel.coords(new_obj.connectors[1],(464.99999999999994, 289.0, 464.99999999999994, 289.0))
       self.UMLmodel.coords(new_obj.connectors[2],(283.0, 232.99999999999997, 283.0, 232.99999999999997))
       self.UMLmodel.coords(new_obj.connectors[3],(283.0, 345.0, 283.0, 345.0))
       self.UMLmodel.coords(new_obj.gf2.handler,101.0,233.0,465.0,345.0)
       self.UMLmodel.itemconfig(new_obj.gf2.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,101.0,226.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='F')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj30.graphObject_ = new_obj
    rootNode.addNode(self.obj30)
    self.globalAndLocalPostcondition(self.obj30, rootNode)

    self.globalPrecondition( rootNode )

    self.obj31=Basic(self)

    self.obj31.is_default.setValue((None, 0))
    self.obj31.is_default.config = 0
    self.obj31.name.setValue('E')
    self.obj31.exit_action.setValue('\n\n')
    self.obj31.enter_action.setValue('\n\n')
    self.obj31.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(246.0,109.0,self.obj31)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(267.0, 111.99999999999999, 267.0, 111.99999999999999))
       self.UMLmodel.coords(new_obj.connectors[1],(267.0, 130.0, 267.0, 130.0))
       self.UMLmodel.coords(new_obj.connectors[2],(276.0, 120.99999999999999, 276.0, 120.99999999999999))
       self.UMLmodel.coords(new_obj.connectors[3],(259.0, 120.99999999999999, 259.0, 120.99999999999999))
       self.UMLmodel.coords(new_obj.gf3.handler,258.0,112.0,276.0,130.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,269.0,139.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='E')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj31.graphObject_ = new_obj
    rootNode.addNode(self.obj31)
    self.globalAndLocalPostcondition(self.obj31, rootNode)

    self.globalPrecondition( rootNode )

    self.obj32=Basic(self)

    self.obj32.is_default.setValue((None, 1))
    self.obj32.is_default.config = 0
    self.obj32.name.setValue('C')
    self.obj32.exit_action.setValue('\n\n\n')
    self.obj32.enter_action.setValue('\n\n\n')
    self.obj32.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(96.0,106.0,self.obj32)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(116.99999999999999, 108.99999999999999, 116.99999999999999, 108.99999999999999))
       self.UMLmodel.coords(new_obj.connectors[1],(116.99999999999999, 126.99999999999999, 116.99999999999999, 126.99999999999999))
       self.UMLmodel.coords(new_obj.connectors[2],(125.99999999999999, 117.99999999999999, 125.99999999999999, 117.99999999999999))
       self.UMLmodel.coords(new_obj.connectors[3],(108.99999999999999, 117.99999999999999, 108.99999999999999, 117.99999999999999))
       self.UMLmodel.coords(new_obj.gf3.handler,108.0,109.0,126.0,127.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,119.0,136.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='C')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj32.graphObject_ = new_obj
    rootNode.addNode(self.obj32)
    self.globalAndLocalPostcondition(self.obj32, rootNode)

    self.globalPrecondition( rootNode )

    self.obj33=Basic(self)

    self.obj33.is_default.setValue((None, 0))
    self.obj33.is_default.config = 0
    self.obj33.name.setValue('D')
    self.obj33.exit_action.setValue('\n\n')
    self.obj33.enter_action.setValue('\n\n')
    self.obj33.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(167.0,150.0,self.obj33)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(188.0, 153.0, 188.0, 153.0))
       self.UMLmodel.coords(new_obj.connectors[1],(188.0, 171.0, 188.0, 171.0))
       self.UMLmodel.coords(new_obj.connectors[2],(197.0, 162.0, 197.0, 162.0))
       self.UMLmodel.coords(new_obj.connectors[3],(180.0, 162.0, 180.0, 162.0))
       self.UMLmodel.coords(new_obj.gf3.handler,179.0,153.0,197.0,171.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,190.0,180.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='D')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj33.graphObject_ = new_obj
    rootNode.addNode(self.obj33)
    self.globalAndLocalPostcondition(self.obj33, rootNode)

    self.globalPrecondition( rootNode )

    self.obj34=Basic(self)

    self.obj34.is_default.setValue((None, 0))
    self.obj34.is_default.config = 0
    self.obj34.name.setValue('G')
    self.obj34.exit_action.setValue('\n\n\n')
    self.obj34.enter_action.setValue('\n\n\n')
    self.obj34.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(549.0,188.0,self.obj34)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(570.0, 191.0, 570.0, 191.0))
       self.UMLmodel.coords(new_obj.connectors[1],(570.0, 209.0, 570.0, 209.0))
       self.UMLmodel.coords(new_obj.connectors[2],(579.0, 200.0, 579.0, 200.0))
       self.UMLmodel.coords(new_obj.connectors[3],(562.0, 200.0, 562.0, 200.0))
       self.UMLmodel.coords(new_obj.gf3.handler,561.0,191.0,579.0,209.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,572.0,218.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='G')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj34.graphObject_ = new_obj
    rootNode.addNode(self.obj34)
    self.globalAndLocalPostcondition(self.obj34, rootNode)

    self.globalPrecondition( rootNode )

    self.obj35=Basic(self)

    self.obj35.is_default.setValue((None, 1))
    self.obj35.is_default.config = 0
    self.obj35.name.setValue('F1a')
    self.obj35.exit_action.setValue('\n\n')
    self.obj35.enter_action.setValue('\n\n')
    self.obj35.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(108.0,295.0,self.obj35)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(129.0, 298.0, 129.0, 298.0))
       self.UMLmodel.coords(new_obj.connectors[1],(129.0, 316.0, 129.0, 316.0))
       self.UMLmodel.coords(new_obj.connectors[2],(138.0, 307.0, 138.0, 307.0))
       self.UMLmodel.coords(new_obj.connectors[3],(120.99999999999999, 307.0, 120.99999999999999, 307.0))
       self.UMLmodel.coords(new_obj.gf3.handler,120.0,298.0,138.0,316.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,131.0,325.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='F1a')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj35.graphObject_ = new_obj
    rootNode.addNode(self.obj35)
    self.globalAndLocalPostcondition(self.obj35, rootNode)

    self.globalPrecondition( rootNode )

    self.obj36=Basic(self)

    self.obj36.is_default.setValue((None, 0))
    self.obj36.is_default.config = 0
    self.obj36.name.setValue('F1b')
    self.obj36.exit_action.setValue('\n\n')
    self.obj36.enter_action.setValue('\n\n')
    self.obj36.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(220.0,296.0,self.obj36)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(240.99999999999997, 299.0, 240.99999999999997, 299.0))
       self.UMLmodel.coords(new_obj.connectors[1],(240.99999999999997, 317.0, 240.99999999999997, 317.0))
       self.UMLmodel.coords(new_obj.connectors[2],(249.99999999999997, 308.0, 249.99999999999997, 308.0))
       self.UMLmodel.coords(new_obj.connectors[3],(232.99999999999997, 308.0, 232.99999999999997, 308.0))
       self.UMLmodel.coords(new_obj.gf3.handler,232.0,299.0,250.0,317.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,243.0,326.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='F1b')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj36.graphObject_ = new_obj
    rootNode.addNode(self.obj36)
    self.globalAndLocalPostcondition(self.obj36, rootNode)

    self.globalPrecondition( rootNode )

    self.obj37=Basic(self)

    self.obj37.is_default.setValue((None, 1))
    self.obj37.is_default.config = 0
    self.obj37.name.setValue('F2a')
    self.obj37.exit_action.setValue('\n\n')
    self.obj37.enter_action.setValue('\n\n')
    self.obj37.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(262.0,296.0,self.obj37)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(283.0, 299.0, 283.0, 299.0))
       self.UMLmodel.coords(new_obj.connectors[1],(283.0, 317.0, 283.0, 317.0))
       self.UMLmodel.coords(new_obj.connectors[2],(292.0, 308.0, 292.0, 308.0))
       self.UMLmodel.coords(new_obj.connectors[3],(275.0, 308.0, 275.0, 308.0))
       self.UMLmodel.coords(new_obj.gf3.handler,274.0,299.0,292.0,317.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,285.0,326.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='F2a')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj37.graphObject_ = new_obj
    rootNode.addNode(self.obj37)
    self.globalAndLocalPostcondition(self.obj37, rootNode)

    self.globalPrecondition( rootNode )

    self.obj38=Basic(self)

    self.obj38.is_default.setValue((None, 0))
    self.obj38.is_default.config = 0
    self.obj38.name.setValue('F2b')
    self.obj38.exit_action.setValue('\n\n')
    self.obj38.enter_action.setValue('\n\n')
    self.obj38.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(375.0,296.0,self.obj38)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(396.0, 299.0, 396.0, 299.0))
       self.UMLmodel.coords(new_obj.connectors[1],(396.0, 317.0, 396.0, 317.0))
       self.UMLmodel.coords(new_obj.connectors[2],(405.0, 308.0, 405.0, 308.0))
       self.UMLmodel.coords(new_obj.connectors[3],(388.0, 308.0, 388.0, 308.0))
       self.UMLmodel.coords(new_obj.gf3.handler,387.0,299.0,405.0,317.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,398.0,326.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='F2b')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj38.graphObject_ = new_obj
    rootNode.addNode(self.obj38)
    self.globalAndLocalPostcondition(self.obj38, rootNode)

    self.globalPrecondition( rootNode )

    self.obj39=History(self)

    self.obj39.is_default.setValue((None, 0))
    self.obj39.is_default.config = 0
    self.obj39.star.setValue((None, 1))
    self.obj39.star.config = 0
    self.obj39.name.setValue('')
    self.obj39.graphClass_= graph_History
    if self.genGraphics:
       from graph_History import *
       new_obj = graph_History(191.0,53.0,self.obj39)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("History", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(213.0, 55.999999999999993, 213.0, 55.999999999999993))
       self.UMLmodel.coords(new_obj.connectors[1],(229.99999999999997, 74.0, 229.99999999999997, 74.0))
       self.UMLmodel.coords(new_obj.connectors[2],(213.0, 91.0, 213.0, 91.0))
       self.UMLmodel.coords(new_obj.connectors[3],(195.0, 75.0, 195.0, 75.0))
       self.UMLmodel.coords(new_obj.gf0.handler,195.0,56.0,231.0,91.0)
       self.UMLmodel.itemconfig(new_obj.gf0.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf0.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf0.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf0.handler, fill='lightblue')
       self.UMLmodel.coords(new_obj.gf1.handler,212.0,75.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='H')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       self.UMLmodel.coords(new_obj.gf2.handler,220.0,75.0)
       self.UMLmodel.itemconfig(new_obj.gf2.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, text='*')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, justify='left')
       self.UMLmodel.coords(new_obj.gf3.handler,214.0,100.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='blue')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, text='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, justify='left')
    else: new_obj = None
    self.obj39.graphObject_ = new_obj
    rootNode.addNode(self.obj39)
    self.globalAndLocalPostcondition(self.obj39, rootNode)

    self.globalPrecondition( rootNode )

    self.obj40=Orthogonal(self)

    self.obj40.visible.setValue((None, 1))
    self.obj40.visible.config = 0
    self.obj40.name.setValue('F1')
    self.obj40.auto_adjust.setValue((None, 1))
    self.obj40.auto_adjust.config = 0
    self.obj40.graphClass_= graph_Orthogonal
    if self.genGraphics:
       from graph_Orthogonal import *
       new_obj = graph_Orthogonal(102.0,259.0,self.obj40)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Orthogonal", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(113.99999999999999, 295.0, 113.99999999999999, 295.0))
       self.UMLmodel.coords(new_obj.connectors[1],(260.0, 295.0, 260.0, 295.0))
       self.UMLmodel.coords(new_obj.connectors[2],(187.0, 251.99999999999997, 187.0, 251.99999999999997))
       self.UMLmodel.coords(new_obj.connectors[3],(187.0, 338.0, 187.0, 338.0))
       self.UMLmodel.coords(new_obj.gf5.handler,114.0,252.0,260.0,338.0)
       self.UMLmodel.itemconfig(new_obj.gf5.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, outline='DARKGRAY')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,114.0,245.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='F1')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj40.graphObject_ = new_obj
    rootNode.addNode(self.obj40)
    self.globalAndLocalPostcondition(self.obj40, rootNode)

    self.globalPrecondition( rootNode )

    self.obj41=Orthogonal(self)

    self.obj41.visible.setValue((None, 1))
    self.obj41.visible.config = 0
    self.obj41.name.setValue('F2')
    self.obj41.auto_adjust.setValue((None, 1))
    self.obj41.auto_adjust.config = 0
    self.obj41.graphClass_= graph_Orthogonal
    if self.genGraphics:
       from graph_Orthogonal import *
       new_obj = graph_Orthogonal(309.0,284.0,self.obj41)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Orthogonal", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(268.0, 295.0, 268.0, 295.0))
       self.UMLmodel.coords(new_obj.connectors[1],(457.99999999999994, 295.0, 457.99999999999994, 295.0))
       self.UMLmodel.coords(new_obj.connectors[2],(363.0, 251.99999999999997, 363.0, 251.99999999999997))
       self.UMLmodel.coords(new_obj.connectors[3],(363.0, 338.0, 363.0, 338.0))
       self.UMLmodel.coords(new_obj.gf5.handler,268.0,252.0,458.0,338.0)
       self.UMLmodel.itemconfig(new_obj.gf5.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, outline='DARKGRAY')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,268.0,245.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='F2')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj41.graphObject_ = new_obj
    rootNode.addNode(self.obj41)
    self.globalAndLocalPostcondition(self.obj41, rootNode)

    self.globalPrecondition( rootNode )

    self.obj42=contains(self)

    self.obj42.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(190.0,283.5,self.obj42)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj42.graphObject_ = new_obj
    rootNode.addNode(self.obj42)
    self.globalAndLocalPostcondition(self.obj42, rootNode)

    self.globalPrecondition( rootNode )

    self.obj43=contains(self)

    self.obj43.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(190.0,54.5,self.obj43)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj43.graphObject_ = new_obj
    rootNode.addNode(self.obj43)
    self.globalAndLocalPostcondition(self.obj43, rootNode)

    self.globalPrecondition( rootNode )

    self.obj44=contains(self)

    self.obj44.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(114.5,-15.0,self.obj44)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj44.graphObject_ = new_obj
    rootNode.addNode(self.obj44)
    self.globalAndLocalPostcondition(self.obj44, rootNode)

    self.globalPrecondition( rootNode )

    self.obj45=contains(self)

    self.obj45.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(153.0,-52.5,self.obj45)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj45.graphObject_ = new_obj
    rootNode.addNode(self.obj45)
    self.globalAndLocalPostcondition(self.obj45, rootNode)

    self.globalPrecondition( rootNode )

    self.obj46=contains(self)

    self.obj46.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(78.5,168.0,self.obj46)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj46.graphObject_ = new_obj
    rootNode.addNode(self.obj46)
    self.globalAndLocalPostcondition(self.obj46, rootNode)

    self.globalPrecondition( rootNode )

    self.obj47=contains(self)

    self.obj47.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(73.0,279.0,self.obj47)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj47.graphObject_ = new_obj
    rootNode.addNode(self.obj47)
    self.globalAndLocalPostcondition(self.obj47, rootNode)

    self.globalPrecondition( rootNode )

    self.obj48=contains(self)

    self.obj48.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(93.0,256.0,self.obj48)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj48.graphObject_ = new_obj
    rootNode.addNode(self.obj48)
    self.globalAndLocalPostcondition(self.obj48, rootNode)

    self.globalPrecondition( rootNode )

    self.obj49=contains(self)

    self.obj49.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(154.0,284.0,self.obj49)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj49.graphObject_ = new_obj
    rootNode.addNode(self.obj49)
    self.globalAndLocalPostcondition(self.obj49, rootNode)

    self.globalPrecondition( rootNode )

    self.obj50=contains(self)

    self.obj50.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(314.5,294.0,self.obj50)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj50.graphObject_ = new_obj
    rootNode.addNode(self.obj50)
    self.globalAndLocalPostcondition(self.obj50, rootNode)

    self.globalPrecondition( rootNode )

    self.obj51=contains(self)

    self.obj51.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(339.0,309.0,self.obj51)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj51.graphObject_ = new_obj
    rootNode.addNode(self.obj51)
    self.globalAndLocalPostcondition(self.obj51, rootNode)

    self.globalPrecondition( rootNode )

    self.obj52=Hyperedge(self)

    self.obj52.name.setValue('')
    self.obj52.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n\n\n')
    self.obj52.guard.setValue('1')
    self.obj52.trigger.setValue('to A')
    self.obj52.action.setValue('[DUMP("Go back to default substate of A")]\n\n')
    self.obj52.broadcast_to.setValue('')
    self.obj52.display.setValue('to A')
    self.obj52.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(514.0,200.5,self.obj52)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj52.graphObject_ = new_obj
    rootNode.addNode(self.obj52)
    self.globalAndLocalPostcondition(self.obj52, rootNode)

    self.globalPrecondition( rootNode )

    self.obj53=Hyperedge(self)

    self.obj53.name.setValue('')
    self.obj53.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n\n\n\n')
    self.obj53.guard.setValue('1')
    self.obj53.trigger.setValue('to HS')
    self.obj53.action.setValue('[DUMP("Go back to history state of A")]\n\n')
    self.obj53.broadcast_to.setValue('')
    self.obj53.display.setValue('to HS')
    self.obj53.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(400.5,73.5,self.obj53)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj53.graphObject_ = new_obj
    rootNode.addNode(self.obj53)
    self.globalAndLocalPostcondition(self.obj53, rootNode)

    self.globalPrecondition( rootNode )

    self.obj54=Hyperedge(self)

    self.obj54.name.setValue('')
    self.obj54.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n\n\n\n')
    self.obj54.guard.setValue('1')
    self.obj54.trigger.setValue('to D')
    self.obj54.action.setValue('[DUMP("Now we are in D")]\n[EVENT("to E")]\n\n\n')
    self.obj54.broadcast_to.setValue('')
    self.obj54.display.setValue('to D')
    self.obj54.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(137.0,134.5,self.obj54)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj54.graphObject_ = new_obj
    rootNode.addNode(self.obj54)
    self.globalAndLocalPostcondition(self.obj54, rootNode)

    self.globalPrecondition( rootNode )

    self.obj55=Hyperedge(self)

    self.obj55.name.setValue('')
    self.obj55.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n\n\n\n')
    self.obj55.guard.setValue('1')
    self.obj55.trigger.setValue('to E')
    self.obj55.action.setValue('[DUMP("Immediately go to E")]\n\n')
    self.obj55.broadcast_to.setValue('')
    self.obj55.display.setValue('to E')
    self.obj55.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(227.0,146.0,self.obj55)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj55.graphObject_ = new_obj
    rootNode.addNode(self.obj55)
    self.globalAndLocalPostcondition(self.obj55, rootNode)

    self.globalPrecondition( rootNode )

    self.obj56=Hyperedge(self)

    self.obj56.name.setValue('')
    self.obj56.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n\n\n\n')
    self.obj56.guard.setValue('1')
    self.obj56.trigger.setValue('to G')
    self.obj56.action.setValue('[DUMP(\'Get out from A. Send "to A" or "to HS" to go back.\')]\n\n\n')
    self.obj56.broadcast_to.setValue('')
    self.obj56.display.setValue('to G')
    self.obj56.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(282.0,376.5,self.obj56)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj56.graphObject_ = new_obj
    rootNode.addNode(self.obj56)
    self.globalAndLocalPostcondition(self.obj56, rootNode)

    self.globalPrecondition( rootNode )

    self.obj57=Hyperedge(self)

    self.obj57.name.setValue('')
    self.obj57.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj57.guard.setValue('1')
    self.obj57.trigger.setValue('to F')
    self.obj57.action.setValue('\n')
    self.obj57.broadcast_to.setValue('')
    self.obj57.display.setValue('to F')
    self.obj57.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(322.0,146.5,self.obj57)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj57.graphObject_ = new_obj
    rootNode.addNode(self.obj57)
    self.globalAndLocalPostcondition(self.obj57, rootNode)

    self.globalPrecondition( rootNode )

    self.obj58=Hyperedge(self)

    self.obj58.name.setValue('')
    self.obj58.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj58.guard.setValue('1')
    self.obj58.trigger.setValue('AFTER(1)')
    self.obj58.action.setValue('\n')
    self.obj58.broadcast_to.setValue('')
    self.obj58.display.setValue('AFTER(1)')
    self.obj58.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(129.5,259.5,self.obj58)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj58.graphObject_ = new_obj
    rootNode.addNode(self.obj58)
    self.globalAndLocalPostcondition(self.obj58, rootNode)

    self.globalPrecondition( rootNode )

    self.obj59=Hyperedge(self)

    self.obj59.name.setValue('')
    self.obj59.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj59.guard.setValue('1')
    self.obj59.trigger.setValue('AFTER(1)')
    self.obj59.action.setValue('\n')
    self.obj59.broadcast_to.setValue('')
    self.obj59.display.setValue('AFTER(1)')
    self.obj59.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(167.0,308.0,self.obj59)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj59.graphObject_ = new_obj
    rootNode.addNode(self.obj59)
    self.globalAndLocalPostcondition(self.obj59, rootNode)

    self.globalPrecondition( rootNode )

    self.obj60=Hyperedge(self)

    self.obj60.name.setValue('')
    self.obj60.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n\n')
    self.obj60.guard.setValue('1')
    self.obj60.trigger.setValue('AFTER(2)')
    self.obj60.action.setValue('\n\n')
    self.obj60.broadcast_to.setValue('')
    self.obj60.display.setValue('AFTER(2)')
    self.obj60.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(396.0,259.5,self.obj60)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj60.graphObject_ = new_obj
    rootNode.addNode(self.obj60)
    self.globalAndLocalPostcondition(self.obj60, rootNode)

    self.globalPrecondition( rootNode )

    self.obj61=Hyperedge(self)

    self.obj61.name.setValue('')
    self.obj61.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n\n')
    self.obj61.guard.setValue('1')
    self.obj61.trigger.setValue('AFTER(2)')
    self.obj61.action.setValue('\n\n')
    self.obj61.broadcast_to.setValue('')
    self.obj61.display.setValue('AFTER(2)')
    self.obj61.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(325.0,308.5,self.obj61)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj61.graphObject_ = new_obj
    rootNode.addNode(self.obj61)
    self.globalAndLocalPostcondition(self.obj61, rootNode)

    self.globalPrecondition( rootNode )

    self.obj62=orthogonality(self)

    self.obj62.graphClass_= graph_orthogonality
    if self.genGraphics:
       from graph_orthogonality import *
       new_obj = graph_orthogonality(107.5,242.5,self.obj62)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("orthogonality", new_obj.tag)
    else: new_obj = None
    self.obj62.graphObject_ = new_obj
    rootNode.addNode(self.obj62)
    self.globalAndLocalPostcondition(self.obj62, rootNode)

    self.globalPrecondition( rootNode )

    self.obj63=orthogonality(self)

    self.obj63.graphClass_= graph_orthogonality
    if self.genGraphics:
       from graph_orthogonality import *
       new_obj = graph_orthogonality(184.5,242.5,self.obj63)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("orthogonality", new_obj.tag)
    else: new_obj = None
    self.obj63.graphObject_ = new_obj
    rootNode.addNode(self.obj63)
    self.globalAndLocalPostcondition(self.obj63, rootNode)
    self.drawConnections((self.obj28,self.obj42,[164.0, 117.99999999999999, 190.0, 283.5], 0, 2), (self.obj28,self.obj46,[91.0, 201.0, 78.5, 168.0], 0, 2), (self.obj28,self.obj56,[281.0, 352.0, 282.0, 376.5],"bezier", 2), (self.obj28,self.obj47,[247.99999999999997, 335.0, 73.0, 279.0], 0, 2), (self.obj29,self.obj43,[187.0, 90.0, 190.0, 54.499999999999993], 0, 2), (self.obj29,self.obj44,[226.99999999999997, 182.0, 114.49999999999999, -14.999999999999998], 0, 2), (self.obj29,self.obj45,[176.0, 103.0, 153.0, -52.5], 0, 2), (self.obj29,self.obj57,[283.0, 147.0, 322.0, 146.5], 0, 2), (self.obj30,self.obj62,[401.0, 280.0, 107.5, 242.49999999999997], 0, 2), (self.obj30,self.obj63,[401.0, 280.0, 184.5, 242.49999999999997], 0, 2), (self.obj32,self.obj54,[125.99999999999999, 117.99999999999999, 137.0, 134.5], 0, 2), (self.obj33,self.obj55,[197.0, 162.0, 226.99999999999997, 146.0], 0, 2), (self.obj34,self.obj52,[562.0, 200.0, 514.0, 200.5], 0, 2), (self.obj34,self.obj53,[570.0, 191.0, 400.5, 73.5], 0, 2), (self.obj35,self.obj58,[129.0, 298.0, 129.5, 259.5], 0, 2), (self.obj36,self.obj59,[232.99999999999997, 308.0, 167.0, 308.0], 0, 2), (self.obj37,self.obj60,[283.0, 299.0, 282.0, 260.0, 396.0, 259.5], 0, 3), (self.obj38,self.obj61,[388.0, 308.0, 325.0, 308.5], 0, 2), (self.obj40,self.obj48,[171.0, 297.0, 93.0, 255.99999999999997], 0, 2), (self.obj40,self.obj49,[171.0, 297.0, 154.0, 284.0], 0, 2), (self.obj41,self.obj50,[383.0, 296.0, 314.5, 294.0], 0, 2), (self.obj41,self.obj51,[383.0, 296.0, 339.0, 309.0], 0, 2), (self.obj42,self.obj29,[190.0, 283.5, 161.0, 115.99999999999999], 0, 2), (self.obj43,self.obj31,[190.0, 54.499999999999993, 267.0, 111.99999999999999], 0, 2), (self.obj44,self.obj32,[114.49999999999999, -14.999999999999998, 125.99999999999999, 117.99999999999999], 0, 2), (self.obj45,self.obj33,[153.0, -52.5, 188.0, 171.0], 0, 2), (self.obj46,self.obj39,[78.5, 168.0, 213.0, 91.0], 0, 2), (self.obj47,self.obj30,[73.0, 279.0, 210.0, 287.0], 0, 2), (self.obj48,self.obj35,[93.0, 255.99999999999997, 138.0, 307.0], 0, 2), (self.obj49,self.obj36,[154.0, 284.0, 240.99999999999997, 317.0], 0, 2), (self.obj50,self.obj37,[314.5, 294.0, 292.0, 308.0], 0, 2), (self.obj51,self.obj38,[339.0, 309.0, 405.0, 308.0], 0, 2), (self.obj52,self.obj28,[514.0, 200.5, 471.99999999999994, 201.0], 0, 2), (self.obj53,self.obj39,[400.5, 73.5, 229.99999999999997, 74.0], 0, 2), (self.obj54,self.obj33,[137.0, 134.5, 180.0, 162.0], 0, 2), (self.obj55,self.obj31,[226.99999999999997, 146.0, 259.0, 120.99999999999999], 0, 2), (self.obj56,self.obj34,[282.0, 376.5, 488.99999999999994, 377.0, 570.0, 209.0], 0, 3), (self.obj57,self.obj30,[322.0, 146.5, 321.0, 200.0, 250.99999999999997, 232.99999999999997], 0, 3), (self.obj58,self.obj36,[129.5, 259.5, 241.99999999999997, 261.0, 240.99999999999997, 299.0], 0, 3), (self.obj59,self.obj35,[167.0, 308.0, 138.0, 307.0], 0, 2), (self.obj60,self.obj38,[396.0, 259.5, 396.0, 299.0], 0, 2), (self.obj61,self.obj37,[325.0, 308.5, 292.0, 308.0], 0, 2), (self.obj62,self.obj40,[107.5, 242.49999999999997, 132.0, 270.0], 0, 2), (self.obj63,self.obj41,[184.5, 242.49999999999997, 299.0, 315.0], 0, 2) )

newfunction = testsvm

loadedMMName = 'Statechart'
