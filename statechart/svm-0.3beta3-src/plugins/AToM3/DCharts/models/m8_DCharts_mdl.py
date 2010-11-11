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

def m8_DCharts_mdl(self, rootNode):

    self.globalPrecondition( rootNode )

    self.obj39=Composite(self)

    self.obj39.auto_adjust.setValue((None, 1))
    self.obj39.auto_adjust.config = 0
    self.obj39.name.setValue('AB')
    self.obj39.is_default.setValue((None, 1))
    self.obj39.is_default.config = 0
    self.obj39.visible.setValue((None, 1))
    self.obj39.visible.config = 0
    self.obj39.exit_action.setValue('\n\n\n')
    self.obj39.enter_action.setValue('\n\n\n')
    self.obj39.graphClass_= graph_Composite
    if self.genGraphics:
       from graph_Composite import *
       new_obj = graph_Composite(49.0,76.0,self.obj39)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Composite", new_obj.tag)
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
    self.obj39.graphObject_ = new_obj
    rootNode.addNode(self.obj39)
    self.globalAndLocalPostcondition(self.obj39, rootNode)

    self.globalPrecondition( rootNode )

    self.obj40=Composite(self)

    self.obj40.auto_adjust.setValue((None, 1))
    self.obj40.auto_adjust.config = 0
    self.obj40.name.setValue('active')
    self.obj40.is_default.setValue((None, 1))
    self.obj40.is_default.config = 0
    self.obj40.visible.setValue((None, 1))
    self.obj40.visible.config = 0
    self.obj40.exit_action.setValue('\n\n')
    self.obj40.enter_action.setValue('\n\n')
    self.obj40.graphClass_= graph_Composite
    if self.genGraphics:
       from graph_Composite import *
       new_obj = graph_Composite(40.0,38.0,self.obj40)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Composite", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf2.handler,85.0,55.0,830.0,284.0)
       self.UMLmodel.itemconfig(new_obj.gf2.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,85.0,48.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='active')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj40.graphObject_ = new_obj
    rootNode.addNode(self.obj40)
    self.globalAndLocalPostcondition(self.obj40, rootNode)

    self.globalPrecondition( rootNode )

    self.obj41=Basic(self)

    self.obj41.is_default.setValue((None, 1))
    self.obj41.is_default.config = 0
    self.obj41.name.setValue('A')
    self.obj41.exit_action.setValue('[DUMP("exiting state A")]\n\n')
    self.obj41.enter_action.setValue('[DUMP("entering state A")]\n\n')
    self.obj41.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(107.0,147.0,self.obj41)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
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
    self.obj41.graphObject_ = new_obj
    rootNode.addNode(self.obj41)
    self.globalAndLocalPostcondition(self.obj41, rootNode)

    self.globalPrecondition( rootNode )

    self.obj42=Basic(self)

    self.obj42.is_default.setValue((None, 0))
    self.obj42.is_default.config = 0
    self.obj42.name.setValue('B')
    self.obj42.exit_action.setValue('\n\n')
    self.obj42.enter_action.setValue('\n\n')
    self.obj42.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(248.0,149.0,self.obj42)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
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
    self.obj42.graphObject_ = new_obj
    rootNode.addNode(self.obj42)
    self.globalAndLocalPostcondition(self.obj42, rootNode)

    self.globalPrecondition( rootNode )

    self.obj43=Basic(self)

    self.obj43.is_default.setValue((None, 0))
    self.obj43.is_default.config = 0
    self.obj43.name.setValue('C')
    self.obj43.exit_action.setValue('[DUMP("exiting state C")]\n\n')
    self.obj43.enter_action.setValue('[DUMP("entering state C")]\n')
    self.obj43.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(352.0,179.0,self.obj43)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
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
    self.obj43.graphObject_ = new_obj
    rootNode.addNode(self.obj43)
    self.globalAndLocalPostcondition(self.obj43, rootNode)

    self.globalPrecondition( rootNode )

    self.obj44=Basic(self)

    self.obj44.is_default.setValue((None, 1))
    self.obj44.is_default.config = 0
    self.obj44.name.setValue('X')
    self.obj44.exit_action.setValue('\n\n')
    self.obj44.enter_action.setValue('\n\n')
    self.obj44.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(435.0,80.0,self.obj44)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
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
    self.obj44.graphObject_ = new_obj
    rootNode.addNode(self.obj44)
    self.globalAndLocalPostcondition(self.obj44, rootNode)

    self.globalPrecondition( rootNode )

    self.obj45=Basic(self)

    self.obj45.is_default.setValue((None, 0))
    self.obj45.is_default.config = 0
    self.obj45.name.setValue('Y')
    self.obj45.exit_action.setValue('\n\n')
    self.obj45.enter_action.setValue('\n\n')
    self.obj45.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(483.0,157.0,self.obj45)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
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
    self.obj45.graphObject_ = new_obj
    rootNode.addNode(self.obj45)
    self.globalAndLocalPostcondition(self.obj45, rootNode)

    self.globalPrecondition( rootNode )

    self.obj46=Basic(self)

    self.obj46.is_default.setValue((None, 1))
    self.obj46.is_default.config = 0
    self.obj46.name.setValue('t1')
    self.obj46.exit_action.setValue('\n\n\n')
    self.obj46.enter_action.setValue('\n\n\n')
    self.obj46.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(658.0,77.0,self.obj46)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,670.0,80.0,688.0,98.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,681.0,107.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='t1')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj46.graphObject_ = new_obj
    rootNode.addNode(self.obj46)
    self.globalAndLocalPostcondition(self.obj46, rootNode)

    self.globalPrecondition( rootNode )

    self.obj47=Basic(self)

    self.obj47.is_default.setValue((None, 0))
    self.obj47.is_default.config = 0
    self.obj47.name.setValue('t2')
    self.obj47.exit_action.setValue('\n\n')
    self.obj47.enter_action.setValue('\n\n')
    self.obj47.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(677.0,176.0,self.obj47)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,689.0,179.0,707.0,197.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,700.0,206.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='t2')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj47.graphObject_ = new_obj
    rootNode.addNode(self.obj47)
    self.globalAndLocalPostcondition(self.obj47, rootNode)

    self.globalPrecondition( rootNode )

    self.obj48=Basic(self)

    self.obj48.is_default.setValue((None, 0))
    self.obj48.is_default.config = 0
    self.obj48.name.setValue('inactive')
    self.obj48.exit_action.setValue('\n\n')
    self.obj48.enter_action.setValue('\n\n')
    self.obj48.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(406.0,363.0,self.obj48)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
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
    self.obj48.graphObject_ = new_obj
    rootNode.addNode(self.obj48)
    self.globalAndLocalPostcondition(self.obj48, rootNode)

    self.globalPrecondition( rootNode )

    self.obj49=History(self)

    self.obj49.is_default.setValue((None, 0))
    self.obj49.is_default.config = 0
    self.obj49.star.setValue((None, 0))
    self.obj49.star.config = 0
    self.obj49.name.setValue('')
    self.obj49.graphClass_= graph_History
    if self.genGraphics:
       from graph_History import *
       new_obj = graph_History(140.0,211.0,self.obj49)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("History", new_obj.tag)
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
    self.obj49.graphObject_ = new_obj
    rootNode.addNode(self.obj49)
    self.globalAndLocalPostcondition(self.obj49, rootNode)

    self.globalPrecondition( rootNode )

    self.obj50=Orthogonal(self)

    self.obj50.visible.setValue((None, 1))
    self.obj50.visible.config = 0
    self.obj50.name.setValue('O1')
    self.obj50.auto_adjust.setValue((None, 1))
    self.obj50.auto_adjust.config = 0
    self.obj50.graphClass_= graph_Orthogonal
    if self.genGraphics:
       from graph_Orthogonal import *
       new_obj = graph_Orthogonal(20.0,69.0,self.obj50)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Orthogonal", new_obj.tag)
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
    self.obj50.graphObject_ = new_obj
    rootNode.addNode(self.obj50)
    self.globalAndLocalPostcondition(self.obj50, rootNode)

    self.globalPrecondition( rootNode )

    self.obj51=Orthogonal(self)

    self.obj51.visible.setValue((None, 1))
    self.obj51.visible.config = 0
    self.obj51.name.setValue('O2')
    self.obj51.auto_adjust.setValue((None, 1))
    self.obj51.auto_adjust.config = 0
    self.obj51.graphClass_= graph_Orthogonal
    if self.genGraphics:
       from graph_Orthogonal import *
       new_obj = graph_Orthogonal(325.0,46.0,self.obj51)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Orthogonal", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf5.handler,427.0,77.0,601.0,199.0)
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
    self.obj51.graphObject_ = new_obj
    rootNode.addNode(self.obj51)
    self.globalAndLocalPostcondition(self.obj51, rootNode)

    self.globalPrecondition( rootNode )

    self.obj52=Orthogonal(self)

    self.obj52.visible.setValue((None, 1))
    self.obj52.visible.config = 0
    self.obj52.name.setValue('O3')
    self.obj52.auto_adjust.setValue((None, 1))
    self.obj52.auto_adjust.config = 0
    self.obj52.graphClass_= graph_Orthogonal
    if self.genGraphics:
       from graph_Orthogonal import *
       new_obj = graph_Orthogonal(603.0,73.0,self.obj52)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Orthogonal", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf5.handler,633.0,74.0,823.0,218.0)
       self.UMLmodel.itemconfig(new_obj.gf5.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, outline='DARKGRAY')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,633.0,67.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='O3')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj52.graphObject_ = new_obj
    rootNode.addNode(self.obj52)
    self.globalAndLocalPostcondition(self.obj52, rootNode)

    self.globalPrecondition( rootNode )

    self.obj53=contains(self)

    self.obj53.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(106.5,138.0,self.obj53)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj53.graphObject_ = new_obj
    rootNode.addNode(self.obj53)
    self.globalAndLocalPostcondition(self.obj53, rootNode)

    self.globalPrecondition( rootNode )

    self.obj54=contains(self)

    self.obj54.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(165.0,138.5,self.obj54)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj54.graphObject_ = new_obj
    rootNode.addNode(self.obj54)
    self.globalAndLocalPostcondition(self.obj54, rootNode)

    self.globalPrecondition( rootNode )

    self.obj55=contains(self)

    self.obj55.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(-3.5,106.5,self.obj55)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj55.graphObject_ = new_obj
    rootNode.addNode(self.obj55)
    self.globalAndLocalPostcondition(self.obj55, rootNode)

    self.globalPrecondition( rootNode )

    self.obj56=contains(self)

    self.obj56.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(157.0,135.0,self.obj56)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj56.graphObject_ = new_obj
    rootNode.addNode(self.obj56)
    self.globalAndLocalPostcondition(self.obj56, rootNode)

    self.globalPrecondition( rootNode )

    self.obj57=contains(self)

    self.obj57.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(271.5,51.5,self.obj57)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj57.graphObject_ = new_obj
    rootNode.addNode(self.obj57)
    self.globalAndLocalPostcondition(self.obj57, rootNode)

    self.globalPrecondition( rootNode )

    self.obj58=contains(self)

    self.obj58.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(295.5,90.0,self.obj58)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj58.graphObject_ = new_obj
    rootNode.addNode(self.obj58)
    self.globalAndLocalPostcondition(self.obj58, rootNode)

    self.globalPrecondition( rootNode )

    self.obj59=contains(self)

    self.obj59.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(174.0,166.5,self.obj59)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj59.graphObject_ = new_obj
    rootNode.addNode(self.obj59)
    self.globalAndLocalPostcondition(self.obj59, rootNode)

    self.globalPrecondition( rootNode )

    self.obj60=contains(self)

    self.obj60.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(645.0,84.5,self.obj60)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj60.graphObject_ = new_obj
    rootNode.addNode(self.obj60)
    self.globalAndLocalPostcondition(self.obj60, rootNode)

    self.globalPrecondition( rootNode )

    self.obj61=contains(self)

    self.obj61.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(654.5,134.0,self.obj61)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj61.graphObject_ = new_obj
    rootNode.addNode(self.obj61)
    self.globalAndLocalPostcondition(self.obj61, rootNode)

    self.globalPrecondition( rootNode )

    self.obj62=Hyperedge(self)

    self.obj62.name.setValue('')
    self.obj62.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj62.guard.setValue('1')
    self.obj62.trigger.setValue('e1')
    self.obj62.action.setValue('[DUMP("triggered by e1")]\n')
    self.obj62.broadcast_to.setValue('')
    self.obj62.display.setValue('e1')
    self.obj62.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(181.5,120.5,self.obj62)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj62.graphObject_ = new_obj
    rootNode.addNode(self.obj62)
    self.globalAndLocalPostcondition(self.obj62, rootNode)

    self.globalPrecondition( rootNode )

    self.obj63=Hyperedge(self)

    self.obj63.name.setValue('')
    self.obj63.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj63.guard.setValue('1')
    self.obj63.trigger.setValue('e2')
    self.obj63.action.setValue('[DUMP("triggered by e2")]\n')
    self.obj63.broadcast_to.setValue('')
    self.obj63.display.setValue('e2')
    self.obj63.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(188.5,192.5,self.obj63)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj63.graphObject_ = new_obj
    rootNode.addNode(self.obj63)
    self.globalAndLocalPostcondition(self.obj63, rootNode)

    self.globalPrecondition( rootNode )

    self.obj64=Hyperedge(self)

    self.obj64.name.setValue('')
    self.obj64.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n\n')
    self.obj64.guard.setValue('1')
    self.obj64.trigger.setValue('e3')
    self.obj64.action.setValue('\n\n')
    self.obj64.broadcast_to.setValue('')
    self.obj64.display.setValue('e3')
    self.obj64.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(309.0,191.5,self.obj64)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj64.graphObject_ = new_obj
    rootNode.addNode(self.obj64)
    self.globalAndLocalPostcondition(self.obj64, rootNode)

    self.globalPrecondition( rootNode )

    self.obj65=Hyperedge(self)

    self.obj65.name.setValue('')
    self.obj65.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n\n\n')
    self.obj65.guard.setValue('[PARAMS][0] > 1')
    self.obj65.trigger.setValue('trig1')
    self.obj65.action.setValue('\n[DUMP([PARAMS][1])]\n')
    self.obj65.broadcast_to.setValue('')
    self.obj65.display.setValue('trig1[[PARAMS][0] > 1]')
    self.obj65.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(505.0,116.5,self.obj65)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj65.graphObject_ = new_obj
    rootNode.addNode(self.obj65)
    self.globalAndLocalPostcondition(self.obj65, rootNode)

    self.globalPrecondition( rootNode )

    self.obj66=Hyperedge(self)

    self.obj66.name.setValue('')
    self.obj66.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj66.guard.setValue('1')
    self.obj66.trigger.setValue('AFTER(2)')
    self.obj66.action.setValue('\n')
    self.obj66.broadcast_to.setValue('')
    self.obj66.display.setValue('tm(2)')
    self.obj66.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(435.0,151.5,self.obj66)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj66.graphObject_ = new_obj
    rootNode.addNode(self.obj66)
    self.globalAndLocalPostcondition(self.obj66, rootNode)

    self.globalPrecondition( rootNode )

    self.obj67=Hyperedge(self)

    self.obj67.name.setValue('')
    self.obj67.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj67.guard.setValue('1')
    self.obj67.trigger.setValue('back')
    self.obj67.action.setValue('\n')
    self.obj67.broadcast_to.setValue('')
    self.obj67.display.setValue('back')
    self.obj67.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(202.5,83.5,self.obj67)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj67.graphObject_ = new_obj
    rootNode.addNode(self.obj67)
    self.globalAndLocalPostcondition(self.obj67, rootNode)

    self.globalPrecondition( rootNode )

    self.obj68=Hyperedge(self)

    self.obj68.name.setValue('')
    self.obj68.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj68.guard.setValue('1')
    self.obj68.trigger.setValue('hist')
    self.obj68.action.setValue('\n')
    self.obj68.broadcast_to.setValue('')
    self.obj68.display.setValue('hist')
    self.obj68.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(361.0,231.5,self.obj68)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj68.graphObject_ = new_obj
    rootNode.addNode(self.obj68)
    self.globalAndLocalPostcondition(self.obj68, rootNode)

    self.globalPrecondition( rootNode )

    self.obj69=Hyperedge(self)

    self.obj69.name.setValue('')
    self.obj69.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj69.guard.setValue('1')
    self.obj69.trigger.setValue('AFTER(0.5)')
    self.obj69.action.setValue('\n')
    self.obj69.broadcast_to.setValue('')
    self.obj69.display.setValue('tm(0.5)')
    self.obj69.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(640.5,132.5,self.obj69)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj69.graphObject_ = new_obj
    rootNode.addNode(self.obj69)
    self.globalAndLocalPostcondition(self.obj69, rootNode)

    self.globalPrecondition( rootNode )

    self.obj70=Hyperedge(self)

    self.obj70.name.setValue('')
    self.obj70.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n\n\n\n\n')
    self.obj70.guard.setValue('1')
    self.obj70.trigger.setValue('AFTER(3)')
    self.obj70.action.setValue('[EVENT("trig1",[2,"hello"])]\n\n\n\n\n')
    self.obj70.broadcast_to.setValue('')
    self.obj70.display.setValue('tm(3)/trig1([2,"hello"])')
    self.obj70.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(729.5,135.5,self.obj70)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj70.graphObject_ = new_obj
    rootNode.addNode(self.obj70)
    self.globalAndLocalPostcondition(self.obj70, rootNode)

    self.globalPrecondition( rootNode )

    self.obj71=Hyperedge(self)

    self.obj71.name.setValue('')
    self.obj71.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj71.guard.setValue('1')
    self.obj71.trigger.setValue('activate')
    self.obj71.action.setValue('\n')
    self.obj71.broadcast_to.setValue('')
    self.obj71.display.setValue('activate')
    self.obj71.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(427.5,336.5,self.obj71)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj71.graphObject_ = new_obj
    rootNode.addNode(self.obj71)
    self.globalAndLocalPostcondition(self.obj71, rootNode)

    self.globalPrecondition( rootNode )

    self.obj72=Hyperedge(self)

    self.obj72.name.setValue('')
    self.obj72.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj72.guard.setValue('1')
    self.obj72.trigger.setValue('deactivate')
    self.obj72.action.setValue('\n')
    self.obj72.broadcast_to.setValue('')
    self.obj72.display.setValue('deactivate')
    self.obj72.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(17.5,168.5,self.obj72)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj72.graphObject_ = new_obj
    rootNode.addNode(self.obj72)
    self.globalAndLocalPostcondition(self.obj72, rootNode)

    self.globalPrecondition( rootNode )

    self.obj73=orthogonality(self)

    self.obj73.graphClass_= graph_orthogonality
    if self.genGraphics:
       from graph_orthogonality import *
       new_obj = graph_orthogonality(92.0,66.5,self.obj73)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("orthogonality", new_obj.tag)
    else: new_obj = None
    self.obj73.graphObject_ = new_obj
    rootNode.addNode(self.obj73)
    self.globalAndLocalPostcondition(self.obj73, rootNode)

    self.globalPrecondition( rootNode )

    self.obj74=orthogonality(self)

    self.obj74.graphClass_= graph_orthogonality
    if self.genGraphics:
       from graph_orthogonality import *
       new_obj = graph_orthogonality(256.0,67.0,self.obj74)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("orthogonality", new_obj.tag)
    else: new_obj = None
    self.obj74.graphObject_ = new_obj
    rootNode.addNode(self.obj74)
    self.globalAndLocalPostcondition(self.obj74, rootNode)

    self.globalPrecondition( rootNode )

    self.obj75=orthogonality(self)

    self.obj75.graphClass_= graph_orthogonality
    if self.genGraphics:
       from graph_orthogonality import *
       new_obj = graph_orthogonality(342.5,67.0,self.obj75)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("orthogonality", new_obj.tag)
    else: new_obj = None
    self.obj75.graphObject_ = new_obj
    rootNode.addNode(self.obj75)
    self.globalAndLocalPostcondition(self.obj75, rootNode)
    self.drawConnections((self.obj39,self.obj53,[113.0, 191.0, 106.5, 138.0], 0, 2), (self.obj39,self.obj54,[198.99999999999997, 113.0, 165.0, 138.5], 0, 2), (self.obj39,self.obj64,[285.0, 191.0, 309.0, 191.5], 0, 2), (self.obj39,self.obj59,[198.99999999999997, 270.0, 174.0, 166.5], 0, 2), (self.obj40,self.obj73,[85.0, 169.0, 92.0, 66.5], 0, 2), (self.obj40,self.obj74,[457.0, 55.000000000000007, 256.0, 67.0], 0, 2), (self.obj40,self.obj75,[457.0, 55.000000000000007, 342.5, 67.0], 0, 2), (self.obj40,self.obj72,[85.0, 169.0, 17.5, 168.5], 0, 2), (self.obj41,self.obj62,[137.0, 159.0, 181.5, 120.5], 0, 2), (self.obj42,self.obj63,[261.0, 161.0, 188.5, 192.49999999999997], 0, 2), (self.obj43,self.obj67,[373.0, 182.0, 364.0, 85.0, 202.5, 83.5], 0, 3), (self.obj43,self.obj68,[373.0, 200.0, 361.0, 231.5], 0, 2), (self.obj44,self.obj65,[465.00000000000006, 92.0, 505.0, 116.49999999999999], 0, 2), (self.obj45,self.obj66,[496.0, 169.0, 434.99999999999994, 151.5], 0, 2), (self.obj46,self.obj69,[671.0, 89.0, 640.5, 132.5], 0, 2), (self.obj47,self.obj70,[707.0, 188.0, 729.5, 135.5], 0, 2), (self.obj48,self.obj71,[427.0, 366.0, 427.50000000000006, 336.5], 0, 2), (self.obj50,self.obj55,[395.0, 176.0, -3.4999999999999996, 106.5], 0, 2), (self.obj50,self.obj56,[247.0, 76.0, 157.0, 135.0], 0, 2), (self.obj51,self.obj57,[561.0, 138.0, 271.5, 51.5], 0, 2), (self.obj51,self.obj58,[427.0, 138.0, 295.5, 90.0], 0, 2), (self.obj52,self.obj60,[797.0, 146.0, 645.0, 84.5], 0, 2), (self.obj52,self.obj61,[707.0, 218.0, 654.5, 134.0], 0, 2), (self.obj53,self.obj41,[106.5, 138.0, 128.0, 150.0], 0, 2), (self.obj54,self.obj42,[165.0, 138.5, 261.0, 161.0], 0, 2), (self.obj55,self.obj39,[-3.4999999999999996, 106.5, 113.0, 191.0], 0, 2), (self.obj56,self.obj43,[157.0, 135.0, 365.0, 191.0], 0, 2), (self.obj57,self.obj44,[271.5, 51.5, 447.99999999999994, 92.0], 0, 2), (self.obj58,self.obj45,[295.5, 90.0, 496.0, 169.0], 0, 2), (self.obj59,self.obj49,[174.0, 166.5, 144.0, 232.99999999999997], 0, 2), (self.obj60,self.obj46,[645.0, 84.5, 679.0, 98.0], 0, 2), (self.obj61,self.obj47,[654.5, 134.0, 698.0, 179.0], 0, 2), (self.obj62,self.obj42,[181.5, 120.5, 261.0, 161.0], 0, 2), (self.obj63,self.obj41,[188.5, 192.49999999999997, 137.0, 159.0], 0, 2), (self.obj64,self.obj43,[309.0, 191.5, 365.0, 191.0], 0, 2), (self.obj65,self.obj45,[505.0, 116.49999999999999, 513.0, 169.0], 0, 2), (self.obj66,self.obj44,[434.99999999999994, 151.5, 447.99999999999994, 92.0], 0, 2), (self.obj67,self.obj39,[202.5, 83.5, 198.99999999999997, 113.0], 0, 2), (self.obj68,self.obj49,[361.0, 231.5, 179.0, 232.0], 0, 2), (self.obj69,self.obj47,[640.5, 132.5, 690.0, 188.0], 0, 2), (self.obj70,self.obj46,[729.5, 135.5, 688.0, 89.0], 0, 2), (self.obj71,self.obj40,[427.50000000000006, 336.5, 457.0, 284.0], 0, 2), (self.obj72,self.obj48,[17.5, 168.5, 18.0, 375.0, 419.0, 375.0], 0, 3), (self.obj73,self.obj50,[92.0, 66.5, 99.0, 176.0], 0, 2), (self.obj74,self.obj51,[256.0, 67.0, 427.0, 138.0], 0, 2), (self.obj75,self.obj52,[342.5, 67.0, 633.0, 146.0], 0, 2) )

newfunction = m8_DCharts_mdl

loadedMMName = 'DCharts'
