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

def behavior_DCharts_mdl(self, rootNode):

    self.globalPrecondition( rootNode )

    self.obj28=Composite(self)

    self.obj28.auto_adjust.setValue((None, 1))
    self.obj28.auto_adjust.config = 0
    self.obj28.name.setValue('Enabled')
    self.obj28.is_default.setValue((None, 1))
    self.obj28.is_default.config = 0
    self.obj28.visible.setValue((None, 1))
    self.obj28.visible.config = 0
    self.obj28.exit_action.setValue('\n\n')
    self.obj28.enter_action.setValue('\n\n')
    self.obj28.graphClass_= graph_Composite
    if self.genGraphics:
       from graph_Composite import *
       new_obj = graph_Composite(124.0,30.0,self.obj28)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Composite", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(84.0, 160.0, 84.0, 160.0))
       self.UMLmodel.coords(new_obj.connectors[1],(258.0, 160.0, 258.0, 160.0))
       self.UMLmodel.coords(new_obj.connectors[2],(171.0, 94.0, 171.0, 94.0))
       self.UMLmodel.coords(new_obj.connectors[3],(171.0, 226.0, 171.0, 226.0))
       self.UMLmodel.coords(new_obj.gf2.handler,84.0,94.0,258.0,226.0)
       self.UMLmodel.itemconfig(new_obj.gf2.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,84.0,87.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Enabled')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj28.graphObject_ = new_obj
    rootNode.addNode(self.obj28)
    self.globalAndLocalPostcondition(self.obj28, rootNode)

    self.globalPrecondition( rootNode )

    self.obj29=Basic(self)

    self.obj29.is_default.setValue((None, 1))
    self.obj29.is_default.config = 0
    self.obj29.name.setValue('Red')
    self.obj29.exit_action.setValue('\n\n\n')
    self.obj29.enter_action.setValue('\n\n\n')
    self.obj29.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(78.0,144.0,self.obj29)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(99.0, 147.0, 99.0, 147.0))
       self.UMLmodel.coords(new_obj.connectors[1],(99.0, 165.0, 99.0, 165.0))
       self.UMLmodel.coords(new_obj.connectors[2],(108.0, 156.0, 108.0, 156.0))
       self.UMLmodel.coords(new_obj.connectors[3],(91.0, 156.0, 91.0, 156.0))
       self.UMLmodel.coords(new_obj.gf3.handler,90.0,147.0,108.0,165.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,101.0,174.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Red')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj29.graphObject_ = new_obj
    rootNode.addNode(self.obj29)
    self.globalAndLocalPostcondition(self.obj29, rootNode)

    self.globalPrecondition( rootNode )

    self.obj30=Basic(self)

    self.obj30.is_default.setValue((None, 0))
    self.obj30.is_default.config = 0
    self.obj30.name.setValue('Green')
    self.obj30.exit_action.setValue('\n\n')
    self.obj30.enter_action.setValue('\n\n')
    self.obj30.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(212.0,143.0,self.obj30)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(232.99999999999997, 146.0, 232.99999999999997, 146.0))
       self.UMLmodel.coords(new_obj.connectors[1],(232.99999999999997, 164.0, 232.99999999999997, 164.0))
       self.UMLmodel.coords(new_obj.connectors[2],(242.00000000000003, 155.0, 242.00000000000003, 155.0))
       self.UMLmodel.coords(new_obj.connectors[3],(225.0, 155.0, 225.0, 155.0))
       self.UMLmodel.coords(new_obj.gf3.handler,224.0,146.0,242.0,164.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,235.0,173.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Green')
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
    self.obj31.name.setValue('Disabled')
    self.obj31.exit_action.setValue('\n\n')
    self.obj31.enter_action.setValue('\n\n')
    self.obj31.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(370.0,148.0,self.obj31)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(390.99999999999994, 151.0, 390.99999999999994, 151.0))
       self.UMLmodel.coords(new_obj.connectors[1],(390.99999999999994, 169.0, 390.99999999999994, 169.0))
       self.UMLmodel.coords(new_obj.connectors[2],(400.0, 160.0, 400.0, 160.0))
       self.UMLmodel.coords(new_obj.connectors[3],(383.0, 160.0, 383.0, 160.0))
       self.UMLmodel.coords(new_obj.gf3.handler,382.0,151.0,400.0,169.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,393.0,178.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Disabled')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj31.graphObject_ = new_obj
    rootNode.addNode(self.obj31)
    self.globalAndLocalPostcondition(self.obj31, rootNode)

    self.globalPrecondition( rootNode )

    self.obj32=contains(self)

    self.obj32.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(135.0,27.5,self.obj32)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj32.graphObject_ = new_obj
    rootNode.addNode(self.obj32)
    self.globalAndLocalPostcondition(self.obj32, rootNode)

    self.globalPrecondition( rootNode )

    self.obj33=contains(self)

    self.obj33.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(158.5,34.0,self.obj33)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj33.graphObject_ = new_obj
    rootNode.addNode(self.obj33)
    self.globalAndLocalPostcondition(self.obj33, rootNode)

    self.globalPrecondition( rootNode )

    self.obj34=Hyperedge(self)

    self.obj34.name.setValue('')
    self.obj34.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n\n')
    self.obj34.guard.setValue('1')
    self.obj34.trigger.setValue('AFTER(10)')
    self.obj34.action.setValue('\n\n')
    self.obj34.broadcast_to.setValue('')
    self.obj34.display.setValue('AFTER(10)')
    self.obj34.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(303.0,160.5,self.obj34)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj34.graphObject_ = new_obj
    rootNode.addNode(self.obj34)
    self.globalAndLocalPostcondition(self.obj34, rootNode)

    self.globalPrecondition( rootNode )

    self.obj35=Hyperedge(self)

    self.obj35.name.setValue('')
    self.obj35.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj35.guard.setValue('1')
    self.obj35.trigger.setValue('press')
    self.obj35.action.setValue('\n')
    self.obj35.broadcast_to.setValue('')
    self.obj35.display.setValue('press')
    self.obj35.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(168.0,102.5,self.obj35)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj35.graphObject_ = new_obj
    rootNode.addNode(self.obj35)
    self.globalAndLocalPostcondition(self.obj35, rootNode)

    self.globalPrecondition( rootNode )

    self.obj36=Hyperedge(self)

    self.obj36.name.setValue('')
    self.obj36.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj36.guard.setValue('1')
    self.obj36.trigger.setValue('press')
    self.obj36.action.setValue('\n')
    self.obj36.broadcast_to.setValue('')
    self.obj36.display.setValue('press')
    self.obj36.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(168.0,207.5,self.obj36)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj36.graphObject_ = new_obj
    rootNode.addNode(self.obj36)
    self.globalAndLocalPostcondition(self.obj36, rootNode)
    self.drawConnections((self.obj28,self.obj34,[258.0, 160.0, 303.0, 160.5], 0, 2), (self.obj28,self.obj32,[84.0, 160.0, 135.0, 27.500000000000004], 0, 2), (self.obj28,self.obj33,[171.0, 95.0, 158.5, 34.0], 0, 2), (self.obj29,self.obj35,[99.0, 147.0, 168.0, 102.49999999999999], 0, 2), (self.obj30,self.obj36,[232.99999999999997, 164.0, 168.0, 207.50000000000003], 0, 2), (self.obj32,self.obj29,[135.0, 27.500000000000004, 108.0, 156.0], 0, 2), (self.obj33,self.obj30,[158.5, 34.0, 232.99999999999997, 146.0], 0, 2), (self.obj34,self.obj31,[303.0, 160.5, 383.0, 160.0], 0, 2), (self.obj35,self.obj30,[168.0, 102.49999999999999, 232.99999999999997, 146.0], 0, 2), (self.obj36,self.obj29,[168.0, 207.50000000000003, 99.0, 165.0], 0, 2) )

newfunction = behavior_DCharts_mdl

loadedMMName = 'DCharts'
