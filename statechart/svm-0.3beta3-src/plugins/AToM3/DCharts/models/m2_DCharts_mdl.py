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

def m2_DCharts_mdl(self, rootNode):

    self.globalPrecondition( rootNode )

    self.obj80=Composite(self)

    self.obj80.auto_adjust.setValue((None, 1))
    self.obj80.auto_adjust.config = 0
    self.obj80.name.setValue('AB')
    self.obj80.is_default.setValue((None, 1))
    self.obj80.is_default.config = 0
    self.obj80.visible.setValue((None, 1))
    self.obj80.visible.config = 0
    self.obj80.exit_action.setValue('\n')
    self.obj80.enter_action.setValue('\n')
    self.obj80.graphClass_= graph_Composite
    if self.genGraphics:
       from graph_Composite import *
       new_obj = graph_Composite(120.0,78.0,self.obj80)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Composite", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(184.0, 166.0, 184.0, 166.0))
       self.UMLmodel.coords(new_obj.connectors[1],(356.0, 166.0, 356.0, 166.0))
       self.UMLmodel.coords(new_obj.connectors[2],(270.0, 108.0, 270.0, 108.0))
       self.UMLmodel.coords(new_obj.connectors[3],(270.0, 225.0, 270.0, 225.0))
       self.UMLmodel.coords(new_obj.gf2.handler,184.0,108.0,356.0,225.0)
       self.UMLmodel.itemconfig(new_obj.gf2.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,184.0,101.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='AB')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj80.graphObject_ = new_obj
    rootNode.addNode(self.obj80)
    self.globalAndLocalPostcondition(self.obj80, rootNode)

    self.globalPrecondition( rootNode )

    self.obj81=Basic(self)

    self.obj81.is_default.setValue((None, 1))
    self.obj81.is_default.config = 0
    self.obj81.name.setValue('A')
    self.obj81.exit_action.setValue('[DUMP("exiting state A")]\n\n')
    self.obj81.enter_action.setValue('[DUMP("entering state A")]\n\n')
    self.obj81.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(178.0,149.0,self.obj81)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(198.99999999999997, 152.0, 198.99999999999997, 152.0))
       self.UMLmodel.coords(new_obj.connectors[1],(198.99999999999997, 170.0, 198.99999999999997, 170.0))
       self.UMLmodel.coords(new_obj.connectors[2],(207.99999999999997, 161.0, 207.99999999999997, 161.0))
       self.UMLmodel.coords(new_obj.connectors[3],(191.0, 161.0, 191.0, 161.0))
       self.UMLmodel.coords(new_obj.gf3.handler,190.0,152.0,208.0,170.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,201.0,179.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='A')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj81.graphObject_ = new_obj
    rootNode.addNode(self.obj81)
    self.globalAndLocalPostcondition(self.obj81, rootNode)

    self.globalPrecondition( rootNode )

    self.obj82=Basic(self)

    self.obj82.is_default.setValue((None, 0))
    self.obj82.is_default.config = 0
    self.obj82.name.setValue('B')
    self.obj82.exit_action.setValue('\n\n')
    self.obj82.enter_action.setValue('\n\n')
    self.obj82.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(319.0,151.0,self.obj82)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(340.0, 154.0, 340.0, 154.0))
       self.UMLmodel.coords(new_obj.connectors[1],(340.0, 172.0, 340.0, 172.0))
       self.UMLmodel.coords(new_obj.connectors[2],(349.0, 163.0, 349.0, 163.0))
       self.UMLmodel.coords(new_obj.connectors[3],(332.0, 163.0, 332.0, 163.0))
       self.UMLmodel.coords(new_obj.gf3.handler,331.0,154.0,349.0,172.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,342.0,181.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='B')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj82.graphObject_ = new_obj
    rootNode.addNode(self.obj82)
    self.globalAndLocalPostcondition(self.obj82, rootNode)

    self.globalPrecondition( rootNode )

    self.obj83=contains(self)

    self.obj83.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(177.5,140.0,self.obj83)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj83.graphObject_ = new_obj
    rootNode.addNode(self.obj83)
    self.globalAndLocalPostcondition(self.obj83, rootNode)

    self.globalPrecondition( rootNode )

    self.obj84=contains(self)

    self.obj84.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(236.0,140.5,self.obj84)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj84.graphObject_ = new_obj
    rootNode.addNode(self.obj84)
    self.globalAndLocalPostcondition(self.obj84, rootNode)

    self.globalPrecondition( rootNode )

    self.obj85=Hyperedge(self)

    self.obj85.name.setValue('')
    self.obj85.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj85.guard.setValue('1')
    self.obj85.trigger.setValue('e1')
    self.obj85.action.setValue('[DUMP("triggered by e1")]\n')
    self.obj85.broadcast_to.setValue('')
    self.obj85.display.setValue('e1')
    self.obj85.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(247.5,116.5,self.obj85)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj85.graphObject_ = new_obj
    rootNode.addNode(self.obj85)
    self.globalAndLocalPostcondition(self.obj85, rootNode)

    self.globalPrecondition( rootNode )

    self.obj86=Hyperedge(self)

    self.obj86.name.setValue('')
    self.obj86.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj86.guard.setValue('1')
    self.obj86.trigger.setValue('e2')
    self.obj86.action.setValue('[DUMP("triggered by e2")]\n')
    self.obj86.broadcast_to.setValue('')
    self.obj86.display.setValue('e2')
    self.obj86.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(252.5,205.5,self.obj86)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj86.graphObject_ = new_obj
    rootNode.addNode(self.obj86)
    self.globalAndLocalPostcondition(self.obj86, rootNode)
    self.drawConnections((self.obj80,self.obj83,[184.0, 166.0, 177.5, 140.0], 0, 2), (self.obj80,self.obj84,[270.0, 108.0, 235.99999999999997, 140.5], 0, 2), (self.obj81,self.obj85,[207.99999999999997, 161.0, 247.5, 116.49999999999999], 0, 2), (self.obj82,self.obj86,[332.0, 163.0, 252.5, 205.5], 0, 2), (self.obj83,self.obj81,[177.5, 140.0, 198.99999999999997, 152.0], 0, 2), (self.obj84,self.obj82,[235.99999999999997, 140.5, 332.0, 163.0], 0, 2), (self.obj85,self.obj82,[247.5, 116.49999999999999, 332.0, 163.0], 0, 2), (self.obj86,self.obj81,[252.5, 205.5, 207.99999999999997, 161.0], 0, 2) )

newfunction = m2_DCharts_mdl

loadedMMName = 'DCharts'
