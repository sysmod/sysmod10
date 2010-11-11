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

def TrafficLight_and_EnvironmentBehaviour_DCharts_mdl(self, rootNode):

    self.globalPrecondition( rootNode )

    self.obj324=Composite(self)

    self.obj324.auto_adjust.setValue((None, 1))
    self.obj324.auto_adjust.config = 0
    self.obj324.name.setValue('ON')
    self.obj324.is_default.setValue((None, 1))
    self.obj324.is_default.config = 0
    self.obj324.visible.setValue((None, 1))
    self.obj324.visible.config = 0
    self.obj324.exit_action.setValue('\n')
    self.obj324.enter_action.setValue('\n')
    self.obj324.graphClass_= graph_Composite
    if self.genGraphics:
       from graph_Composite import *
       new_obj = graph_Composite(26.0,196.0,self.obj324)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Composite", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf2.handler,69.0,96.0,474.0,645.0)
       self.UMLmodel.itemconfig(new_obj.gf2.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,69.0,89.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='ON')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj324.graphObject_ = new_obj
    rootNode.addNode(self.obj324)
    self.globalAndLocalPostcondition(self.obj324, rootNode)

    self.globalPrecondition( rootNode )

    self.obj325=Composite(self)

    self.obj325.auto_adjust.setValue((None, 1))
    self.obj325.auto_adjust.config = 0
    self.obj325.name.setValue('NORMAL')
    self.obj325.is_default.setValue((None, 1))
    self.obj325.is_default.config = 0
    self.obj325.visible.setValue((None, 1))
    self.obj325.visible.config = 0
    self.obj325.exit_action.setValue('\n\n')
    self.obj325.enter_action.setValue('\n\n')
    self.obj325.graphClass_= graph_Composite
    if self.genGraphics:
       from graph_Composite import *
       new_obj = graph_Composite(230.0,145.0,self.obj325)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Composite", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf2.handler,116.0,115.0,380.0,471.0)
       self.UMLmodel.itemconfig(new_obj.gf2.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,116.0,108.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='NORMAL')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj325.graphObject_ = new_obj
    rootNode.addNode(self.obj325)
    self.globalAndLocalPostcondition(self.obj325, rootNode)

    self.globalPrecondition( rootNode )

    self.obj326=Composite(self)

    self.obj326.auto_adjust.setValue((None, 1))
    self.obj326.auto_adjust.config = 0
    self.obj326.name.setValue('FLASHING')
    self.obj326.is_default.setValue((None, 0))
    self.obj326.is_default.config = 0
    self.obj326.visible.setValue((None, 1))
    self.obj326.visible.config = 0
    self.obj326.exit_action.setValue('\n')
    self.obj326.enter_action.setValue('\n')
    self.obj326.graphClass_= graph_Composite
    if self.genGraphics:
       from graph_Composite import *
       new_obj = graph_Composite(222.0,404.0,self.obj326)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Composite", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf2.handler,121.0,527.0,365.0,638.0)
       self.UMLmodel.itemconfig(new_obj.gf2.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,121.0,520.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='FLASHING')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj326.graphObject_ = new_obj
    rootNode.addNode(self.obj326)
    self.globalAndLocalPostcondition(self.obj326, rootNode)

    self.globalPrecondition( rootNode )

    self.obj327=Composite(self)

    self.obj327.auto_adjust.setValue((None, 1))
    self.obj327.auto_adjust.config = 0
    self.obj327.name.setValue('RED')
    self.obj327.is_default.setValue((None, 1))
    self.obj327.is_default.config = 0
    self.obj327.visible.setValue((None, 1))
    self.obj327.visible.config = 0
    self.obj327.exit_action.setValue('\n\n')
    self.obj327.enter_action.setValue('\n\n')
    self.obj327.graphClass_= graph_Composite
    if self.genGraphics:
       from graph_Composite import *
       new_obj = graph_Composite(181.0,68.0,self.obj327)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Composite", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf2.handler,134.0,134.0,373.0,210.0)
       self.UMLmodel.itemconfig(new_obj.gf2.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,134.0,127.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='RED')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj327.graphObject_ = new_obj
    rootNode.addNode(self.obj327)
    self.globalAndLocalPostcondition(self.obj327, rootNode)

    self.globalPrecondition( rootNode )

    self.obj328=Basic(self)

    self.obj328.is_default.setValue((None, 0))
    self.obj328.is_default.config = 0
    self.obj328.name.setValue('GREEN')
    self.obj328.exit_action.setValue('\n\n')
    self.obj328.enter_action.setValue('\n\n')
    self.obj328.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(232.0,429.0,self.obj328)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,244.0,432.0,262.0,450.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,255.0,459.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='GREEN')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj328.graphObject_ = new_obj
    rootNode.addNode(self.obj328)
    self.globalAndLocalPostcondition(self.obj328, rootNode)

    self.globalPrecondition( rootNode )

    self.obj329=Basic(self)

    self.obj329.is_default.setValue((None, 0))
    self.obj329.is_default.config = 0
    self.obj329.name.setValue('YELLOW')
    self.obj329.exit_action.setValue('\n\n\n')
    self.obj329.enter_action.setValue('\n\n\n')
    self.obj329.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(232.0,330.0,self.obj329)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,244.0,333.0,262.0,351.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,255.0,360.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='YELLOW')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj329.graphObject_ = new_obj
    rootNode.addNode(self.obj329)
    self.globalAndLocalPostcondition(self.obj329, rootNode)

    self.globalPrecondition( rootNode )

    self.obj330=Basic(self)

    self.obj330.is_default.setValue((None, 1))
    self.obj330.is_default.config = 0
    self.obj330.name.setValue('RED_WAIT')
    self.obj330.exit_action.setValue('\n\n')
    self.obj330.enter_action.setValue('\n\n')
    self.obj330.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(313.0,168.0,self.obj330)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,325.0,171.0,343.0,189.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,336.0,198.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='RED_WAIT')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj330.graphObject_ = new_obj
    rootNode.addNode(self.obj330)
    self.globalAndLocalPostcondition(self.obj330, rootNode)

    self.globalPrecondition( rootNode )

    self.obj331=Basic(self)

    self.obj331.is_default.setValue((None, 0))
    self.obj331.is_default.config = 0
    self.obj331.name.setValue('GREEN_SOON')
    self.obj331.exit_action.setValue('\n\n')
    self.obj331.enter_action.setValue('\n\n')
    self.obj331.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(160.0,167.0,self.obj331)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,172.0,170.0,190.0,188.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,183.0,197.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='GREEN_SOON')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj331.graphObject_ = new_obj
    rootNode.addNode(self.obj331)
    self.globalAndLocalPostcondition(self.obj331, rootNode)

    self.globalPrecondition( rootNode )

    self.obj332=Basic(self)

    self.obj332.is_default.setValue((None, 1))
    self.obj332.is_default.config = 0
    self.obj332.name.setValue('YELLOW_ON')
    self.obj332.exit_action.setValue('\n\n')
    self.obj332.enter_action.setValue('\n\n')
    self.obj332.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(213.0,530.0,self.obj332)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,225.0,533.0,243.0,551.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,236.0,560.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='YELLOW_ON')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj332.graphObject_ = new_obj
    rootNode.addNode(self.obj332)
    self.globalAndLocalPostcondition(self.obj332, rootNode)

    self.globalPrecondition( rootNode )

    self.obj333=Basic(self)

    self.obj333.is_default.setValue((None, 0))
    self.obj333.is_default.config = 0
    self.obj333.name.setValue('YELLOW_OFF')
    self.obj333.exit_action.setValue('\n\n')
    self.obj333.enter_action.setValue('\n')
    self.obj333.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(219.0,596.0,self.obj333)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,231.0,599.0,249.0,617.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,242.0,626.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='YELLOW_OFF')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj333.graphObject_ = new_obj
    rootNode.addNode(self.obj333)
    self.globalAndLocalPostcondition(self.obj333, rootNode)

    self.globalPrecondition( rootNode )

    self.obj334=Basic(self)

    self.obj334.is_default.setValue((None, 0))
    self.obj334.is_default.config = 0
    self.obj334.name.setValue('OFF')
    self.obj334.exit_action.setValue('\n\n')
    self.obj334.enter_action.setValue('\n\n')
    self.obj334.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(342.0,34.0,self.obj334)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,354.0,37.0,372.0,55.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,365.0,64.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='OFF')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj334.graphObject_ = new_obj
    rootNode.addNode(self.obj334)
    self.globalAndLocalPostcondition(self.obj334, rootNode)

    self.globalPrecondition( rootNode )

    self.obj335=Basic(self)

    self.obj335.is_default.setValue((None, 0))
    self.obj335.is_default.config = 0
    self.obj335.name.setValue('DEAD')
    self.obj335.exit_action.setValue('\n\n')
    self.obj335.enter_action.setValue('\n')
    self.obj335.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(524.0,358.0,self.obj335)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,536.0,361.0,554.0,379.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,547.0,388.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='DEAD')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj335.graphObject_ = new_obj
    rootNode.addNode(self.obj335)
    self.globalAndLocalPostcondition(self.obj335, rootNode)

    self.globalPrecondition( rootNode )

    self.obj336=Basic(self)

    self.obj336.is_default.setValue((None, 1))
    self.obj336.is_default.config = 0
    self.obj336.name.setValue('u1')
    self.obj336.exit_action.setValue('\n\n\n')
    self.obj336.enter_action.setValue('\n\n\n')
    self.obj336.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(627.0,105.0,self.obj336)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,639.0,108.0,657.0,126.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,650.0,135.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='u1')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj336.graphObject_ = new_obj
    rootNode.addNode(self.obj336)
    self.globalAndLocalPostcondition(self.obj336, rootNode)

    self.globalPrecondition( rootNode )

    self.obj337=Basic(self)

    self.obj337.is_default.setValue((None, 0))
    self.obj337.is_default.config = 0
    self.obj337.name.setValue('u2')
    self.obj337.exit_action.setValue('\n\n')
    self.obj337.enter_action.setValue('\n\n')
    self.obj337.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(627.0,184.0,self.obj337)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,639.0,187.0,657.0,205.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,650.0,214.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='u2')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj337.graphObject_ = new_obj
    rootNode.addNode(self.obj337)
    self.globalAndLocalPostcondition(self.obj337, rootNode)

    self.globalPrecondition( rootNode )

    self.obj338=Basic(self)

    self.obj338.is_default.setValue((None, 0))
    self.obj338.is_default.config = 0
    self.obj338.name.setValue('u3')
    self.obj338.exit_action.setValue('\n\n')
    self.obj338.enter_action.setValue('\n\n')
    self.obj338.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(628.0,269.0,self.obj338)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,640.0,272.0,658.0,290.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,651.0,299.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='u3')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj338.graphObject_ = new_obj
    rootNode.addNode(self.obj338)
    self.globalAndLocalPostcondition(self.obj338, rootNode)

    self.globalPrecondition( rootNode )

    self.obj339=Basic(self)

    self.obj339.is_default.setValue((None, 0))
    self.obj339.is_default.config = 0
    self.obj339.name.setValue('u4')
    self.obj339.exit_action.setValue('\n\n')
    self.obj339.enter_action.setValue('\n\n')
    self.obj339.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(784.0,269.0,self.obj339)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,796.0,272.0,814.0,290.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,807.0,299.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='u4')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj339.graphObject_ = new_obj
    rootNode.addNode(self.obj339)
    self.globalAndLocalPostcondition(self.obj339, rootNode)

    self.globalPrecondition( rootNode )

    self.obj340=Basic(self)

    self.obj340.is_default.setValue((None, 0))
    self.obj340.is_default.config = 0
    self.obj340.name.setValue('u5')
    self.obj340.exit_action.setValue('\n\n')
    self.obj340.enter_action.setValue('\n\n')
    self.obj340.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(784.0,186.0,self.obj340)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,796.0,189.0,814.0,207.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,807.0,216.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='u5')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj340.graphObject_ = new_obj
    rootNode.addNode(self.obj340)
    self.globalAndLocalPostcondition(self.obj340, rootNode)

    self.globalPrecondition( rootNode )

    self.obj341=Basic(self)

    self.obj341.is_default.setValue((None, 0))
    self.obj341.is_default.config = 0
    self.obj341.name.setValue('u6')
    self.obj341.exit_action.setValue('\n\n')
    self.obj341.enter_action.setValue('\n\n')
    self.obj341.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(783.0,107.0,self.obj341)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,795.0,110.0,813.0,128.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,806.0,137.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='u6')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj341.graphObject_ = new_obj
    rootNode.addNode(self.obj341)
    self.globalAndLocalPostcondition(self.obj341, rootNode)

    self.globalPrecondition( rootNode )

    self.obj342=Basic(self)

    self.obj342.is_default.setValue((None, 1))
    self.obj342.is_default.config = 0
    self.obj342.name.setValue('idle')
    self.obj342.exit_action.setValue('\n\n\n')
    self.obj342.enter_action.setValue('\n\n\n')
    self.obj342.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(694.0,380.0,self.obj342)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,706.0,383.0,724.0,401.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,717.0,410.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='idle')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj342.graphObject_ = new_obj
    rootNode.addNode(self.obj342)
    self.globalAndLocalPostcondition(self.obj342, rootNode)

    self.globalPrecondition( rootNode )

    self.obj343=Basic(self)

    self.obj343.is_default.setValue((None, 0))
    self.obj343.is_default.config = 0
    self.obj343.name.setValue('pressed')
    self.obj343.exit_action.setValue('\n\n')
    self.obj343.enter_action.setValue('\n\n')
    self.obj343.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(747.0,566.0,self.obj343)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,759.0,569.0,777.0,587.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,770.0,596.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='pressed')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj343.graphObject_ = new_obj
    rootNode.addNode(self.obj343)
    self.globalAndLocalPostcondition(self.obj343, rootNode)

    self.globalPrecondition( rootNode )

    self.obj344=History(self)

    self.obj344.is_default.setValue((None, 0))
    self.obj344.is_default.config = 0
    self.obj344.star.setValue((None, 1))
    self.obj344.star.config = 0
    self.obj344.name.setValue('')
    self.obj344.graphClass_= graph_History
    if self.genGraphics:
       from graph_History import *
       new_obj = graph_History(408.0,200.0,self.obj344)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("History", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf0.handler,411.0,203.0,447.0,238.0)
       self.UMLmodel.itemconfig(new_obj.gf0.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf0.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf0.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf0.handler, fill='lightblue')
       self.UMLmodel.coords(new_obj.gf1.handler,428.0,222.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='H')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       self.UMLmodel.coords(new_obj.gf2.handler,436.0,222.0)
       self.UMLmodel.itemconfig(new_obj.gf2.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, text='*')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, justify='left')
       self.UMLmodel.coords(new_obj.gf3.handler,431.0,247.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='blue')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, text='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, justify='left')
    else: new_obj = None
    self.obj344.graphObject_ = new_obj
    rootNode.addNode(self.obj344)
    self.globalAndLocalPostcondition(self.obj344, rootNode)

    self.globalPrecondition( rootNode )

    self.obj345=Orthogonal(self)

    self.obj345.visible.setValue((None, 1))
    self.obj345.visible.config = 0
    self.obj345.name.setValue('police')
    self.obj345.auto_adjust.setValue((None, 1))
    self.obj345.auto_adjust.config = 0
    self.obj345.graphClass_= graph_Orthogonal
    if self.genGraphics:
       from graph_Orthogonal import *
       new_obj = graph_Orthogonal(552.0,43.0,self.obj345)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Orthogonal", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf5.handler,627.0,70.0,879.0,331.0)
       self.UMLmodel.itemconfig(new_obj.gf5.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, outline='DARKGRAY')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,627.0,63.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='police')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj345.graphObject_ = new_obj
    rootNode.addNode(self.obj345)
    self.globalAndLocalPostcondition(self.obj345, rootNode)

    self.globalPrecondition( rootNode )

    self.obj346=Orthogonal(self)

    self.obj346.visible.setValue((None, 1))
    self.obj346.visible.config = 0
    self.obj346.name.setValue('TrafficLight')
    self.obj346.auto_adjust.setValue((None, 1))
    self.obj346.auto_adjust.config = 0
    self.obj346.graphClass_= graph_Orthogonal
    if self.genGraphics:
       from graph_Orthogonal import *
       new_obj = graph_Orthogonal(4.0,61.0,self.obj346)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Orthogonal", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf5.handler,54.0,31.0,571.0,652.0)
       self.UMLmodel.itemconfig(new_obj.gf5.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, outline='DARKGRAY')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,54.0,24.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='TrafficLight')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj346.graphObject_ = new_obj
    rootNode.addNode(self.obj346)
    self.globalAndLocalPostcondition(self.obj346, rootNode)

    self.globalPrecondition( rootNode )

    self.obj347=Orthogonal(self)

    self.obj347.visible.setValue((None, 1))
    self.obj347.visible.config = 0
    self.obj347.name.setValue('pedestrian')
    self.obj347.auto_adjust.setValue((None, 1))
    self.obj347.auto_adjust.config = 0
    self.obj347.graphClass_= graph_Orthogonal
    if self.genGraphics:
       from graph_Orthogonal import *
       new_obj = graph_Orthogonal(608.0,355.0,self.obj347)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Orthogonal", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf5.handler,628.0,377.0,888.0,608.0)
       self.UMLmodel.itemconfig(new_obj.gf5.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, outline='DARKGRAY')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,628.0,370.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='pedestrian')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj347.graphObject_ = new_obj
    rootNode.addNode(self.obj347)
    self.globalAndLocalPostcondition(self.obj347, rootNode)

    self.globalPrecondition( rootNode )

    self.obj348=contains(self)

    self.obj348.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(174.5,263.5,self.obj348)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj348.graphObject_ = new_obj
    rootNode.addNode(self.obj348)
    self.globalAndLocalPostcondition(self.obj348, rootNode)

    self.globalPrecondition( rootNode )

    self.obj349=contains(self)

    self.obj349.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(275.0,271.5,self.obj349)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj349.graphObject_ = new_obj
    rootNode.addNode(self.obj349)
    self.globalAndLocalPostcondition(self.obj349, rootNode)

    self.globalPrecondition( rootNode )

    self.obj350=contains(self)

    self.obj350.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(232.0,373.0,self.obj350)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj350.graphObject_ = new_obj
    rootNode.addNode(self.obj350)
    self.globalAndLocalPostcondition(self.obj350, rootNode)

    self.globalPrecondition( rootNode )

    self.obj351=contains(self)

    self.obj351.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(261.0,281.0,self.obj351)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj351.graphObject_ = new_obj
    rootNode.addNode(self.obj351)
    self.globalAndLocalPostcondition(self.obj351, rootNode)

    self.globalPrecondition( rootNode )

    self.obj352=contains(self)

    self.obj352.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(240.0,284.5,self.obj352)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj352.graphObject_ = new_obj
    rootNode.addNode(self.obj352)
    self.globalAndLocalPostcondition(self.obj352, rootNode)

    self.globalPrecondition( rootNode )

    self.obj353=contains(self)

    self.obj353.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(310.0,-306.5,self.obj353)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj353.graphObject_ = new_obj
    rootNode.addNode(self.obj353)
    self.globalAndLocalPostcondition(self.obj353, rootNode)

    self.globalPrecondition( rootNode )

    self.obj354=contains(self)

    self.obj354.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(248.0,-306.0,self.obj354)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj354.graphObject_ = new_obj
    rootNode.addNode(self.obj354)
    self.globalAndLocalPostcondition(self.obj354, rootNode)

    self.globalPrecondition( rootNode )

    self.obj355=contains(self)

    self.obj355.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(261.5,269.5,self.obj355)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj355.graphObject_ = new_obj
    rootNode.addNode(self.obj355)
    self.globalAndLocalPostcondition(self.obj355, rootNode)

    self.globalPrecondition( rootNode )

    self.obj356=contains(self)

    self.obj356.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(107.0,477.5,self.obj356)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj356.graphObject_ = new_obj
    rootNode.addNode(self.obj356)
    self.globalAndLocalPostcondition(self.obj356, rootNode)

    self.globalPrecondition( rootNode )

    self.obj357=contains(self)

    self.obj357.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(109.0,517.5,self.obj357)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj357.graphObject_ = new_obj
    rootNode.addNode(self.obj357)
    self.globalAndLocalPostcondition(self.obj357, rootNode)

    self.globalPrecondition( rootNode )

    self.obj358=contains(self)

    self.obj358.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(425.0,-3.5,self.obj358)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj358.graphObject_ = new_obj
    rootNode.addNode(self.obj358)
    self.globalAndLocalPostcondition(self.obj358, rootNode)

    self.globalPrecondition( rootNode )

    self.obj359=contains(self)

    self.obj359.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(503.0,-2.5,self.obj359)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj359.graphObject_ = new_obj
    rootNode.addNode(self.obj359)
    self.globalAndLocalPostcondition(self.obj359, rootNode)

    self.globalPrecondition( rootNode )

    self.obj360=contains(self)

    self.obj360.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(425.0,36.0,self.obj360)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj360.graphObject_ = new_obj
    rootNode.addNode(self.obj360)
    self.globalAndLocalPostcondition(self.obj360, rootNode)

    self.globalPrecondition( rootNode )

    self.obj361=contains(self)

    self.obj361.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(503.5,37.0,self.obj361)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj361.graphObject_ = new_obj
    rootNode.addNode(self.obj361)
    self.globalAndLocalPostcondition(self.obj361, rootNode)

    self.globalPrecondition( rootNode )

    self.obj362=contains(self)

    self.obj362.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(425.5,78.5,self.obj362)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj362.graphObject_ = new_obj
    rootNode.addNode(self.obj362)
    self.globalAndLocalPostcondition(self.obj362, rootNode)

    self.globalPrecondition( rootNode )

    self.obj363=contains(self)

    self.obj363.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(503.5,78.5,self.obj363)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj363.graphObject_ = new_obj
    rootNode.addNode(self.obj363)
    self.globalAndLocalPostcondition(self.obj363, rootNode)

    self.globalPrecondition( rootNode )

    self.obj364=contains(self)

    self.obj364.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(7.0,185.5,self.obj364)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj364.graphObject_ = new_obj
    rootNode.addNode(self.obj364)
    self.globalAndLocalPostcondition(self.obj364, rootNode)

    self.globalPrecondition( rootNode )

    self.obj365=contains(self)

    self.obj365.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(168.0,96.0,self.obj365)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj365.graphObject_ = new_obj
    rootNode.addNode(self.obj365)
    self.globalAndLocalPostcondition(self.obj365, rootNode)

    self.globalPrecondition( rootNode )

    self.obj366=contains(self)

    self.obj366.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(280.0,264.0,self.obj366)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj366.graphObject_ = new_obj
    rootNode.addNode(self.obj366)
    self.globalAndLocalPostcondition(self.obj366, rootNode)

    self.globalPrecondition( rootNode )

    self.obj367=contains(self)

    self.obj367.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(277.5,691.0,self.obj367)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj367.graphObject_ = new_obj
    rootNode.addNode(self.obj367)
    self.globalAndLocalPostcondition(self.obj367, rootNode)

    self.globalPrecondition( rootNode )

    self.obj368=contains(self)

    self.obj368.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(288.0,827.5,self.obj368)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj368.graphObject_ = new_obj
    rootNode.addNode(self.obj368)
    self.globalAndLocalPostcondition(self.obj368, rootNode)

    self.globalPrecondition( rootNode )

    self.obj369=Hyperedge(self)

    self.obj369.name.setValue('')
    self.obj369.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj369.guard.setValue('1')
    self.obj369.trigger.setValue('AFTER(6)')
    self.obj369.action.setValue('\n')
    self.obj369.broadcast_to.setValue('')
    self.obj369.display.setValue('AFTER(6)')
    self.obj369.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(232.0,179.5,self.obj369)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj369.graphObject_ = new_obj
    rootNode.addNode(self.obj369)
    self.globalAndLocalPostcondition(self.obj369, rootNode)

    self.globalPrecondition( rootNode )

    self.obj370=Hyperedge(self)

    self.obj370.name.setValue('')
    self.obj370.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj370.guard.setValue('1')
    self.obj370.trigger.setValue('CROSSWALK')
    self.obj370.action.setValue('\n')
    self.obj370.broadcast_to.setValue('')
    self.obj370.display.setValue('CROSSWALK')
    self.obj370.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(229.0,142.5,self.obj370)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj370.graphObject_ = new_obj
    rootNode.addNode(self.obj370)
    self.globalAndLocalPostcondition(self.obj370, rootNode)

    self.globalPrecondition( rootNode )

    self.obj371=Hyperedge(self)

    self.obj371.name.setValue('')
    self.obj371.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj371.guard.setValue('1')
    self.obj371.trigger.setValue('AFTER(5)')
    self.obj371.action.setValue('\n')
    self.obj371.broadcast_to.setValue('')
    self.obj371.display.setValue('AFTER(5)')
    self.obj371.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(254.0,395.5,self.obj371)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj371.graphObject_ = new_obj
    rootNode.addNode(self.obj371)
    self.globalAndLocalPostcondition(self.obj371, rootNode)

    self.globalPrecondition( rootNode )

    self.obj372=Hyperedge(self)

    self.obj372.name.setValue('')
    self.obj372.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj372.guard.setValue('1')
    self.obj372.trigger.setValue('AFTER(2)')
    self.obj372.action.setValue('\n')
    self.obj372.broadcast_to.setValue('')
    self.obj372.display.setValue('AFTER(2)')
    self.obj372.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(252.5,280.5,self.obj372)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj372.graphObject_ = new_obj
    rootNode.addNode(self.obj372)
    self.globalAndLocalPostcondition(self.obj372, rootNode)

    self.globalPrecondition( rootNode )

    self.obj373=Hyperedge(self)

    self.obj373.name.setValue('')
    self.obj373.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj373.guard.setValue('1')
    self.obj373.trigger.setValue('AFTER(2)')
    self.obj373.action.setValue('\n')
    self.obj373.broadcast_to.setValue('')
    self.obj373.display.setValue('AFTER(2)')
    self.obj373.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(181.0,246.0,self.obj373)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj373.graphObject_ = new_obj
    rootNode.addNode(self.obj373)
    self.globalAndLocalPostcondition(self.obj373, rootNode)

    self.globalPrecondition( rootNode )

    self.obj374=Hyperedge(self)

    self.obj374.name.setValue('')
    self.obj374.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj374.guard.setValue('1')
    self.obj374.trigger.setValue('AFTER(0.5)')
    self.obj374.action.setValue('\n')
    self.obj374.broadcast_to.setValue('')
    self.obj374.display.setValue('AFTER(0.5)')
    self.obj374.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(298.0,581.0,self.obj374)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj374.graphObject_ = new_obj
    rootNode.addNode(self.obj374)
    self.globalAndLocalPostcondition(self.obj374, rootNode)

    self.globalPrecondition( rootNode )

    self.obj375=Hyperedge(self)

    self.obj375.name.setValue('')
    self.obj375.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj375.guard.setValue('1')
    self.obj375.trigger.setValue('ON-OFF')
    self.obj375.action.setValue('\n')
    self.obj375.broadcast_to.setValue('')
    self.obj375.display.setValue('ON-OFF')
    self.obj375.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(430.0,166.5,self.obj375)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj375.graphObject_ = new_obj
    rootNode.addNode(self.obj375)
    self.globalAndLocalPostcondition(self.obj375, rootNode)

    self.globalPrecondition( rootNode )

    self.obj376=Hyperedge(self)

    self.obj376.name.setValue('')
    self.obj376.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj376.guard.setValue('1')
    self.obj376.trigger.setValue('ON-OFF')
    self.obj376.action.setValue('\n')
    self.obj376.broadcast_to.setValue('')
    self.obj376.display.setValue('ON-OFF')
    self.obj376.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(284.0,46.0,self.obj376)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj376.graphObject_ = new_obj
    rootNode.addNode(self.obj376)
    self.globalAndLocalPostcondition(self.obj376, rootNode)

    self.globalPrecondition( rootNode )

    self.obj377=Hyperedge(self)

    self.obj377.name.setValue('')
    self.obj377.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj377.guard.setValue('1')
    self.obj377.trigger.setValue('POLICE')
    self.obj377.action.setValue('\n')
    self.obj377.broadcast_to.setValue('')
    self.obj377.display.setValue('POLICE')
    self.obj377.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(417.0,485.5,self.obj377)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj377.graphObject_ = new_obj
    rootNode.addNode(self.obj377)
    self.globalAndLocalPostcondition(self.obj377, rootNode)

    self.globalPrecondition( rootNode )

    self.obj378=Hyperedge(self)

    self.obj378.name.setValue('')
    self.obj378.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj378.guard.setValue('1')
    self.obj378.trigger.setValue('POLICE')
    self.obj378.action.setValue('\n')
    self.obj378.broadcast_to.setValue('')
    self.obj378.display.setValue('POLICE')
    self.obj378.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(78.0,481.5,self.obj378)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj378.graphObject_ = new_obj
    rootNode.addNode(self.obj378)
    self.globalAndLocalPostcondition(self.obj378, rootNode)

    self.globalPrecondition( rootNode )

    self.obj379=Hyperedge(self)

    self.obj379.name.setValue('')
    self.obj379.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj379.guard.setValue('1')
    self.obj379.trigger.setValue('QUIT')
    self.obj379.action.setValue('\n')
    self.obj379.broadcast_to.setValue('')
    self.obj379.display.setValue('QUIT')
    self.obj379.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(482.5,369.5,self.obj379)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj379.graphObject_ = new_obj
    rootNode.addNode(self.obj379)
    self.globalAndLocalPostcondition(self.obj379, rootNode)

    self.globalPrecondition( rootNode )

    self.obj380=Hyperedge(self)

    self.obj380.name.setValue('')
    self.obj380.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj380.guard.setValue('1')
    self.obj380.trigger.setValue('AFTER(0.5)')
    self.obj380.action.setValue('\n')
    self.obj380.broadcast_to.setValue('')
    self.obj380.display.setValue('AFTER(0.5)')
    self.obj380.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(131.0,576.0,self.obj380)
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
    self.obj381.trigger.setValue('AFTER(20)')
    self.obj381.action.setValue('[EVENT("POLICE")]\n\n')
    self.obj381.broadcast_to.setValue('')
    self.obj381.display.setValue('tm(20)/POLICE')
    self.obj381.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(649.0,154.0,self.obj381)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj381.graphObject_ = new_obj
    rootNode.addNode(self.obj381)
    self.globalAndLocalPostcondition(self.obj381, rootNode)

    self.globalPrecondition( rootNode )

    self.obj382=Hyperedge(self)

    self.obj382.name.setValue('')
    self.obj382.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n\n')
    self.obj382.guard.setValue('1')
    self.obj382.trigger.setValue('AFTER(20)')
    self.obj382.action.setValue('[EVENT("ON-OFF")]\n\n')
    self.obj382.broadcast_to.setValue('')
    self.obj382.display.setValue('tm(20)/ON-OFF')
    self.obj382.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(648.5,237.0,self.obj382)
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
    self.obj383.trigger.setValue('AFTER(5)')
    self.obj383.action.setValue('[EVENT("POLICE")]\n')
    self.obj383.broadcast_to.setValue('')
    self.obj383.display.setValue('tm(5)/POLICE')
    self.obj383.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(704.0,312.0,self.obj383)
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
    self.obj384.trigger.setValue('AFTER(1)')
    self.obj384.action.setValue('[EVENT("ON-OFF")]\n')
    self.obj384.broadcast_to.setValue('')
    self.obj384.display.setValue('tm(1)/ON-OFF')
    self.obj384.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(804.0,235.0,self.obj384)
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
    self.obj385.trigger.setValue('AFTER(3)')
    self.obj385.action.setValue('[EVENT("POLICE")]\n')
    self.obj385.broadcast_to.setValue('')
    self.obj385.display.setValue('tm(3)/POLICE')
    self.obj385.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(804.5,154.0,self.obj385)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj385.graphObject_ = new_obj
    rootNode.addNode(self.obj385)
    self.globalAndLocalPostcondition(self.obj385, rootNode)

    self.globalPrecondition( rootNode )

    self.obj386=Hyperedge(self)

    self.obj386.name.setValue('')
    self.obj386.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj386.guard.setValue('1')
    self.obj386.trigger.setValue('AFTER(10)')
    self.obj386.action.setValue('\n')
    self.obj386.broadcast_to.setValue('')
    self.obj386.display.setValue('tm(10)')
    self.obj386.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(778.0,78.0,self.obj386)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj386.graphObject_ = new_obj
    rootNode.addNode(self.obj386)
    self.globalAndLocalPostcondition(self.obj386, rootNode)

    self.globalPrecondition( rootNode )

    self.obj387=Hyperedge(self)

    self.obj387.name.setValue('')
    self.obj387.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n\n')
    self.obj387.guard.setValue('1')
    self.obj387.trigger.setValue('AFTER(5)')
    self.obj387.action.setValue('[EVENT("CROSSWALK")]\n\n')
    self.obj387.broadcast_to.setValue('')
    self.obj387.display.setValue('tm(5)/CROSSWALK')
    self.obj387.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(660.0,504.0,self.obj387)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj387.graphObject_ = new_obj
    rootNode.addNode(self.obj387)
    self.globalAndLocalPostcondition(self.obj387, rootNode)

    self.globalPrecondition( rootNode )

    self.obj388=Hyperedge(self)

    self.obj388.name.setValue('')
    self.obj388.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n\n')
    self.obj388.guard.setValue('[INSTATE("TrafficLight.ON.NORMAL.GREEN",0)]')
    self.obj388.trigger.setValue('')
    self.obj388.action.setValue('[DUMP("Crossing the intersection")]\n\n')
    self.obj388.broadcast_to.setValue('')
    self.obj388.display.setValue('[TrafficLight in ON.NORMAL.GREEN')
    self.obj388.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(778.0,476.5,self.obj388)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj388.graphObject_ = new_obj
    rootNode.addNode(self.obj388)
    self.globalAndLocalPostcondition(self.obj388, rootNode)
    self.drawConnections((self.obj324,self.obj348,[79.0, 222.0, 174.5, 263.5], 0, 2), (self.obj324,self.obj349,[283.0, 96.000000000000014, 275.0, 271.5], 0, 2), (self.obj324,self.obj350,[154.0, 289.0, 232.0, 373.0], 0, 2), (self.obj324,self.obj376,[283.0, 96.000000000000014, 284.0, 46.0], 0, 2), (self.obj324,self.obj379,[474.0, 370.0, 482.5, 369.5], 0, 2), (self.obj325,self.obj351,[248.0, 471.0, 261.0, 281.0], 0, 2), (self.obj325,self.obj352,[248.0, 471.0, 240.0, 284.5], 0, 2), (self.obj325,self.obj355,[116.0, 293.0, 261.5, 269.5], 0, 2), (self.obj325,self.obj378,[116.0, 293.0, 77.0, 292.0, 78.0, 481.5], 0, 3), (self.obj326,self.obj356,[121.00000000000001, 582.0, 107.00000000000001, 477.50000000000006], 0, 2), (self.obj326,self.obj357,[243.0, 527.0, 109.0, 517.5], 0, 2), (self.obj326,self.obj377,[365.0, 582.0, 417.0, 582.0, 417.0, 485.49999999999994], 0, 3), (self.obj327,self.obj353,[373.0, 198.99999999999997, 310.0, -306.5], 0, 2), (self.obj327,self.obj354,[134.0, 198.99999999999997, 248.0, -306.0], 0, 2), (self.obj328,self.obj371,[253.0, 432.0, 254.0, 395.5], 0, 2), (self.obj329,self.obj372,[253.0, 333.0, 252.5, 280.5], 0, 2), (self.obj330,self.obj369,[326.0, 180.0, 232.0, 179.5], 0, 2), (self.obj330,self.obj370,[334.0, 171.0, 334.0, 142.0, 229.0, 142.5], 0, 3), (self.obj331,self.obj373,[181.0, 188.0, 181.0, 246.0], 0, 2), (self.obj332,self.obj380,[226.0, 542.0, 131.0, 542.0, 131.0, 576.0], 0, 3), (self.obj333,self.obj374,[248.99999999999997, 608.0, 298.0, 609.0, 298.0, 581.0], 0, 3), (self.obj334,self.obj375,[372.0, 46.0, 430.0, 46.0, 430.0, 166.5], 0, 3), (self.obj336,self.obj381,[648.0, 125.99999999999999, 649.0, 154.0], 0, 2), (self.obj337,self.obj382,[648.0, 204.99999999999997, 648.5, 237.0], 0, 2), (self.obj338,self.obj383,[658.0, 281.0, 704.0, 312.0], 0, 2), (self.obj339,self.obj384,[805.00000000000011, 272.0, 804.0, 235.0], 0, 2), (self.obj340,self.obj385,[805.00000000000011, 189.00000000000003, 804.5, 154.0], 0, 2), (self.obj341,self.obj386,[804.0, 110.00000000000001, 778.0, 78.0], 0, 2), (self.obj342,self.obj387,[707.0, 392.0, 660.0, 503.99999999999994], 0, 2), (self.obj343,self.obj388,[768.00000000000011, 569.0, 778.0, 476.5], 0, 2), (self.obj345,self.obj358,[879.0, 200.0, 425.0, -3.4999999999999996], 0, 2), (self.obj345,self.obj359,[879.0, 200.0, 503.00000000000006, -2.5], 0, 2), (self.obj345,self.obj360,[626.0, 200.0, 425.0, 36.0], 0, 2), (self.obj345,self.obj361,[626.0, 200.0, 503.49999999999994, 37.0], 0, 2), (self.obj345,self.obj362,[626.0, 200.0, 425.5, 78.5], 0, 2), (self.obj345,self.obj363,[626.0, 200.0, 503.49999999999994, 78.5], 0, 2), (self.obj346,self.obj364,[312.0, 652.0, 6.9999999999999991, 185.5], 0, 2), (self.obj346,self.obj365,[312.0, 31.0, 168.0, 96.000000000000014], 0, 2), (self.obj346,self.obj366,[312.0, 31.0, 280.0, 264.0], 0, 2), (self.obj347,self.obj367,[912.0, 494.0, 277.5, 691.0], 0, 2), (self.obj347,self.obj368,[717.0, 531.0, 288.0, 827.5], 0, 2), (self.obj348,self.obj325,[174.5, 263.5, 116.0, 293.0], 0, 2), (self.obj349,self.obj326,[275.0, 271.5, 204.0, 535.0], 0, 2), (self.obj350,self.obj344,[232.0, 373.0, 411.0, 222.0], 0, 2), (self.obj351,self.obj328,[261.0, 281.0, 253.0, 432.0], 0, 2), (self.obj352,self.obj329,[240.0, 284.5, 253.0, 333.0], 0, 2), (self.obj353,self.obj330,[310.0, -306.5, 326.0, 180.0], 0, 2), (self.obj354,self.obj331,[248.0, -306.0, 181.0, 170.0], 0, 2), (self.obj355,self.obj327,[261.5, 269.5, 253.0, 134.0], 0, 2), (self.obj356,self.obj332,[107.00000000000001, 477.50000000000006, 243.0, 542.0], 0, 2), (self.obj357,self.obj333,[109.0, 517.5, 248.99999999999997, 608.0], 0, 2), (self.obj358,self.obj336,[425.0, -3.4999999999999996, 648.0, 108.0], 0, 2), (self.obj359,self.obj341,[503.00000000000006, -2.5, 795.99999999999989, 119.0], 0, 2), (self.obj360,self.obj337,[425.0, 36.0, 648.0, 187.0], 0, 2), (self.obj361,self.obj340,[503.49999999999994, 37.0, 797.0, 198.0], 0, 2), (self.obj362,self.obj338,[425.5, 78.5, 649.0, 272.0], 0, 2), (self.obj363,self.obj339,[503.49999999999994, 78.5, 805.00000000000011, 272.0], 0, 2), (self.obj364,self.obj324,[6.9999999999999991, 185.5, 69.0, 370.0], 0, 2), (self.obj365,self.obj334,[168.0, 96.000000000000014, 355.0, 46.0], 0, 2), (self.obj366,self.obj335,[280.0, 264.0, 537.0, 370.0], 0, 2), (self.obj367,self.obj342,[277.5, 691.0, 707.0, 392.0], 0, 2), (self.obj368,self.obj343,[288.0, 827.5, 768.00000000000011, 569.0], 0, 2), (self.obj369,self.obj331,[232.0, 179.5, 190.0, 179.0], 0, 2), (self.obj370,self.obj331,[229.0, 142.5, 181.0, 143.0, 181.0, 170.0], 0, 3), (self.obj371,self.obj329,[254.0, 395.5, 253.0, 351.0], 0, 2), (self.obj372,self.obj327,[252.5, 280.5, 253.0, 210.0], 0, 2), (self.obj373,self.obj328,[181.0, 246.0, 180.0, 375.0, 181.0, 440.99999999999994, 245.00000000000003, 440.99999999999994], 0, 4), (self.obj374,self.obj332,[298.0, 581.0, 297.0, 542.0, 243.0, 542.0], 0, 3), (self.obj375,self.obj344,[430.0, 166.5, 428.99999999999994, 203.0], 0, 2), (self.obj376,self.obj334,[284.0, 46.0, 355.0, 46.0], 0, 2), (self.obj377,self.obj325,[417.0, 485.49999999999994, 417.0, 294.0, 380.0, 293.0], 0, 3), (self.obj378,self.obj326,[78.0, 481.5, 77.0, 579.0, 121.00000000000001, 578.0], 0, 3), (self.obj379,self.obj335,[482.5, 369.5, 537.0, 370.0], 0, 2), (self.obj380,self.obj333,[131.0, 576.0, 131.0, 609.0, 232.0, 608.0], 0, 3), (self.obj381,self.obj337,[649.0, 154.0, 648.0, 187.0], 0, 2), (self.obj382,self.obj338,[648.5, 237.0, 649.0, 272.0], 0, 2), (self.obj383,self.obj339,[704.0, 312.0, 797.0, 281.0], 0, 2), (self.obj384,self.obj340,[804.0, 235.0, 805.00000000000011, 207.0], 0, 2), (self.obj385,self.obj341,[804.5, 154.0, 804.0, 128.0], 0, 2), (self.obj386,self.obj336,[778.0, 78.0, 657.0, 117.0], 0, 2), (self.obj387,self.obj343,[660.0, 503.99999999999994, 768.00000000000011, 569.0], 0, 2), (self.obj388,self.obj342,[778.0, 476.5, 724.0, 392.0], 0, 2) )

newfunction = TrafficLight_and_EnvironmentBehaviour_DCharts_mdl

loadedMMName = 'DCharts'
