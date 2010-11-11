from Tkinter import Tk
from TrafficLightGUI import TrafficLightGUI
from TrafficLightBehaviour import TrafficLightBehaviour
from code import InteractiveInterpreter

if __name__=="__main__":
  # Create an interpreter with the current scope and dictionary
  # All the action code and guards are executed with this interpreter
  interpreter=InteractiveInterpreter(locals())
  behaviour=TrafficLightBehaviour(interpreter)

  root=Tk()
  # Initialize the GUI with the behaviour model as a parameter 
  # (see GUI.py)
  gui=TrafficLightGUI(behaviour, root)

  # Be sure to initialize the behaviour model after gui is created
  behaviour.initModel()

  # The Tkinter main event loop
  root.mainloop()

