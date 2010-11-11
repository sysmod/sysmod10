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

def m1_DCharts_mdl(self, rootNode):

    self.globalPrecondition( rootNode )

    self.obj50=Basic(self)

    self.obj50.is_default.setValue((None, 1))
    self.obj50.is_default.config = 0
    self.obj50.name.setValue('A')
    self.obj50.exit_action.setValue('[DUMP("exiting state A")]\n\n')
    self.obj50.enter_action.setValue('[DUMP("entering state A")]\n\n')
    self.obj50.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(178.0,149.0,self.obj50)
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
    self.obj50.graphObject_ = new_obj
    rootNode.addNode(self.obj50)
    self.globalAndLocalPostcondition(self.obj50, rootNode)

    self.globalPrecondition( rootNode )

    self.obj51=Basic(self)

    self.obj51.is_default.setValue((None, 0))
    self.obj51.is_default.config = 0
    self.obj51.name.setValue('B')
    self.obj51.exit_action.setValue('\n\n')
    self.obj51.enter_action.setValue('\n\n')
    self.obj51.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(295.0,150.0,self.obj51)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(316.0, 153.0, 316.0, 153.0))
       self.UMLmodel.coords(new_obj.connectors[1],(316.0, 171.0, 316.0, 171.0))
       self.UMLmodel.coords(new_obj.connectors[2],(325.0, 162.0, 325.0, 162.0))
       self.UMLmodel.coords(new_obj.connectors[3],(308.0, 162.0, 308.0, 162.0))
       self.UMLmodel.coords(new_obj.gf3.handler,307.0,153.0,325.0,171.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,318.0,180.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='B')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj51.graphObject_ = new_obj
    rootNode.addNode(self.obj51)
    self.globalAndLocalPostcondition(self.obj51, rootNode)

    self.globalPrecondition( rootNode )

    self.obj52=Hyperedge(self)

    self.obj52.name.setValue('')
    self.obj52.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj52.guard.setValue('1')
    self.obj52.trigger.setValue('e1')
    self.obj52.action.setValue('[DUMP("triggered by e1")]\n')
    self.obj52.broadcast_to.setValue('')
    self.obj52.display.setValue('e1')
    self.obj52.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(247.5,116.5,self.obj52)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj52.graphObject_ = new_obj
    rootNode.addNode(self.obj52)
    self.globalAndLocalPostcondition(self.obj52, rootNode)

    self.globalPrecondition( rootNode )

    self.obj53=Hyperedge(self)

    self.obj53.name.setValue('')
    self.obj53.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj53.guard.setValue('1')
    self.obj53.trigger.setValue('e2')
    self.obj53.action.setValue('[DUMP("triggered by e2")]\n')
    self.obj53.broadcast_to.setValue('')
    self.obj53.display.setValue('e2')
    self.obj53.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(252.5,205.5,self.obj53)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj53.graphObject_ = new_obj
    rootNode.addNode(self.obj53)
    self.globalAndLocalPostcondition(self.obj53, rootNode)
    self.drawConnections((self.obj50,self.obj52,[207.99999999999997, 161.0, 247.5, 116.49999999999999], 0, 2), (self.obj51,self.obj53,[308.0, 162.0, 252.5, 205.5], 0, 2), (self.obj52,self.obj51,[247.5, 116.49999999999999, 308.0, 162.0], 0, 2), (self.obj53,self.obj50,[252.5, 205.5, 207.99999999999997, 161.0], 0, 2) )

newfunction = m1_DCharts_mdl

loadedMMName = 'DCharts'
