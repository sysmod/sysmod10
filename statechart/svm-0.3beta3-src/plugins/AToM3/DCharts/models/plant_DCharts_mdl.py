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

def plant_DCharts_mdl(self, rootNode):

    self.globalPrecondition( rootNode )

    self.obj28=Composite(self)

    self.obj28.auto_adjust.setValue((None, 1))
    self.obj28.auto_adjust.config = 0
    self.obj28.name.setValue('running')
    self.obj28.is_default.setValue((None, 1))
    self.obj28.is_default.config = 0
    self.obj28.visible.setValue((None, 1))
    self.obj28.visible.config = 0
    self.obj28.exit_action.setValue('\n')
    self.obj28.enter_action.setValue('\n')
    self.obj28.graphClass_= graph_Composite
    if self.genGraphics:
       from graph_Composite import *
       new_obj = graph_Composite(75.0,67.0,self.obj28)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Composite", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(121.00000000000001, 206.0, 121.00000000000001, 206.0))
       self.UMLmodel.coords(new_obj.connectors[1],(613.0, 206.0, 613.0, 206.0))
       self.UMLmodel.coords(new_obj.connectors[2],(367.0, 103.99999999999999, 367.0, 103.99999999999999))
       self.UMLmodel.coords(new_obj.connectors[3],(367.0, 309.0, 367.0, 309.0))
       self.UMLmodel.coords(new_obj.gf2.handler,121.0,104.0,613.0,309.0)
       self.UMLmodel.itemconfig(new_obj.gf2.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,121.0,97.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='running')
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
    self.obj29.name.setValue('heating')
    self.obj29.exit_action.setValue('\n\n')
    self.obj29.enter_action.setValue('\n\n')
    self.obj29.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(180.0,126.0,self.obj29)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(201.0, 129.0, 201.0, 129.0))
       self.UMLmodel.coords(new_obj.connectors[1],(201.0, 147.0, 201.0, 147.0))
       self.UMLmodel.coords(new_obj.connectors[2],(210.0, 138.0, 210.0, 138.0))
       self.UMLmodel.coords(new_obj.connectors[3],(193.0, 138.0, 193.0, 138.0))
       self.UMLmodel.coords(new_obj.gf3.handler,192.0,129.0,210.0,147.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,203.0,156.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='heating')
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

    self.obj30.is_default.setValue((None, 1))
    self.obj30.is_default.config = 0
    self.obj30.name.setValue('on')
    self.obj30.exit_action.setValue('\n\n')
    self.obj30.enter_action.setValue('\n\n')
    self.obj30.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(433.0,132.0,self.obj30)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(453.99999999999994, 135.0, 453.99999999999994, 135.0))
       self.UMLmodel.coords(new_obj.connectors[1],(453.99999999999994, 153.0, 453.99999999999994, 153.0))
       self.UMLmodel.coords(new_obj.connectors[2],(463.0, 144.0, 463.0, 144.0))
       self.UMLmodel.coords(new_obj.connectors[3],(446.0, 144.0, 446.0, 144.0))
       self.UMLmodel.coords(new_obj.gf3.handler,445.0,135.0,463.0,153.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,456.0,162.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='on')
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
    self.obj31.name.setValue('cooling')
    self.obj31.exit_action.setValue('\n\n')
    self.obj31.enter_action.setValue('\n\n')
    self.obj31.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(192.0,249.0,self.obj31)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(213.0, 251.99999999999997, 213.0, 251.99999999999997))
       self.UMLmodel.coords(new_obj.connectors[1],(213.0, 270.0, 213.0, 270.0))
       self.UMLmodel.coords(new_obj.connectors[2],(222.0, 261.0, 222.0, 261.0))
       self.UMLmodel.coords(new_obj.connectors[3],(204.99999999999997, 261.0, 204.99999999999997, 261.0))
       self.UMLmodel.coords(new_obj.gf3.handler,204.0,252.0,222.0,270.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,215.0,279.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='cooling')
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

    self.obj32.is_default.setValue((None, 0))
    self.obj32.is_default.config = 0
    self.obj32.name.setValue('off')
    self.obj32.exit_action.setValue('\n\n')
    self.obj32.enter_action.setValue('\n\n')
    self.obj32.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(453.0,260.0,self.obj32)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(474.0, 263.0, 474.0, 263.0))
       self.UMLmodel.coords(new_obj.connectors[1],(474.0, 281.0, 474.0, 281.0))
       self.UMLmodel.coords(new_obj.connectors[2],(483.0, 272.0, 483.0, 272.0))
       self.UMLmodel.coords(new_obj.connectors[3],(465.99999999999994, 272.0, 465.99999999999994, 272.0))
       self.UMLmodel.coords(new_obj.gf3.handler,465.0,263.0,483.0,281.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,476.0,290.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='off')
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
    self.obj33.name.setValue('terminated')
    self.obj33.exit_action.setValue('\n\n')
    self.obj33.enter_action.setValue('\n\n')
    self.obj33.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(346.0,384.0,self.obj33)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(367.0, 387.0, 367.0, 387.0))
       self.UMLmodel.coords(new_obj.connectors[1],(367.0, 405.0, 367.0, 405.0))
       self.UMLmodel.coords(new_obj.connectors[2],(376.0, 396.0, 376.0, 396.0))
       self.UMLmodel.coords(new_obj.connectors[3],(359.0, 396.0, 359.0, 396.0))
       self.UMLmodel.coords(new_obj.gf3.handler,358.0,387.0,376.0,405.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,369.0,414.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='terminated')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj33.graphObject_ = new_obj
    rootNode.addNode(self.obj33)
    self.globalAndLocalPostcondition(self.obj33, rootNode)

    self.globalPrecondition( rootNode )

    self.obj34=Orthogonal(self)

    self.obj34.visible.setValue((None, 1))
    self.obj34.visible.config = 0
    self.obj34.name.setValue('plant')
    self.obj34.auto_adjust.setValue((None, 1))
    self.obj34.auto_adjust.config = 0
    self.obj34.graphClass_= graph_Orthogonal
    if self.genGraphics:
       from graph_Orthogonal import *
       new_obj = graph_Orthogonal(86.0,107.0,self.obj34)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Orthogonal", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(140.0, 207.0, 140.0, 207.0))
       self.UMLmodel.coords(new_obj.connectors[1],(322.0, 207.0, 322.0, 207.0))
       self.UMLmodel.coords(new_obj.connectors[2],(231.0, 123.0, 231.0, 123.0))
       self.UMLmodel.coords(new_obj.connectors[3],(231.0, 291.0, 231.0, 291.0))
       self.UMLmodel.coords(new_obj.gf5.handler,140.0,123.0,322.0,291.0)
       self.UMLmodel.itemconfig(new_obj.gf5.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, outline='darkgray')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,140.0,116.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='plant')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj34.graphObject_ = new_obj
    rootNode.addNode(self.obj34)
    self.globalAndLocalPostcondition(self.obj34, rootNode)

    self.globalPrecondition( rootNode )

    self.obj35=Orthogonal(self)

    self.obj35.visible.setValue((None, 1))
    self.obj35.visible.config = 0
    self.obj35.name.setValue('control')
    self.obj35.auto_adjust.setValue((None, 1))
    self.obj35.auto_adjust.config = 0
    self.obj35.graphClass_= graph_Orthogonal
    if self.genGraphics:
       from graph_Orthogonal import *
       new_obj = graph_Orthogonal(389.0,124.0,self.obj35)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Orthogonal", new_obj.tag)
       self.UMLmodel.coords(new_obj.connectors[0],(376.0, 215.0, 376.0, 215.0))
       self.UMLmodel.coords(new_obj.connectors[1],(606.0, 215.0, 606.0, 215.0))
       self.UMLmodel.coords(new_obj.connectors[2],(490.99999999999994, 129.0, 490.99999999999994, 129.0))
       self.UMLmodel.coords(new_obj.connectors[3],(490.99999999999994, 302.0, 490.99999999999994, 302.0))
       self.UMLmodel.coords(new_obj.gf5.handler,376.0,129.0,606.0,302.0)
       self.UMLmodel.itemconfig(new_obj.gf5.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, outline='darkgray')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,376.0,122.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='control')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj35.graphObject_ = new_obj
    rootNode.addNode(self.obj35)
    self.globalAndLocalPostcondition(self.obj35, rootNode)

    self.globalPrecondition( rootNode )

    self.obj36=contains(self)

    self.obj36.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(160.5,144.0,self.obj36)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj36.graphObject_ = new_obj
    rootNode.addNode(self.obj36)
    self.globalAndLocalPostcondition(self.obj36, rootNode)

    self.globalPrecondition( rootNode )

    self.obj37=contains(self)

    self.obj37.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(166.5,205.5,self.obj37)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj37.graphObject_ = new_obj
    rootNode.addNode(self.obj37)
    self.globalAndLocalPostcondition(self.obj37, rootNode)

    self.globalPrecondition( rootNode )

    self.obj38=contains(self)

    self.obj38.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(438.5,155.5,self.obj38)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj38.graphObject_ = new_obj
    rootNode.addNode(self.obj38)
    self.globalAndLocalPostcondition(self.obj38, rootNode)

    self.globalPrecondition( rootNode )

    self.obj39=contains(self)

    self.obj39.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(448.5,219.5,self.obj39)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj39.graphObject_ = new_obj
    rootNode.addNode(self.obj39)
    self.globalAndLocalPostcondition(self.obj39, rootNode)

    self.globalPrecondition( rootNode )

    self.obj40=Hyperedge(self)

    self.obj40.name.setValue('')
    self.obj40.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj40.guard.setValue('1')
    self.obj40.trigger.setValue('start_cooling')
    self.obj40.action.setValue('\n')
    self.obj40.broadcast_to.setValue('')
    self.obj40.display.setValue('start_cooling')
    self.obj40.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(153.0,196.5,self.obj40)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj40.graphObject_ = new_obj
    rootNode.addNode(self.obj40)
    self.globalAndLocalPostcondition(self.obj40, rootNode)

    self.globalPrecondition( rootNode )

    self.obj41=Hyperedge(self)

    self.obj41.name.setValue('')
    self.obj41.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n\n')
    self.obj41.guard.setValue('1')
    self.obj41.trigger.setValue('AFTER(1)')
    self.obj41.action.setValue('start_cooling\n')
    self.obj41.broadcast_to.setValue('')
    self.obj41.display.setValue('tm(1)/start_cooling')
    self.obj41.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(384.0,208.0,self.obj41)
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
    self.obj42.trigger.setValue('start_heating')
    self.obj42.action.setValue('\n\n')
    self.obj42.broadcast_to.setValue('')
    self.obj42.display.setValue('start_heating')
    self.obj42.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(252.0,201.5,self.obj42)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj42.graphObject_ = new_obj
    rootNode.addNode(self.obj42)
    self.globalAndLocalPostcondition(self.obj42, rootNode)

    self.globalPrecondition( rootNode )

    self.obj43=Hyperedge(self)

    self.obj43.name.setValue('')
    self.obj43.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n\n')
    self.obj43.guard.setValue('1')
    self.obj43.trigger.setValue('AFTER(3)')
    self.obj43.action.setValue('start_heating\n')
    self.obj43.broadcast_to.setValue('')
    self.obj43.display.setValue('tm(3)/start_heating')
    self.obj43.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(558.0,207.0,self.obj43)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj43.graphObject_ = new_obj
    rootNode.addNode(self.obj43)
    self.globalAndLocalPostcondition(self.obj43, rootNode)

    self.globalPrecondition( rootNode )

    self.obj44=Hyperedge(self)

    self.obj44.name.setValue('')
    self.obj44.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n')
    self.obj44.guard.setValue('1')
    self.obj44.trigger.setValue('quit_app')
    self.obj44.action.setValue('\n')
    self.obj44.broadcast_to.setValue('')
    self.obj44.display.setValue('quit_app')
    self.obj44.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(368.0,345.5,self.obj44)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj44.graphObject_ = new_obj
    rootNode.addNode(self.obj44)
    self.globalAndLocalPostcondition(self.obj44, rootNode)

    self.globalPrecondition( rootNode )

    self.obj45=orthogonality(self)

    self.obj45.graphClass_= graph_orthogonality
    if self.genGraphics:
       from graph_orthogonality import *
       new_obj = graph_orthogonality(130.5,113.5,self.obj45)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("orthogonality", new_obj.tag)
    else: new_obj = None
    self.obj45.graphObject_ = new_obj
    rootNode.addNode(self.obj45)
    self.globalAndLocalPostcondition(self.obj45, rootNode)

    self.globalPrecondition( rootNode )

    self.obj46=orthogonality(self)

    self.obj46.graphClass_= graph_orthogonality
    if self.genGraphics:
       from graph_orthogonality import *
       new_obj = graph_orthogonality(248.5,116.5,self.obj46)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("orthogonality", new_obj.tag)
    else: new_obj = None
    self.obj46.graphObject_ = new_obj
    rootNode.addNode(self.obj46)
    self.globalAndLocalPostcondition(self.obj46, rootNode)
    self.drawConnections((self.obj28,self.obj45,[121.00000000000001, 206.0, 130.5, 113.49999999999999], 0, 2), (self.obj28,self.obj46,[367.0, 103.99999999999999, 248.49999999999997, 116.49999999999999], 0, 2), (self.obj28,self.obj44,[367.0, 309.0, 368.0, 345.5], 0, 2), (self.obj29,self.obj40,[193.0, 138.0, 153.0, 196.5], 0, 2), (self.obj30,self.obj41,[446.0, 144.0, 384.00000000000006, 207.99999999999997], 0, 2), (self.obj31,self.obj42,[222.0, 261.0, 251.99999999999997, 201.50000000000003], 0, 2), (self.obj32,self.obj43,[483.0, 272.0, 558.0, 207.0], 0, 2), (self.obj34,self.obj36,[322.0, 207.0, 160.5, 144.0], 0, 2), (self.obj34,self.obj37,[231.0, 291.0, 166.5, 205.5], 0, 2), (self.obj35,self.obj38,[606.0, 215.0, 438.5, 155.5], 0, 2), (self.obj35,self.obj39,[490.99999999999994, 302.0, 448.5, 219.5], 0, 2), (self.obj36,self.obj29,[160.5, 144.0, 193.0, 138.0], 0, 2), (self.obj37,self.obj31,[166.5, 205.5, 213.0, 251.99999999999997], 0, 2), (self.obj38,self.obj30,[438.5, 155.5, 453.99999999999994, 153.0], 0, 2), (self.obj39,self.obj32,[448.5, 219.5, 474.0, 263.0], 0, 2), (self.obj40,self.obj31,[153.0, 196.5, 204.99999999999997, 261.0], 0, 2), (self.obj41,self.obj32,[384.00000000000006, 207.99999999999997, 465.99999999999994, 272.0], 0, 2), (self.obj42,self.obj29,[251.99999999999997, 201.50000000000003, 210.0, 138.0], 0, 2), (self.obj43,self.obj30,[558.0, 207.0, 463.0, 144.0], 0, 2), (self.obj44,self.obj33,[368.0, 345.5, 367.0, 387.0], 0, 2), (self.obj45,self.obj34,[130.5, 113.49999999999999, 140.0, 207.0], 0, 2), (self.obj46,self.obj35,[248.49999999999997, 116.49999999999999, 376.0, 215.0], 0, 2) )

newfunction = plant_DCharts_mdl

loadedMMName = 'DCharts'
