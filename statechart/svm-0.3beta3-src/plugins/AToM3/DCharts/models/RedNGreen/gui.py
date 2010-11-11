from Tkinter import *   # basic Tkinter

class simpleGUI(Frame):

  def __init__(self, model, master=None, title="Simple GUI"):

    self.model=model

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

    self.label = Label(master=self.root,
                       takefocus=0,
                       width=20,
                       relief="groove")
    self.label.pack(side=RIGHT, fill=Y)
    
    self.button = Button(self.root, command=self.buttonPress, text="press")
    self.button.pack(side=LEFT)

  # events on Canvas: bind("<1>", self.callback)

  def buttonPress(self):
    self.model.event("press")

  # events on Canvas: also pass Event instance as parameter
  # def callback(self, event):
  #  self.model.event("press",event)

  def wmQuit(self):
    self.root.destroy()
