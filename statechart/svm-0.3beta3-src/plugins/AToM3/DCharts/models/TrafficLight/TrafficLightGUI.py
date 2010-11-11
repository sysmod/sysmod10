
from Tkinter import *  

class TrafficLightGUI(Frame):

  def __init__(self, behaviour, master=None, title="TrafficLight"):

    self.behaviour=behaviour

    # Initialize superclass
    Frame.__init__(self, master)

    # parent frame, destruction protocol
    self.root=master
    self.root.protocol("WM_DELETE_WINDOW", self.wmQuit)

    # Initialize packer
    self.pack(fill=BOTH, expand=1)

    # Create all widgets in the Frame
    self.__createWidgets()


  def __createWidgets(self):

    self.root.configure(bg="black")
#   self.root.pack(side=LEFT, fill=BOTH, expand=1)

    Label(self.root, text="", bg="black", 
          height=2, width=10).pack(side=TOP, padx = 2, pady=2)

    self.redLight=Label(self.root, text="", bg="red",
                        relief=GROOVE, height=5, width=10)
    self.redLight.pack(side=TOP, padx = 2, pady=4)

    self.yellowLight=Label(self.root, text="", bg="black",
                           relief=GROOVE, height=5, width=10)
    self.yellowLight.pack(side=TOP, padx = 2, pady=4)

    self.greenLight=Label(self.root, text="", bg="black",
                          relief=GROOVE, height=5, width=10)
    self.greenLight.pack(side=TOP, padx = 2, pady=4)

    Label(self.root, text="",bg="black",
          height=5, width=10).pack(side=TOP,padx=2,pady=2)

    self.pedCrossingButton=Button(self.root, text="Pedestrian Crossing",
      command=self.crossingPressed, width=10, wraplength=70)
    self.pedCrossingButton.pack(side=TOP, fill=Y, padx = 5, pady = 2)

    self.polintButton=Button(self.root, text="Police Interrupt",
      command=self.policePressed, width=10, wraplength=70)
    self.polintButton.pack(side=TOP, fill=Y, padx=5, pady=2)

    self.onOFFButton=Button(self.root, text="ON/OFF",
      command=self.onOFFPressed, width=10, wraplength=70)
    self.onOFFButton.pack(side=TOP, fill=Y, padx=5, pady=2)

    self.quitButton=Button(self.root, text="QUIT",
      command=self.quitPressed, width=10, wraplength=70)
    self.quitButton.pack(side=TOP, fill=Y, padx = 5, pady = 2)


  # binding with behaviour

  def crossingPressed(self):
    self.behaviour.event("CROSSWALK")

  def policePressed(self):
    self.behaviour.event("POLICE")

  def onOFFPressed(self):
    self.behaviour.event("ON-OFF")

  def quitPressed(self):
    self.behaviour.event("QUIT")
  
  def wmQuit(self):
    self.root.destroy()

  # the behaviour can call these methods to change the GUI

  def setGreen(self):
      self.redLight["bg"] = "black"
      self.yellowLight["bg"] = "black"
      self.greenLight["bg"] = "green"

  def setRed(self):
      self.redLight["bg"] = "red"
      self.yellowLight["bg"] = "black"
      self.greenLight["bg"] = "black"

  def setYellow(self):
      self.redLight["bg"] = "black"
      self.yellowLight["bg"] = "yellow"
      self.greenLight["bg"] = "black"

  def setDead(self):
      self.redLight["bg"] = "black"
      self.yellowLight["bg"] = "black"
      self.greenLight["bg"] = "black"



