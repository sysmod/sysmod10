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

def TrafficLight(self, rootNode):

    self.globalPrecondition( rootNode )

    self.obj33=Composite(self)

    self.obj33.auto_adjust.setValue((None, 1))
    self.obj33.auto_adjust.config = 0
    self.obj33.name.setValue('ON')
    self.obj33.is_default.setValue((None, 1))
    self.obj33.is_default.config = 0
    self.obj33.visible.setValue((None, 1))
    self.obj33.visible.config = 0
    self.obj33.exit_action.setValue('\n')
    self.obj33.enter_action.setValue('\n')
    self.obj33.graphClass_= graph_Composite
    if self.genGraphics:
       from graph_Composite import *
       new_obj = graph_Composite(68.0,175.0,self.obj33)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Composite", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf2.handler,94.0,75.0,556.0,648.0)
       self.UMLmodel.itemconfig(new_obj.gf2.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,94.0,68.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='ON')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj33.graphObject_ = new_obj
    rootNode.addNode(self.obj33)
    self.globalAndLocalPostcondition(self.obj33, rootNode)

    self.globalPrecondition( rootNode )

    self.obj34=Composite(self)

    self.obj34.auto_adjust.setValue((None, 1))
    self.obj34.auto_adjust.config = 0
    self.obj34.name.setValue('NORMAL')
    self.obj34.is_default.setValue((None, 1))
    self.obj34.is_default.config = 0
    self.obj34.visible.setValue((None, 1))
    self.obj34.visible.config = 0
    self.obj34.exit_action.setValue('\n\n')
    self.obj34.enter_action.setValue('\n\n')
    self.obj34.graphClass_= graph_Composite
    if self.genGraphics:
       from graph_Composite import *
       new_obj = graph_Composite(272.0,124.0,self.obj34)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Composite", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf2.handler,158.0,94.0,422.0,450.0)
       self.UMLmodel.itemconfig(new_obj.gf2.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,158.0,87.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='NORMAL')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj34.graphObject_ = new_obj
    rootNode.addNode(self.obj34)
    self.globalAndLocalPostcondition(self.obj34, rootNode)

    self.globalPrecondition( rootNode )

    self.obj35=Composite(self)

    self.obj35.auto_adjust.setValue((None, 1))
    self.obj35.auto_adjust.config = 0
    self.obj35.name.setValue('FLASHING')
    self.obj35.is_default.setValue((None, 0))
    self.obj35.is_default.config = 0
    self.obj35.visible.setValue((None, 1))
    self.obj35.visible.config = 0
    self.obj35.exit_action.setValue('\n')
    self.obj35.enter_action.setValue('\n')
    self.obj35.graphClass_= graph_Composite
    if self.genGraphics:
       from graph_Composite import *
       new_obj = graph_Composite(272.0,407.0,self.obj35)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Composite", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf2.handler,171.0,530.0,415.0,641.0)
       self.UMLmodel.itemconfig(new_obj.gf2.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,171.0,523.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='FLASHING')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj35.graphObject_ = new_obj
    rootNode.addNode(self.obj35)
    self.globalAndLocalPostcondition(self.obj35, rootNode)

    self.globalPrecondition( rootNode )

    self.obj36=Composite(self)

    self.obj36.auto_adjust.setValue((None, 1))
    self.obj36.auto_adjust.config = 0
    self.obj36.name.setValue('RED')
    self.obj36.is_default.setValue((None, 1))
    self.obj36.is_default.config = 0
    self.obj36.visible.setValue((None, 1))
    self.obj36.visible.config = 0
    self.obj36.exit_action.setValue('\n\n')
    self.obj36.enter_action.setValue('\n')
    self.obj36.graphClass_= graph_Composite
    if self.genGraphics:
       from graph_Composite import *
       new_obj = graph_Composite(223.0,47.0,self.obj36)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Composite", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf2.handler,176.0,113.0,415.0,189.0)
       self.UMLmodel.itemconfig(new_obj.gf2.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,176.0,106.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='RED')
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

    self.obj37.is_default.setValue((None, 0))
    self.obj37.is_default.config = 0
    self.obj37.name.setValue('GREEN')
    self.obj37.exit_action.setValue('\n\n')
    self.obj37.enter_action.setValue('\n')
    self.obj37.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(274.0,408.0,self.obj37)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,286.0,411.0,304.0,429.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,297.0,438.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='GREEN')
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
    self.obj38.name.setValue('YELLOW')
    self.obj38.exit_action.setValue('\n\n')
    self.obj38.enter_action.setValue('\n')
    self.obj38.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(274.0,319.0,self.obj38)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,286.0,322.0,304.0,340.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,297.0,349.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='YELLOW')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj38.graphObject_ = new_obj
    rootNode.addNode(self.obj38)
    self.globalAndLocalPostcondition(self.obj38, rootNode)

    self.globalPrecondition( rootNode )

    self.obj39=Basic(self)

    self.obj39.is_default.setValue((None, 1))
    self.obj39.is_default.config = 0
    self.obj39.name.setValue('RED_WAIT')
    self.obj39.exit_action.setValue('\n')
    self.obj39.enter_action.setValue('\n')
    self.obj39.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(355.0,147.0,self.obj39)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,367.0,150.0,385.0,168.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,378.0,177.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='RED_WAIT')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj39.graphObject_ = new_obj
    rootNode.addNode(self.obj39)
    self.globalAndLocalPostcondition(self.obj39, rootNode)

    self.globalPrecondition( rootNode )

    self.obj40=Basic(self)

    self.obj40.is_default.setValue((None, 0))
    self.obj40.is_default.config = 0
    self.obj40.name.setValue('GREEN_SOON')
    self.obj40.exit_action.setValue('\n')
    self.obj40.enter_action.setValue('\n')
    self.obj40.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(202.0,146.0,self.obj40)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,214.0,149.0,232.0,167.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,225.0,176.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='GREEN_SOON')
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
    self.obj41.name.setValue('YELLOW_ON')
    self.obj41.exit_action.setValue('\n\n')
    self.obj41.enter_action.setValue('\n')
    self.obj41.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(263.0,533.0,self.obj41)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,275.0,536.0,293.0,554.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,286.0,563.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='YELLOW_ON')
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
    self.obj42.name.setValue('YELLOW_OFF')
    self.obj42.exit_action.setValue('\n\n')
    self.obj42.enter_action.setValue('\n')
    self.obj42.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(269.0,599.0,self.obj42)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,281.0,602.0,299.0,620.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,292.0,629.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='YELLOW_OFF')
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
    self.obj43.name.setValue('OFF')
    self.obj43.exit_action.setValue('\n\n')
    self.obj43.enter_action.setValue('\n')
    self.obj43.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(400.0,13.0,self.obj43)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,412.0,16.0,430.0,34.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,423.0,43.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='OFF')
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

    self.obj44.is_default.setValue((None, 0))
    self.obj44.is_default.config = 0
    self.obj44.name.setValue('DEAD')
    self.obj44.exit_action.setValue('\n\n')
    self.obj44.enter_action.setValue('\n')
    self.obj44.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(624.0,349.0,self.obj44)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,636.0,352.0,654.0,370.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,647.0,379.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='DEAD')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj44.graphObject_ = new_obj
    rootNode.addNode(self.obj44)
    self.globalAndLocalPostcondition(self.obj44, rootNode)

    self.globalPrecondition( rootNode )

    self.obj45=History(self)

    self.obj45.is_default.setValue((None, 0))
    self.obj45.is_default.config = 0
    self.obj45.star.setValue((None, 1))
    self.obj45.star.config = 0
    self.obj45.name.setValue('')
    self.obj45.graphClass_= graph_History
    if self.genGraphics:
       from graph_History import *
       new_obj = graph_History(477.0,180.0,self.obj45)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("History", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf0.handler,480.0,183.0,516.0,218.0)
       self.UMLmodel.itemconfig(new_obj.gf0.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf0.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf0.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf0.handler, fill='lightblue')
       self.UMLmodel.coords(new_obj.gf1.handler,497.0,202.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='H')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       self.UMLmodel.coords(new_obj.gf2.handler,505.0,202.0)
       self.UMLmodel.itemconfig(new_obj.gf2.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, text='*')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, justify='left')
       self.UMLmodel.coords(new_obj.gf3.handler,500.0,227.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='blue')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, text='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, justify='left')
    else: new_obj = None
    self.obj45.graphObject_ = new_obj
    rootNode.addNode(self.obj45)
    self.globalAndLocalPostcondition(self.obj45, rootNode)

    self.globalPrecondition( rootNode )

    self.obj46=contains(self)

    self.obj46.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(217.5,242.5,self.obj46)
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
       new_obj = graph_contains(318.0,250.5,self.obj47)
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
       new_obj = graph_contains(275.0,352.0,self.obj48)
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
       new_obj = graph_contains(303.0,260.0,self.obj49)
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
       new_obj = graph_contains(282.0,263.5,self.obj50)
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
       new_obj = graph_contains(352.0,-327.5,self.obj51)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj51.graphObject_ = new_obj
    rootNode.addNode(self.obj51)
    self.globalAndLocalPostcondition(self.obj51, rootNode)

    self.globalPrecondition( rootNode )

    self.obj52=contains(self)

    self.obj52.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(290.0,-327.0,self.obj52)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj52.graphObject_ = new_obj
    rootNode.addNode(self.obj52)
    self.globalAndLocalPostcondition(self.obj52, rootNode)

    self.globalPrecondition( rootNode )

    self.obj53=contains(self)

    self.obj53.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(303.5,248.5,self.obj53)
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
       new_obj = graph_contains(165.0,504.5,self.obj54)
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
       new_obj = graph_contains(167.0,544.5,self.obj55)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj55.graphObject_ = new_obj
    rootNode.addNode(self.obj55)
    self.globalAndLocalPostcondition(self.obj55, rootNode)

    self.globalPrecondition( rootNode )

    self.obj56=Hyperedge(self)

    self.obj56.name.setValue('')
    self.obj56.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj56.guard.setValue('1')
    self.obj56.trigger.setValue('AFTER(6)')
    self.obj56.action.setValue('\n')
    self.obj56.broadcast_to.setValue('')
    self.obj56.display.setValue('AFTER(6)')
    self.obj56.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(274.0,158.5,self.obj56)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj56.graphObject_ = new_obj
    rootNode.addNode(self.obj56)
    self.globalAndLocalPostcondition(self.obj56, rootNode)

    self.globalPrecondition( rootNode )

    self.obj57=Hyperedge(self)

    self.obj57.name.setValue('')
    self.obj57.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj57.guard.setValue('1')
    self.obj57.trigger.setValue('CROSSWALK')
    self.obj57.action.setValue('\n')
    self.obj57.broadcast_to.setValue('')
    self.obj57.display.setValue('CROSSWALK')
    self.obj57.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(271.0,121.5,self.obj57)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj57.graphObject_ = new_obj
    rootNode.addNode(self.obj57)
    self.globalAndLocalPostcondition(self.obj57, rootNode)

    self.globalPrecondition( rootNode )

    self.obj58=Hyperedge(self)

    self.obj58.name.setValue('')
    self.obj58.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj58.guard.setValue('1')
    self.obj58.trigger.setValue('AFTER(5)')
    self.obj58.action.setValue('\n')
    self.obj58.broadcast_to.setValue('')
    self.obj58.display.setValue('AFTER(5)')
    self.obj58.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(296.0,374.5,self.obj58)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj58.graphObject_ = new_obj
    rootNode.addNode(self.obj58)
    self.globalAndLocalPostcondition(self.obj58, rootNode)

    self.globalPrecondition( rootNode )

    self.obj59=Hyperedge(self)

    self.obj59.name.setValue('')
    self.obj59.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj59.guard.setValue('1')
    self.obj59.trigger.setValue('AFTER(2)')
    self.obj59.action.setValue('\n')
    self.obj59.broadcast_to.setValue('')
    self.obj59.display.setValue('AFTER(2)')
    self.obj59.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(294.5,259.5,self.obj59)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj59.graphObject_ = new_obj
    rootNode.addNode(self.obj59)
    self.globalAndLocalPostcondition(self.obj59, rootNode)

    self.globalPrecondition( rootNode )

    self.obj60=Hyperedge(self)

    self.obj60.name.setValue('')
    self.obj60.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj60.guard.setValue('1')
    self.obj60.trigger.setValue('AFTER(2)')
    self.obj60.action.setValue('\n')
    self.obj60.broadcast_to.setValue('')
    self.obj60.display.setValue('AFTER(2)')
    self.obj60.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(223.0,225.0,self.obj60)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj60.graphObject_ = new_obj
    rootNode.addNode(self.obj60)
    self.globalAndLocalPostcondition(self.obj60, rootNode)

    self.globalPrecondition( rootNode )

    self.obj61=Hyperedge(self)

    self.obj61.name.setValue('')
    self.obj61.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj61.guard.setValue('1')
    self.obj61.trigger.setValue('AFTER(0.5)')
    self.obj61.action.setValue('\n')
    self.obj61.broadcast_to.setValue('')
    self.obj61.display.setValue('AFTER(0.5)')
    self.obj61.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(348.0,584.0,self.obj61)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj61.graphObject_ = new_obj
    rootNode.addNode(self.obj61)
    self.globalAndLocalPostcondition(self.obj61, rootNode)

    self.globalPrecondition( rootNode )

    self.obj62=Hyperedge(self)

    self.obj62.name.setValue('')
    self.obj62.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj62.guard.setValue('1')
    self.obj62.trigger.setValue('ON-OFF')
    self.obj62.action.setValue('\n')
    self.obj62.broadcast_to.setValue('')
    self.obj62.display.setValue('ON-OFF')
    self.obj62.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(497.0,144.5,self.obj62)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj62.graphObject_ = new_obj
    rootNode.addNode(self.obj62)
    self.globalAndLocalPostcondition(self.obj62, rootNode)

    self.globalPrecondition( rootNode )

    self.obj63=Hyperedge(self)

    self.obj63.name.setValue('')
    self.obj63.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj63.guard.setValue('1')
    self.obj63.trigger.setValue('ON-OFF')
    self.obj63.action.setValue('\n')
    self.obj63.broadcast_to.setValue('')
    self.obj63.display.setValue('ON-OFF')
    self.obj63.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(325.0,25.0,self.obj63)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj63.graphObject_ = new_obj
    rootNode.addNode(self.obj63)
    self.globalAndLocalPostcondition(self.obj63, rootNode)

    self.globalPrecondition( rootNode )

    self.obj64=Hyperedge(self)

    self.obj64.name.setValue('')
    self.obj64.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj64.guard.setValue('1')
    self.obj64.trigger.setValue('POLICE')
    self.obj64.action.setValue('\n')
    self.obj64.broadcast_to.setValue('')
    self.obj64.display.setValue('POLICE')
    self.obj64.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(466.0,464.5,self.obj64)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj64.graphObject_ = new_obj
    rootNode.addNode(self.obj64)
    self.globalAndLocalPostcondition(self.obj64, rootNode)

    self.globalPrecondition( rootNode )

    self.obj65=Hyperedge(self)

    self.obj65.name.setValue('')
    self.obj65.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj65.guard.setValue('1')
    self.obj65.trigger.setValue('POLICE')
    self.obj65.action.setValue('\n')
    self.obj65.broadcast_to.setValue('')
    self.obj65.display.setValue('POLICE')
    self.obj65.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(102.0,466.5,self.obj65)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj65.graphObject_ = new_obj
    rootNode.addNode(self.obj65)
    self.globalAndLocalPostcondition(self.obj65, rootNode)

    self.globalPrecondition( rootNode )

    self.obj66=Hyperedge(self)

    self.obj66.name.setValue('')
    self.obj66.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj66.guard.setValue('1')
    self.obj66.trigger.setValue('QUIT')
    self.obj66.action.setValue('\n')
    self.obj66.broadcast_to.setValue('')
    self.obj66.display.setValue('QUIT')
    self.obj66.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(565.5,360.5,self.obj66)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj66.graphObject_ = new_obj
    rootNode.addNode(self.obj66)
    self.globalAndLocalPostcondition(self.obj66, rootNode)

    self.globalPrecondition( rootNode )

    self.obj67=Hyperedge(self)

    self.obj67.name.setValue('')
    self.obj67.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj67.guard.setValue('1')
    self.obj67.trigger.setValue('AFTER(0.5)')
    self.obj67.action.setValue('\n')
    self.obj67.broadcast_to.setValue('')
    self.obj67.display.setValue('AFTER(0.5)')
    self.obj67.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(181.0,579.0,self.obj67)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj67.graphObject_ = new_obj
    rootNode.addNode(self.obj67)
    self.globalAndLocalPostcondition(self.obj67, rootNode)
    self.drawConnections((self.obj33,self.obj46,[120.99999999999999, 201.0, 217.49999999999997, 242.49999999999997], 0, 2), (self.obj33,self.obj47,[325.0, 75.0, 318.0, 250.49999999999997], 0, 2), (self.obj33,self.obj48,[196.0, 268.0, 275.0, 352.0], 0, 2), (self.obj33,self.obj63,[325.0, 75.0, 325.0, 25.0], 0, 2), (self.obj33,self.obj66,[556.0, 361.0, 565.5, 360.5], 0, 2), (self.obj34,self.obj49,[290.0, 449.99999999999994, 303.0, 260.0], 0, 2), (self.obj34,self.obj50,[290.0, 449.99999999999994, 282.0, 263.5], 0, 2), (self.obj34,self.obj53,[158.0, 272.0, 303.5, 248.49999999999997], 0, 2), (self.obj34,self.obj65,[158.0, 272.0, 103.0, 273.0, 102.0, 466.49999999999994], 0, 3), (self.obj35,self.obj54,[171.0, 585.0, 165.0, 504.49999999999994], 0, 2), (self.obj35,self.obj55,[293.0, 530.0, 167.0, 544.5], 0, 2), (self.obj35,self.obj64,[415.0, 585.0, 465.99999999999994, 584.0, 465.99999999999994, 464.49999999999994], 0, 3), (self.obj36,self.obj51,[415.0, 178.0, 352.0, -327.5], 0, 2), (self.obj36,self.obj52,[176.0, 178.0, 290.0, -327.0], 0, 2), (self.obj37,self.obj58,[295.0, 411.0, 296.0, 374.5], 0, 2), (self.obj38,self.obj59,[295.0, 322.0, 294.5, 259.5], 0, 2), (self.obj39,self.obj56,[368.0, 159.0, 274.0, 158.5], 0, 2), (self.obj39,self.obj57,[376.0, 150.0, 376.0, 120.99999999999999, 271.0, 121.49999999999999], 0, 3), (self.obj40,self.obj60,[222.99999999999997, 167.0, 222.99999999999997, 224.99999999999997], 0, 2), (self.obj41,self.obj67,[276.0, 545.0, 181.0, 545.0, 181.0, 579.0], 0, 3), (self.obj42,self.obj61,[299.0, 611.0, 348.0, 612.0, 348.0, 584.0], 0, 3), (self.obj43,self.obj62,[430.0, 25.0, 497.99999999999994, 25.0, 496.99999999999994, 144.5], 0, 3), (self.obj46,self.obj34,[217.49999999999997, 242.49999999999997, 158.0, 272.0], 0, 2), (self.obj47,self.obj35,[318.0, 250.49999999999997, 253.99999999999997, 538.0], 0, 2), (self.obj48,self.obj45,[275.0, 352.0, 479.99999999999994, 202.0], 0, 2), (self.obj49,self.obj37,[303.0, 260.0, 295.0, 411.0], 0, 2), (self.obj50,self.obj38,[282.0, 263.5, 295.0, 322.0], 0, 2), (self.obj51,self.obj39,[352.0, -327.5, 368.0, 159.0], 0, 2), (self.obj52,self.obj40,[290.0, -327.0, 222.99999999999997, 149.0], 0, 2), (self.obj53,self.obj36,[303.5, 248.49999999999997, 295.0, 112.99999999999999], 0, 2), (self.obj54,self.obj41,[165.0, 504.49999999999994, 293.0, 545.0], 0, 2), (self.obj55,self.obj42,[167.0, 544.5, 299.0, 611.0], 0, 2), (self.obj56,self.obj40,[274.0, 158.5, 231.99999999999997, 158.0], 0, 2), (self.obj57,self.obj40,[271.0, 121.49999999999999, 222.99999999999997, 121.99999999999999, 222.99999999999997, 149.0], 0, 3), (self.obj58,self.obj38,[296.0, 374.5, 295.0, 340.0], 0, 2), (self.obj59,self.obj36,[294.5, 259.5, 295.0, 189.0], 0, 2), (self.obj60,self.obj37,[222.99999999999997, 224.99999999999997, 221.99999999999997, 354.0, 222.99999999999997, 420.0, 287.0, 420.0], 0, 4), (self.obj61,self.obj41,[348.0, 584.0, 347.0, 545.0, 293.0, 545.0], 0, 3), (self.obj62,self.obj45,[496.99999999999994, 144.5, 497.99999999999994, 183.0], 0, 2), (self.obj63,self.obj43,[325.0, 25.0, 413.0, 25.0], 0, 2), (self.obj64,self.obj34,[465.99999999999994, 464.49999999999994, 464.99999999999994, 272.0, 422.0, 272.0], 0, 3), (self.obj65,self.obj35,[102.0, 466.49999999999994, 103.0, 581.0, 171.0, 581.0], 0, 3), (self.obj66,self.obj44,[565.5, 360.5, 637.0, 361.0], 0, 2), (self.obj67,self.obj42,[181.0, 579.0, 181.0, 612.0, 282.0, 611.0], 0, 3) )

newfunction = TrafficLight

loadedMMName = 'Statechart'
