from Tkinter import Tk
from gui import simpleGUI
from behavior import behavior
from code import InteractiveInterpreter

if __name__=="__main__":
  # Create an interpreter with the current scope and dictionary
  # All the action code and guards are executed with this interpreter
  interpreter=InteractiveInterpreter(locals())
  model=behavior(interpreter)

  root=Tk()
  # Initialize the gui with the model as a parameter (see gui.py)
  gui=simpleGUI(model, root)

  # Be sure to initialize the model AFTER gui is created
  model.initModel()

  root.mainloop()

