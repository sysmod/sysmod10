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

def m3_DCharts_mdl(self, rootNode):

    self.globalPrecondition( rootNode )

    self.obj37=Composite(self)

    self.obj37.auto_adjust.setValue((None, 1))
    self.obj37.auto_adjust.config = 0
    self.obj37.name.setValue('AB')
    self.obj37.is_default.setValue((None, 1))
    self.obj37.is_default.config = 0
    self.obj37.visible.setValue((None, 1))
    self.obj37.visible.config = 0
    self.obj37.exit_action.setValue('\n')
    self.obj37.enter_action.setValue('\n')
    self.obj37.graphClass_= graph_Composite
    if self.genGraphics:
       from graph_Composite import *
       new_obj = graph_Composite(120.0,78.0,self.obj37)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Composite", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(184.0, 164.0, 184.0, 164.0))
       self.UMLmodel.coords(new_obj.connectors[1],(356.0, 164.0, 356.0, 164.0))
       self.UMLmodel.coords(new_obj.connectors[2],(270.0, 114.99999999999999, 270.0, 114.99999999999999))
       self.UMLmodel.coords(new_obj.connectors[3],(270.0, 214.00000000000003, 270.0, 214.00000000000003))
       self.UMLmodel.coords(new_obj.gf2.handler,184.0,115.0,356.0,214.0)
       self.UMLmodel.itemconfig(new_obj.gf2.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,184.0,108.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='AB')
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

    self.obj38.is_default.setValue((None, 1))
    self.obj38.is_default.config = 0
    self.obj38.name.setValue('A')
    self.obj38.exit_action.setValue('[DUMP("exiting state A")]\n\n')
    self.obj38.enter_action.setValue('[DUMP("entering state A")]\n\n')
    self.obj38.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(178.0,149.0,self.obj38)
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
    self.obj38.graphObject_ = new_obj
    rootNode.addNode(self.obj38)
    self.globalAndLocalPostcondition(self.obj38, rootNode)

    self.globalPrecondition( rootNode )

    self.obj39=Basic(self)

    self.obj39.is_default.setValue((None, 0))
    self.obj39.is_default.config = 0
    self.obj39.name.setValue('B')
    self.obj39.exit_action.setValue('\n\n')
    self.obj39.enter_action.setValue('\n\n')
    self.obj39.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(319.0,151.0,self.obj39)
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
    self.obj39.graphObject_ = new_obj
    rootNode.addNode(self.obj39)
    self.globalAndLocalPostcondition(self.obj39, rootNode)

    self.globalPrecondition( rootNode )

    self.obj44=Basic(self)

    self.obj44.is_default.setValue((None, 0))
    self.obj44.is_default.config = 0
    self.obj44.name.setValue('C')
    self.obj44.exit_action.setValue('[DUMP("exiting state C")]\n\n')
    self.obj44.enter_action.setValue('[DUMP("entering state C")]\n')
    self.obj44.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(452.0,152.0,self.obj44)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(472.99999999999994, 155.0, 472.99999999999994, 155.0))
       self.UMLmodel.coords(new_obj.connectors[1],(472.99999999999994, 173.0, 472.99999999999994, 173.0))
       self.UMLmodel.coords(new_obj.connectors[2],(482.0, 164.0, 482.0, 164.0))
       self.UMLmodel.coords(new_obj.connectors[3],(465.0, 164.0, 465.0, 164.0))
       self.UMLmodel.coords(new_obj.gf3.handler,464.0,155.0,482.0,173.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,475.0,182.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='C')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj44.graphObject_ = new_obj
    rootNode.addNode(self.obj44)
    self.globalAndLocalPostcondition(self.obj44, rootNode)

    self.globalPrecondition( rootNode )

    self.obj40=contains(self)

    self.obj40.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(177.5,140.0,self.obj40)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj40.graphObject_ = new_obj
    rootNode.addNode(self.obj40)
    self.globalAndLocalPostcondition(self.obj40, rootNode)

    self.globalPrecondition( rootNode )

    self.obj41=contains(self)

    self.obj41.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(236.0,140.5,self.obj41)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj41.graphObject_ = new_obj
    rootNode.addNode(self.obj41)
    self.globalAndLocalPostcondition(self.obj41, rootNode)

    self.globalPrecondition( rootNode )

    self.obj42=Hyperedge(self)

    self.obj42.name.setValue('')
    self.obj42.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj42.guard.setValue('1')
    self.obj42.trigger.setValue('e1')
    self.obj42.action.setValue('[DUMP("triggered by e1")]\n')
    self.obj42.broadcast_to.setValue('')
    self.obj42.display.setValue('e1')
    self.obj42.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(252.5,122.5,self.obj42)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj42.graphObject_ = new_obj
    rootNode.addNode(self.obj42)
    self.globalAndLocalPostcondition(self.obj42, rootNode)

    self.globalPrecondition( rootNode )

    self.obj43=Hyperedge(self)

    self.obj43.name.setValue('')
    self.obj43.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj43.guard.setValue('1')
    self.obj43.trigger.setValue('e2')
    self.obj43.action.setValue('[DUMP("triggered by e2")]\n')
    self.obj43.broadcast_to.setValue('')
    self.obj43.display.setValue('e2')
    self.obj43.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(259.5,194.5,self.obj43)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj43.graphObject_ = new_obj
    rootNode.addNode(self.obj43)
    self.globalAndLocalPostcondition(self.obj43, rootNode)

    self.globalPrecondition( rootNode )

    self.obj47=Hyperedge(self)

    self.obj47.name.setValue('')
    self.obj47.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj47.guard.setValue('1')
    self.obj47.trigger.setValue('e1')
    self.obj47.action.setValue('\n')
    self.obj47.broadcast_to.setValue('')
    self.obj47.display.setValue('e1')
    self.obj47.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(406.0,162.5,self.obj47)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj47.graphObject_ = new_obj
    rootNode.addNode(self.obj47)
    self.globalAndLocalPostcondition(self.obj47, rootNode)
    self.drawConnections((self.obj37,self.obj40,[184.0, 164.0, 177.5, 140.0], 0, 2), (self.obj37,self.obj41,[270.0, 114.99999999999999, 235.99999999999997, 140.5], 0, 2), (self.obj37,self.obj47,[356.0, 164.0, 406.0, 162.5], 0, 2), (self.obj38,self.obj42,[207.99999999999997, 161.0, 252.5, 122.50000000000001], 0, 2), (self.obj39,self.obj43,[332.0, 163.0, 259.5, 194.5], 0, 2), (self.obj40,self.obj38,[177.5, 140.0, 198.99999999999997, 152.0], 0, 2), (self.obj41,self.obj39,[235.99999999999997, 140.5, 332.0, 163.0], 0, 2), (self.obj42,self.obj39,[252.5, 122.50000000000001, 332.0, 163.0], 0, 2), (self.obj43,self.obj38,[259.5, 194.5, 207.99999999999997, 161.0], 0, 2), (self.obj47,self.obj44,[406.0, 162.5, 465.00000000000006, 164.0], 0, 2) )

newfunction = m3_DCharts_mdl

loadedMMName = 'DCharts'
