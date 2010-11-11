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

def Client(self, rootNode):

    self.globalPrecondition( rootNode )

    self.obj32=Basic(self)

    self.obj32.is_default.setValue((None, 0))
    self.obj32.is_default.config = 0
    self.obj32.name.setValue('NOCHAT')
    self.obj32.exit_action.setValue('\n\n\n')
    self.obj32.enter_action.setValue('\n')
    self.obj32.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(106.0,170.0,self.obj32)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,118.0,173.0,136.0,191.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,129.0,200.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='NOCHAT')
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
    self.obj33.name.setValue('CONNECTED')
    self.obj33.exit_action.setValue('\n\n')
    self.obj33.enter_action.setValue('\n\n')
    self.obj33.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(261.0,168.0,self.obj33)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,273.0,171.0,291.0,189.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,284.0,198.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='CONNECTED')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj33.graphObject_ = new_obj
    rootNode.addNode(self.obj33)
    self.globalAndLocalPostcondition(self.obj33, rootNode)

    self.globalPrecondition( rootNode )

    self.obj46=Basic(self)

    self.obj46.is_default.setValue((None, 1))
    self.obj46.is_default.config = 0
    self.obj46.name.setValue('INIT')
    self.obj46.exit_action.setValue('\n')
    self.obj46.enter_action.setValue('import random\nSelfID=random.randint(0, 65535)\nRandomMessages=["Hello, everyone!", "Have a nice day!", "How are you today?", "I feel very well today!", "The same to you!"]\nRequestMin=1\nRequestMax=3\nSendMin=1\nSendMax=5\n')
    self.obj46.graphClass_= graph_Basic
    if self.genGraphics:
       from graph_Basic import *
       new_obj = graph_Basic(34.0,67.0,self.obj46)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,46.0,70.0,64.0,88.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,57.0,97.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='INIT')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
    else: new_obj = None
    self.obj46.graphObject_ = new_obj
    rootNode.addNode(self.obj46)
    self.globalAndLocalPostcondition(self.obj46, rootNode)

    self.globalPrecondition( rootNode )

    self.obj34=Port(self)

    self.obj34.is_out.setValue((None, 1))
    self.obj34.is_out.config = 0
    self.obj34.name.setValue('request')
    self.obj34.is_in.setValue((None, 1))
    self.obj34.is_in.config = 0
    self.obj34.graphClass_= graph_Port
    if self.genGraphics:
       from graph_Port import *
       new_obj = graph_Port(75.0,299.0,self.obj34)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Port", new_obj.tag)
    else: new_obj = None
    self.obj34.graphObject_ = new_obj
    rootNode.addNode(self.obj34)
    self.globalAndLocalPostcondition(self.obj34, rootNode)

    self.globalPrecondition( rootNode )

    self.obj35=Port(self)

    self.obj35.is_out.setValue((None, 1))
    self.obj35.is_out.config = 0
    self.obj35.name.setValue('message')
    self.obj35.is_in.setValue((None, 1))
    self.obj35.is_in.config = 0
    self.obj35.graphClass_= graph_Port
    if self.genGraphics:
       from graph_Port import *
       new_obj = graph_Port(75.0,370.0,self.obj35)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Port", new_obj.tag)
    else: new_obj = None
    self.obj35.graphObject_ = new_obj
    rootNode.addNode(self.obj35)
    self.globalAndLocalPostcondition(self.obj35, rootNode)

    self.globalPrecondition( rootNode )

    self.obj36=Server(self)

    self.obj36.id.setValue('ChatRoom')
    self.obj36.name_pattern.setValue('ChatRoom')
    self.obj36.graphClass_= graph_Server
    if self.genGraphics:
       from graph_Server import *
       new_obj = graph_Server(151.0,329.0,self.obj36)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Server", new_obj.tag)
    else: new_obj = None
    self.obj36.graphObject_ = new_obj
    rootNode.addNode(self.obj36)
    self.globalAndLocalPostcondition(self.obj36, rootNode)

    self.globalPrecondition( rootNode )

    self.obj37=Hyperedge(self)

    self.obj37.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj37.guard.setValue('1')
    self.obj37.trigger.setValue('AFTER(random.uniform(RequestMin, RequestMax))')
    self.obj37.name.setValue('')
    self.obj37.action.setValue('room=random.randint(0, 1)\n[DUMP(time.ctime(time.time()))]\n[DUMP("(Client %d) A connection request is sent to chat room %d." % (SelfID, room))]\n[EVENT("request.Request", [room, SelfID])]\n')
    self.obj37.broadcast_to.setValue('')
    self.obj37.display.setValue('after(...)')
    self.obj37.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(128.0,172.0,self.obj37)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj37.graphObject_ = new_obj
    rootNode.addNode(self.obj37)
    self.globalAndLocalPostcondition(self.obj37, rootNode)

    self.globalPrecondition( rootNode )

    self.obj38=Hyperedge(self)

    self.obj38.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj38.guard.setValue('[PARAMS][0]==SelfID')
    self.obj38.trigger.setValue('request.Reject')
    self.obj38.name.setValue('')
    self.obj38.action.setValue('[DUMP(time.ctime(time.time()))]\n[DUMP("(Client %d) Rejected by chat room %d." % (SelfID, [PARAMS][1]))]\n')
    self.obj38.broadcast_to.setValue('')
    self.obj38.display.setValue('request.Reject')
    self.obj38.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(129.0,190.0,self.obj38)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj38.graphObject_ = new_obj
    rootNode.addNode(self.obj38)
    self.globalAndLocalPostcondition(self.obj38, rootNode)

    self.globalPrecondition( rootNode )

    self.obj39=Hyperedge(self)

    self.obj39.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj39.guard.setValue('[PARAMS][0]==SelfID')
    self.obj39.trigger.setValue('request.Accept')
    self.obj39.name.setValue('')
    self.obj39.action.setValue('RoomNo=[PARAMS][1]\n[DUMP(time.ctime(time.time()))]\n[DUMP("(Client %d) Accepted by chat room %d." % (SelfID, RoomNo))]\n')
    self.obj39.broadcast_to.setValue('')
    self.obj39.display.setValue('request.Accept')
    self.obj39.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(169.0,221.0,self.obj39)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj39.graphObject_ = new_obj
    rootNode.addNode(self.obj39)
    self.globalAndLocalPostcondition(self.obj39, rootNode)

    self.globalPrecondition( rootNode )

    self.obj40=Hyperedge(self)

    self.obj40.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj40.guard.setValue('1')
    self.obj40.trigger.setValue('AFTER(random.uniform(SendMin, SendMax))')
    self.obj40.name.setValue('')
    self.obj40.action.setValue('msg=RandomMessages[random.randint(0, len(RandomMessages)-1)]\n[DUMP(time.ctime(time.time()))]\n[DUMP("(Client %d) Says: " % SelfID + msg)]\n[EVENT("message.Send", [RoomNo, SelfID, msg, time.time()])]\n')
    self.obj40.broadcast_to.setValue('')
    self.obj40.display.setValue('after(...)')
    self.obj40.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(286.0,165.0,self.obj40)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj40.graphObject_ = new_obj
    rootNode.addNode(self.obj40)
    self.globalAndLocalPostcondition(self.obj40, rootNode)

    self.globalPrecondition( rootNode )

    self.obj41=Hyperedge(self)

    self.obj41.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj41.guard.setValue('[PARAMS][0]==SelfID')
    self.obj41.trigger.setValue('message.Broadcast')
    self.obj41.name.setValue('')
    self.obj41.action.setValue('sender=[PARAMS][1]\nmsg=[PARAMS][2]\n[DUMP(time.ctime(time.time()))]\n[DUMP("(Client %d) Received message \\"" % SelfID + msg + "\\" from client %d." % sender)]\n')
    self.obj41.broadcast_to.setValue('')
    self.obj41.display.setValue('message.Broadcast')
    self.obj41.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(304.0,184.0,self.obj41)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj41.graphObject_ = new_obj
    rootNode.addNode(self.obj41)
    self.globalAndLocalPostcondition(self.obj41, rootNode)

    self.globalPrecondition( rootNode )

    self.obj47=Hyperedge(self)

    self.obj47.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj47.guard.setValue('1')
    self.obj47.trigger.setValue('')
    self.obj47.name.setValue('')
    self.obj47.action.setValue('')
    self.obj47.broadcast_to.setValue('')
    self.obj47.display.setValue('')
    self.obj47.graphClass_= graph_Hyperedge
    if self.genGraphics:
       from graph_Hyperedge import *
       new_obj = graph_Hyperedge(56.5,86.0,self.obj47)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
    else: new_obj = None
    self.obj47.graphObject_ = new_obj
    rootNode.addNode(self.obj47)
    self.globalAndLocalPostcondition(self.obj47, rootNode)

    self.globalPrecondition( rootNode )

    self.obj42=connection(self)

    self.obj42.server_port.setValue('request')
    self.obj42.graphClass_= graph_connection
    if self.genGraphics:
       from graph_connection import *
       new_obj = graph_connection(141.0,318.5,self.obj42)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("connection", new_obj.tag)
    else: new_obj = None
    self.obj42.graphObject_ = new_obj
    rootNode.addNode(self.obj42)
    self.globalAndLocalPostcondition(self.obj42, rootNode)

    self.globalPrecondition( rootNode )

    self.obj43=connection(self)

    self.obj43.server_port.setValue('message')
    self.obj43.graphClass_= graph_connection
    if self.genGraphics:
       from graph_connection import *
       new_obj = graph_connection(137.0,388.5,self.obj43)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("connection", new_obj.tag)
    else: new_obj = None
    self.obj43.graphObject_ = new_obj
    rootNode.addNode(self.obj43)
    self.globalAndLocalPostcondition(self.obj43, rootNode)
    self.drawConnections((self.obj32,self.obj37,[127.0, 173.0, 128.0, 172.0], 0, 2), (self.obj32,self.obj38,[127.0, 191.0, 129.0, 190.0],"bezier", 2), (self.obj32,self.obj39,[136.0, 182.0, 169.0, 221.0], 0, 2), (self.obj33,self.obj40,[274.0, 180.0, 185.0, 166.0, 319.0, 92.0, 286.0, 165.0],"bezier", 4), (self.obj33,self.obj41,[282.0, 189.0, 244.0, 278.0, 381.0, 196.0, 304.0, 184.0],"bezier", 4), (self.obj46,self.obj47,[55.0, 88.0, 56.5, 86.0], 0, 2), (self.obj34,self.obj42,[91.0, 319.0, 141.0, 318.5], 0, 2), (self.obj35,self.obj43,[91.0, 390.0, 137.0, 388.5], 0, 2), (self.obj37,self.obj32,[128.0, 172.0, 115.0, 128.0, 135.0, 113.0, 224.0, 181.0, 136.0, 182.0],"bezier", 5), (self.obj38,self.obj32,[129.0, 190.0, 154.0, 276.0, 30.0, 184.0, 119.0, 182.0],"bezier", 4), (self.obj39,self.obj33,[169.0, 221.0, 228.0, 280.0, 274.0, 180.0],"bezier", 3), (self.obj40,self.obj33,[286.0, 165.0, 282.0, 171.0], 0, 2), (self.obj41,self.obj33,[304.0, 184.0, 291.0, 180.0], 0, 2), (self.obj47,self.obj32,[56.5, 86.0, 71.0, 143.0, 119.0, 182.0],"bezier", 3), (self.obj42,self.obj36,[141.0, 318.5, 160.0, 344.0], 0, 2), (self.obj43,self.obj36,[137.0, 388.5, 160.0, 373.0], 0, 2) )

newfunction = Client

loadedMMName = 'DCharts'
