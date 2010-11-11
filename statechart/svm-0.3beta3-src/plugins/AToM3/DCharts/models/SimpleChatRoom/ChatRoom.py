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

def ChatRoom(self, rootNode):

    self.globalPrecondition( rootNode )

    self.obj32=Composite(self)

    self.obj32.is_default.setValue((None, 0))
    self.obj32.is_default.config = 0
    self.obj32.visible.setValue((None, 1))
    self.obj32.visible.config = 0
    self.obj32.auto_adjust.setValue((None, 1))
    self.obj32.auto_adjust.config = 0
    self.obj32.name.setValue('ROOT')
    self.obj32.exit_action.setValue('\n')
    self.obj32.enter_action.setValue('\n')
    self.obj32.graphClass_= graph_Composite
    if self.genGraphics:
       from graph_Composite import *
       new_obj = graph_Composite(309.0,120.0,self.obj32)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Composite", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf2.handler,69.0,30.0,557.0,262.0)
       self.UMLmodel.itemconfig(new_obj.gf2.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, outline='darkblue')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,69.0,23.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='ROOT')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj32.graphObject_ = new_obj
    rootNode.addNode(self.obj32)
    self.globalAndLocalPostcondition(self.obj32, rootNode)

    self.globalPrecondition( rootNode )

    self.obj33=Composite(self)

    self.obj33.is_default.setValue((None, 0))
    self.obj33.is_default.config = 0
    self.obj33.visible.setValue((None, 1))
    self.obj33.visible.config = 0
    self.obj33.auto_adjust.setValue((None, 1))
    self.obj33.auto_adjust.config = 0
    self.obj33.name.setValue('BROADCAST')
    self.obj33.exit_action.setValue('\n\n')
    self.obj33.enter_action.setValue('\n\n')
    self.obj33.graphClass_= graph_Composite
    if self.genGraphics:
       from graph_Composite import *
       new_obj = graph_Composite(230.0,223.0,self.obj33)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Composite", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf2.handler,188.0,72.0,550.0,255.0)
       self.UMLmodel.itemconfig(new_obj.gf2.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, outline='darkblue')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,188.0,65.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='BROADCAST')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj33.graphObject_ = new_obj
    rootNode.addNode(self.obj33)
    self.globalAndLocalPostcondition(self.obj33, rootNode)

    self.globalPrecondition( rootNode )

    self.obj34=Basic(self)

    self.obj34.is_default.setValue((None, 1))
    self.obj34.is_default.config = 0
    self.obj34.name.setValue('NORMAL')
    self.obj34.exit_action.setValue('\n\n')
    self.obj34.enter_action.setValue('\n\n')
    self.obj34.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(368.0,46.0,self.obj34)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,380.0,49.0,398.0,67.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,391.0,76.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='NORMAL')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj34.graphObject_ = new_obj
    rootNode.addNode(self.obj34)
    self.globalAndLocalPostcondition(self.obj34, rootNode)

    self.globalPrecondition( rootNode )

    self.obj35=Basic(self)

    self.obj35.is_default.setValue((None, 1))
    self.obj35.is_default.config = 0
    self.obj35.name.setValue('WAITING')
    self.obj35.exit_action.setValue('\n\n')
    self.obj35.enter_action.setValue('\n\n')
    self.obj35.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(278.0,127.0,self.obj35)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,290.0,130.0,308.0,148.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,301.0,157.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='WAITING')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj35.graphObject_ = new_obj
    rootNode.addNode(self.obj35)
    self.globalAndLocalPostcondition(self.obj35, rootNode)

    self.globalPrecondition( rootNode )

    self.obj36=Basic(self)

    self.obj36.is_default.setValue((None, 0))
    self.obj36.is_default.config = 0
    self.obj36.name.setValue('SENDING')
    self.obj36.exit_action.setValue('\n\n')
    self.obj36.enter_action.setValue('\n\n')
    self.obj36.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(346.0,186.0,self.obj36)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,358.0,189.0,376.0,207.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,369.0,216.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='SENDING')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj36.graphObject_ = new_obj
    rootNode.addNode(self.obj36)
    self.globalAndLocalPostcondition(self.obj36, rootNode)

    self.globalPrecondition( rootNode )

    self.obj57=Basic(self)

    self.obj57.is_default.setValue((None, 1))
    self.obj57.is_default.config = 0
    self.obj57.name.setValue('INIT')
    self.obj57.exit_action.setValue('\n')
    self.obj57.enter_action.setValue('import random\nSelfID=random.randint(0, 1)\nClients=[]\nPendingSend=[]\nMaxClients=3\n')
    self.obj57.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(8.0,43.0,self.obj57)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,20.0,46.0,38.0,64.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,31.0,73.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='INIT')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj57.graphObject_ = new_obj
    rootNode.addNode(self.obj57)
    self.globalAndLocalPostcondition(self.obj57, rootNode)

    self.globalPrecondition( rootNode )

    self.obj37=History(self)

    self.obj37.is_default.setValue((None, 0))
    self.obj37.is_default.config = 0
    self.obj37.star.setValue((None, 0))
    self.obj37.star.config = 0
    self.obj37.name.setValue('')
    self.obj37.graphClass_= graph_History
    if self.genGraphics:
       from graph_History import *
       new_obj = graph_History(190.0,123.0,self.obj37)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("History", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf0.handler,194.0,126.0,230.0,161.0)
       self.UMLmodel.itemconfig(new_obj.gf0.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf0.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf0.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf0.handler, fill='lightblue')
       self.UMLmodel.coords(new_obj.gf1.handler,211.0,145.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='H')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       self.UMLmodel.coords(new_obj.gf2.handler,219.0,145.0)
       self.UMLmodel.itemconfig(new_obj.gf2.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, fill='')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, text='*')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, justify='left')
       self.UMLmodel.coords(new_obj.gf3.handler,213.0,170.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='blue')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, text='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, justify='left')
    else: new_obj = None
    self.obj37.graphObject_ = new_obj
    rootNode.addNode(self.obj37)
    self.globalAndLocalPostcondition(self.obj37, rootNode)

    self.globalPrecondition( rootNode )

    self.obj38=History(self)

    self.obj38.is_default.setValue((None, 0))
    self.obj38.is_default.config = 0
    self.obj38.star.setValue((None, 1))
    self.obj38.star.config = 0
    self.obj38.name.setValue(' ')
    self.obj38.graphClass_= graph_History
    if self.genGraphics:
       from graph_History import *
       new_obj = graph_History(79.0,58.0,self.obj38)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("History", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf0.handler,83.0,61.0,119.0,96.0)
       self.UMLmodel.itemconfig(new_obj.gf0.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf0.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf0.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf0.handler, fill='lightblue')
       self.UMLmodel.coords(new_obj.gf1.handler,100.0,80.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='H')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       self.UMLmodel.coords(new_obj.gf2.handler,108.0,80.0)
       self.UMLmodel.itemconfig(new_obj.gf2.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, text='*')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, justify='left')
       self.UMLmodel.coords(new_obj.gf3.handler,102.0,105.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='blue')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, text=' ')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, justify='left')
    else: new_obj = None
    self.obj38.graphObject_ = new_obj
    rootNode.addNode(self.obj38)
    self.globalAndLocalPostcondition(self.obj38, rootNode)

    self.globalPrecondition( rootNode )

    self.obj39=Port(self)

    self.obj39.is_out.setValue((None, 1))
    self.obj39.is_out.config = 0
    self.obj39.name.setValue('message')
    self.obj39.is_in.setValue((None, 1))
    self.obj39.is_in.config = 0
    self.obj39.graphClass_= graph_Port
    if self.genGraphics:
       from graph_Port import *
       new_obj = graph_Port(557.0,168.0,self.obj39)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Port", new_obj.tag)
    else: new_obj = None
    self.obj39.graphObject_ = new_obj
    rootNode.addNode(self.obj39)
    self.globalAndLocalPostcondition(self.obj39, rootNode)

    self.globalPrecondition( rootNode )

    self.obj40=Port(self)

    self.obj40.is_out.setValue((None, 1))
    self.obj40.is_out.config = 0
    self.obj40.name.setValue('request')
    self.obj40.is_in.setValue((None, 1))
    self.obj40.is_in.config = 0
    self.obj40.graphClass_= graph_Port
    if self.genGraphics:
       from graph_Port import *
       new_obj = graph_Port(557.0,73.0,self.obj40)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Port", new_obj.tag)
    else: new_obj = None
    self.obj40.graphObject_ = new_obj
    rootNode.addNode(self.obj40)
    self.globalAndLocalPostcondition(self.obj40, rootNode)

    self.globalPrecondition( rootNode )

    self.obj41=contains(self)

    self.obj41.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(498.5,138.5,self.obj41)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj41.graphObject_ = new_obj
    rootNode.addNode(self.obj41)
    self.globalAndLocalPostcondition(self.obj41, rootNode)

    self.globalPrecondition( rootNode )

    self.obj42=contains(self)

    self.obj42.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(275.5,195.0,self.obj42)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj42.graphObject_ = new_obj
    rootNode.addNode(self.obj42)
    self.globalAndLocalPostcondition(self.obj42, rootNode)

    self.globalPrecondition( rootNode )

    self.obj43=contains(self)

    self.obj43.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(284.5,153.0,self.obj43)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj43.graphObject_ = new_obj
    rootNode.addNode(self.obj43)
    self.globalAndLocalPostcondition(self.obj43, rootNode)

    self.globalPrecondition( rootNode )

    self.obj44=contains(self)

    self.obj44.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(333.5,165.0,self.obj44)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj44.graphObject_ = new_obj
    rootNode.addNode(self.obj44)
    self.globalAndLocalPostcondition(self.obj44, rootNode)

    self.globalPrecondition( rootNode )

    self.obj45=contains(self)

    self.obj45.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(420.5,189.0,self.obj45)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj45.graphObject_ = new_obj
    rootNode.addNode(self.obj45)
    self.globalAndLocalPostcondition(self.obj45, rootNode)

    self.globalPrecondition( rootNode )

    self.obj46=contains(self)

    self.obj46.graphClass_= graph_contains
    if self.genGraphics:
       from graph_contains import *
       new_obj = graph_contains(191.5,119.0,self.obj46)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
    else: new_obj = None
    self.obj46.graphObject_ = new_obj
    rootNode.addNode(self.obj46)
    self.globalAndLocalPostcondition(self.obj46, rootNode)

    self.globalPrecondition( rootNode )

    self.obj47=Hyperedge(self)

    self.obj47.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj47.guard.setValue('[PARAMS][0]==SelfID and len(Clients)<MaxClients')
    self.obj47.trigger.setValue('request.Request')
    self.obj47.name.setValue('')
    self.obj47.action.setValue('ClientID=[PARAMS][1]\nClients.append(ClientID)\n[DUMP(time.ctime(time.time()))]\n[DUMP("(Chat Room %d) Received connection request from client %d." % (SelfID, ClientID))]\n[DUMP(time.ctime(time.time()))]\n[DUMP("(Chat Room %d) Accepted client %d." % (SelfID, ClientID))]\n[EVENT("request.Accept", [ClientID, SelfID])]\n')
    self.obj47.broadcast_to.setValue('')
    self.obj47.display.setValue('request.Request (accept)')
    self.obj47.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(115.5,35.0,self.obj47)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj47.graphObject_ = new_obj
    rootNode.addNode(self.obj47)
    self.globalAndLocalPostcondition(self.obj47, rootNode)

    self.globalPrecondition( rootNode )

    self.obj48=Hyperedge(self)

    self.obj48.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj48.guard.setValue('[PARAMS][0]==SelfID and len(Clients)>=MaxClients')
    self.obj48.trigger.setValue('request.Request')
    self.obj48.name.setValue('')
    self.obj48.action.setValue('ClientID=[PARAMS][1]\n[DUMP(time.ctime(time.time()))]\n[DUMP("(Chat Room %d) Received connection request from client %d." % (SelfID, ClientID))]\n[DUMP(time.ctime(time.time()))]\n[DUMP("(Chat Room %d) Rejected client %d." % (SelfID, ClientID))]\n[EVENT("request.Reject", [ClientID])]\n')
    self.obj48.broadcast_to.setValue('')
    self.obj48.display.setValue('request.Request (reject)')
    self.obj48.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(210.5,78.0,self.obj48)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj48.graphObject_ = new_obj
    rootNode.addNode(self.obj48)
    self.globalAndLocalPostcondition(self.obj48, rootNode)

    self.globalPrecondition( rootNode )

    self.obj49=Hyperedge(self)

    self.obj49.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj49.guard.setValue('[PARAMS][0]==SelfID')
    self.obj49.trigger.setValue('message.Send')
    self.obj49.name.setValue('')
    self.obj49.action.setValue('[sender, msg, sendtime]=[PARAMS][1:]\nPendingSend.append([sender, msg, sendtime])\n[DUMP(time.ctime(time.time()))]\n[DUMP("(Chat Room %d) Received message \\"" % SelfID + msg + "\\" from client %d." % sender)]\n')
    self.obj49.broadcast_to.setValue('')
    self.obj49.display.setValue('message.Send')
    self.obj49.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(321.0,92.0,self.obj49)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj49.graphObject_ = new_obj
    rootNode.addNode(self.obj49)
    self.globalAndLocalPostcondition(self.obj49, rootNode)

    self.globalPrecondition( rootNode )

    self.obj50=Hyperedge(self)

    self.obj50.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj50.guard.setValue('[PARAMS][0]==SelfID')
    self.obj50.trigger.setValue('message.Send')
    self.obj50.name.setValue('')
    self.obj50.action.setValue('[sender, msg, sendtime]=[PARAMS][1:]\nPendingSend.append([sender, msg, sendtime])\n[DUMP(time.ctime(time.time()))]\n[DUMP("(Chat Room %d) Received message \\"" % SelfID + msg + "\\" from client %d." % sender)]\n')
    self.obj50.broadcast_to.setValue('')
    self.obj50.display.setValue('message.Send')
    self.obj50.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(228.5,219.0,self.obj50)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj50.graphObject_ = new_obj
    rootNode.addNode(self.obj50)
    self.globalAndLocalPostcondition(self.obj50, rootNode)

    self.globalPrecondition( rootNode )

    self.obj51=Hyperedge(self)

    self.obj51.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n\n\n\n\n')
    self.obj51.guard.setValue('1')
    self.obj51.trigger.setValue('AFTER(PendingSend[0][2]+1-time.time())')
    self.obj51.name.setValue('')
    self.obj51.action.setValue('Receiver=0\n[EVENT("Send Loop", SelfID)]\n\n\n\n')
    self.obj51.broadcast_to.setValue('')
    self.obj51.display.setValue('after(...)')
    self.obj51.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(385.5,139.0,self.obj51)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj51.graphObject_ = new_obj
    rootNode.addNode(self.obj51)
    self.globalAndLocalPostcondition(self.obj51, rootNode)

    self.globalPrecondition( rootNode )

    self.obj52=Hyperedge(self)

    self.obj52.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj52.guard.setValue('[PARAMS]==SelfID and Receiver<len(Clients) and Clients[Receiver]!=PendingSend[0][0]')
    self.obj52.trigger.setValue('Send Loop')
    self.obj52.name.setValue('')
    self.obj52.action.setValue('[EVENT("message.Broadcast", [Clients[Receiver]]+PendingSend[0])]\nReceiver+=1\n[EVENT("Send Loop", SelfID)]\n')
    self.obj52.broadcast_to.setValue('')
    self.obj52.display.setValue('Send Loop 1')
    self.obj52.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(447.0,192.0,self.obj52)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj52.graphObject_ = new_obj
    rootNode.addNode(self.obj52)
    self.globalAndLocalPostcondition(self.obj52, rootNode)

    self.globalPrecondition( rootNode )

    self.obj53=Hyperedge(self)

    self.obj53.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj53.guard.setValue('[PARAMS]==SelfID and Receiver<len(Clients) and Clients[Receiver]==PendingSend[0][0]')
    self.obj53.trigger.setValue('Send Loop')
    self.obj53.name.setValue('')
    self.obj53.action.setValue('Receiver+=1\n[EVENT("Send Loop", SelfID)]\n')
    self.obj53.broadcast_to.setValue('')
    self.obj53.display.setValue('Send Loop 2')
    self.obj53.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(346.0,236.0,self.obj53)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj53.graphObject_ = new_obj
    rootNode.addNode(self.obj53)
    self.globalAndLocalPostcondition(self.obj53, rootNode)

    self.globalPrecondition( rootNode )

    self.obj54=Hyperedge(self)

    self.obj54.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj54.guard.setValue('[PARAMS]==SelfID and Receiver==len(Clients) and len(PendingSend)>1')
    self.obj54.trigger.setValue('Send Loop')
    self.obj54.name.setValue('')
    self.obj54.action.setValue('pending=PendingSend[0]\nsender=pending[0]\nmsg=pending[1]\n[DUMP(time.ctime(time.time()))]\n[DUMP("(Chat Room %d) Sent message \\"" % SelfID + msg + "\\" to all connected clients except client %d." % sender)]\nReceiver=0\ndel PendingSend[0]\n')
    self.obj54.broadcast_to.setValue('')
    self.obj54.display.setValue('Send Loop 3')
    self.obj54.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(280.0,198.0,self.obj54)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj54.graphObject_ = new_obj
    rootNode.addNode(self.obj54)
    self.globalAndLocalPostcondition(self.obj54, rootNode)

    self.globalPrecondition( rootNode )

    self.obj55=Hyperedge(self)

    self.obj55.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj55.guard.setValue('[PARAMS]==SelfID and Receiver==len(Clients) and len(PendingSend)==1')
    self.obj55.trigger.setValue('Send Loop')
    self.obj55.name.setValue('')
    self.obj55.action.setValue('pending=PendingSend[0]\nsender=pending[0]\nmsg=pending[1]\n[DUMP(time.ctime(time.time()))]\n[DUMP("(Chat Room %d) Sent message \\"" % SelfID + msg + "\\" to all connected clients except client %d." % sender)]\nReceiver=0\ndel PendingSend[0]\n')
    self.obj55.broadcast_to.setValue('')
    self.obj55.display.setValue('Send Loop 4')
    self.obj55.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(480.0,77.0,self.obj55)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj55.graphObject_ = new_obj
    rootNode.addNode(self.obj55)
    self.globalAndLocalPostcondition(self.obj55, rootNode)

    self.globalPrecondition( rootNode )

    self.obj58=Hyperedge(self)

    self.obj58.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj58.guard.setValue('1')
    self.obj58.trigger.setValue('')
    self.obj58.name.setValue('')
    self.obj58.action.setValue('')
    self.obj58.broadcast_to.setValue('')
    self.obj58.display.setValue('')
    self.obj58.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(61.0,146.0,self.obj58)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj58.graphObject_ = new_obj
    rootNode.addNode(self.obj58)
    self.globalAndLocalPostcondition(self.obj58, rootNode)
    self.drawConnections((self.obj32,self.obj41,[327.0, 61.0, 498.5, 138.5], 0, 2), (self.obj32,self.obj45,[265.0, 229.0, 420.5, 189.0], 0, 2), (self.obj32,self.obj46,[68.0, 129.0, 191.5, 119.0], 0, 2), (self.obj32,self.obj47,[265.0, 30.0, 115.5, 35.0], 0, 2), (self.obj32,self.obj48,[265.0, 30.0, 210.5, 78.0], 0, 2), (self.obj33,self.obj42,[322.0, 120.0, 275.5, 195.0], 0, 2), (self.obj33,self.obj43,[322.0, 222.0, 284.5, 153.0], 0, 2), (self.obj33,self.obj44,[456.0, 171.0, 333.5, 165.0], 0, 2), (self.obj33,self.obj50,[188.0, 163.0, 228.5, 219.0], 0, 2), (self.obj34,self.obj49,[381.0, 58.0, 321.0, 92.0], 0, 2), (self.obj35,self.obj51,[308.0, 139.0, 385.5, 139.0], 0, 2), (self.obj36,self.obj52,[367.0, 207.0, 447.0, 192.0], 0, 2), (self.obj36,self.obj53,[367.0, 207.0, 370.0, 232.0, 346.0, 236.0], 0, 3), (self.obj36,self.obj54,[359.0, 198.0, 280.0, 198.0], 0, 2), (self.obj36,self.obj55,[367.0, 189.0, 480.0, 77.0], 0, 2), (self.obj57,self.obj58,[29.0, 64.0, 21.0, 137.0, 61.0, 146.0],"bezier", 3), (self.obj41,self.obj34,[498.5, 138.5, 389.0, 67.0], 0, 2), (self.obj42,self.obj37,[275.5, 195.0, 212.0, 161.0], 0, 2), (self.obj43,self.obj35,[284.5, 153.0, 299.0, 148.0], 0, 2), (self.obj44,self.obj36,[333.5, 165.0, 359.0, 198.0], 0, 2), (self.obj45,self.obj33,[420.5, 189.0, 322.0, 120.0], 0, 2), (self.obj46,self.obj38,[191.5, 119.0, 118.0, 79.0], 0, 2), (self.obj47,self.obj38,[115.5, 35.0, 101.0, 61.0], 0, 2), (self.obj48,self.obj38,[210.5, 78.0, 118.0, 79.0], 0, 2), (self.obj49,self.obj33,[321.0, 92.0, 322.0, 120.0], 0, 2), (self.obj50,self.obj37,[228.5, 219.0, 212.0, 161.0], 0, 2), (self.obj51,self.obj36,[385.5, 139.0, 367.0, 189.0], 0, 2), (self.obj52,self.obj36,[447.0, 192.0, 406.0, 164.0, 376.0, 198.0], 0, 3), (self.obj53,self.obj36,[346.0, 236.0, 359.0, 198.0], 0, 2), (self.obj54,self.obj35,[280.0, 198.0, 299.0, 148.0], 0, 2), (self.obj55,self.obj34,[480.0, 77.0, 398.0, 58.0], 0, 2), (self.obj58,self.obj32,[61.0, 146.0, 69.0, 146.0], 0, 2) )

newfunction = ChatRoom

loadedMMName = 'DCharts'
