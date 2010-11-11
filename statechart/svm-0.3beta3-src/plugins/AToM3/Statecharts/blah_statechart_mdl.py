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
from ATOM3BottomType import *
from ATOM3String import *
from ATOM3Constraint import *
from ATOM3Attribute import *
from ATOM3Enum import *
from ATOM3Appearance import *
from ATOM3Float import *
from ATOM3Connection import *
from ATOM3Boolean import *
from ATOM3Link import *
from ATOM3Text import *
from ATOM3Integer import *
from ATOM3List import *
from ATOM3Port import *
from ATOM3MSEnum import *

def blah_statechart_mdl(self, rootNode):

    self.globalPrecondition( rootNode )

    self.obj25=Basic(self)

    self.obj25.is_default.setValue((None, 1))
    self.obj25.is_default.config = 0
    self.obj25.name.setValue('B')
    self.obj25.exit_action.setValue('\n\n')
    self.obj25.enter_action.setValue('\n\n')
    self.obj25.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(81.0,73.0,self.obj25)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(102.0, 76.0, 102.0, 76.0))
       self.UMLmodel.coords(new_obj.connectors[1],(102.0, 94.0, 102.0, 94.0))
       self.UMLmodel.coords(new_obj.connectors[2],(111.0, 85.0, 111.0, 85.0))
       self.UMLmodel.coords(new_obj.connectors[3],(94.0, 85.0, 94.0, 85.0))
       self.UMLmodel.coords(new_obj.gf3.handler,93.0,76.0,111.0,94.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,104.0,103.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='B')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj25.graphObject_ = new_obj
    rootNode.addNode(self.obj25)
    self.globalAndLocalPostcondition(self.obj25, rootNode)

    self.globalPrecondition( rootNode )

    self.obj26=Basic(self)

    self.obj26.is_default.setValue((None, 0))
    self.obj26.is_default.config = 0
    self.obj26.name.setValue('Basic')
    self.obj26.exit_action.setValue('\n')
    self.obj26.enter_action.setValue('\n')
    self.obj26.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(192.0,122.0,self.obj26)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(213.0, 125.0, 213.0, 125.0))
       self.UMLmodel.coords(new_obj.connectors[1],(213.0, 143.0, 213.0, 143.0))
       self.UMLmodel.coords(new_obj.connectors[2],(222.0, 134.0, 222.0, 134.0))
       self.UMLmodel.coords(new_obj.connectors[3],(205.0, 134.0, 205.0, 134.0))
       self.UMLmodel.coords(new_obj.gf3.handler,204.0,125.0,222.0,143.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,215.0,152.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Basic')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj26.graphObject_ = new_obj
    rootNode.addNode(self.obj26)
    self.globalAndLocalPostcondition(self.obj26, rootNode)

    self.globalPrecondition( rootNode )

    self.obj29=Hyperedge(self)

    self.obj29.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj29.guard.setValue('1')
    self.obj29.trigger.setValue('AFTER(1)')
    self.obj29.name.setValue('')
    self.obj29.action.setValue('\n')
    self.obj29.broadcast_to.setValue('')
    self.obj29.display.setValue('')
    self.obj29.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(191.5,64.5,self.obj29)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj29.graphObject_ = new_obj
    rootNode.addNode(self.obj29)
    self.globalAndLocalPostcondition(self.obj29, rootNode)
    self.drawConnections((self.obj25,self.obj29,[111.0, 85.0, 191.5, 64.5], 0, 2), (self.obj29,self.obj26,[191.5, 64.5, 222.0, 134.0], 0, 2) )

newfunction = blah_statechart_mdl

loadedMMName = 'Statechart'
