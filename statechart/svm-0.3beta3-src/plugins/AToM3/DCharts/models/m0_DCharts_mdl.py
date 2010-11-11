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

def m0_DCharts_mdl(self, rootNode):

    self.globalPrecondition( rootNode )

    self.obj39=Basic(self)

    self.obj39.is_default.setValue((None, 1))
    self.obj39.is_default.config = 0
    self.obj39.name.setValue('A')
    self.obj39.exit_action.setValue('[DUMP("exiting A")]\n\n')
    self.obj39.enter_action.setValue('[DUMP("entering A")]\n\n\n')
    self.obj39.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(172.0,102.0,self.obj39)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(193.0, 105.0, 193.0, 105.0))
       self.UMLmodel.coords(new_obj.connectors[1],(193.0, 123.0, 193.0, 123.0))
       self.UMLmodel.coords(new_obj.connectors[2],(201.99999999999997, 114.0, 201.99999999999997, 114.0))
       self.UMLmodel.coords(new_obj.connectors[3],(185.0, 114.0, 185.0, 114.0))
       self.UMLmodel.coords(new_obj.gf3.handler,184.0,105.0,202.0,123.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,195.0,132.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='A')
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
    self.obj40.name.setValue('B')
    self.obj40.exit_action.setValue('\n\n')
    self.obj40.enter_action.setValue('\n\n')
    self.obj40.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(245.0,201.0,self.obj40)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(266.0, 204.0, 266.0, 204.0))
       self.UMLmodel.coords(new_obj.connectors[1],(266.0, 222.0, 266.0, 222.0))
       self.UMLmodel.coords(new_obj.connectors[2],(275.0, 213.0, 275.0, 213.0))
       self.UMLmodel.coords(new_obj.connectors[3],(258.0, 213.0, 258.0, 213.0))
       self.UMLmodel.coords(new_obj.gf3.handler,257.0,204.0,275.0,222.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,268.0,231.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='B')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj40.graphObject_ = new_obj
    rootNode.addNode(self.obj40)
    self.globalAndLocalPostcondition(self.obj40, rootNode)

    self.globalPrecondition( rootNode )

    self.obj41=Hyperedge(self)

    self.obj41.name.setValue('')
    self.obj41.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj41.guard.setValue('1')
    self.obj41.trigger.setValue('e1')
    self.obj41.action.setValue('[DUMP("doing A->B transition")]\n')
    self.obj41.broadcast_to.setValue('')
    self.obj41.display.setValue('e1')
    self.obj41.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(339.5,122.5,self.obj41)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj41.graphObject_ = new_obj
    rootNode.addNode(self.obj41)
    self.globalAndLocalPostcondition(self.obj41, rootNode)

    self.globalPrecondition( rootNode )

    self.obj42=Hyperedge(self)

    self.obj42.name.setValue('')
    self.obj42.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n\n')
    self.obj42.guard.setValue('1')
    self.obj42.trigger.setValue('e2')
    self.obj42.action.setValue('\n\n')
    self.obj42.broadcast_to.setValue('')
    self.obj42.display.setValue('e2')
    self.obj42.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(234.5,158.5,self.obj42)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj42.graphObject_ = new_obj
    rootNode.addNode(self.obj42)
    self.globalAndLocalPostcondition(self.obj42, rootNode)
    self.drawConnections((self.obj39,self.obj41,[201.99999999999997, 114.0, 289.0, 46.0, 339.5, 122.50000000000001],"bezier", 3), (self.obj40,self.obj42,[266.0, 204.0, 234.5, 158.5], 0, 2), (self.obj41,self.obj40,[339.5, 122.50000000000001, 362.0, 184.0, 275.0, 213.0],"bezier", 3), (self.obj42,self.obj39,[234.5, 158.5, 201.99999999999997, 114.0], 0, 2) )

newfunction = m0_DCharts_mdl

loadedMMName = 'DCharts'
