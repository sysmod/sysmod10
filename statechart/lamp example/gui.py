from Tkinter import *

class GUI:
    def __init__(self, master, eventhandler):
        frame = Frame(master);
        frame.pack()

        self.eventhandler = eventhandler
        
        self.buttonOn = Button(frame, text="On", command=self.handleEventOn)
        self.buttonOn.pack()

        self.buttonOff = Button(frame, text="Off", command=self.handleEventOff)
        self.buttonOff.pack()

        self.label = Label(frame);
        self.label.pack();
        self.imageOn = PhotoImage(file="on.gif")
        self.imageOff = PhotoImage(file="off.gif")
        self.setLightBulbOff()

    def handleEventOn(self):
        self.eventhandler.event("on")

    def handleEventOff(self):
        self.eventhandler.event("off")

    def setLightBulbOn(self):
        self.label.config(image = self.imageOn)

    def setLightBulbOff(self):
        self.label.config(image = self.imageOff)

#root = Tk()
#root.title("Flasing machine!!!")
#g = GUI(root, eventhandler)
#eventhandler.start()
#root.mainloop()
        
