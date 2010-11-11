from Tkinter import *
from DigitalWatchGUI import DigitalWatchGUI

if __name__=="__main__":
  root = Tk()
  root.withdraw()
  topLevel = Toplevel(root)
  topLevel.resizable(width="NO", height="NO")
  topLevel.title("DWatch")
  DigitalWatchGUI(topLevel)
  root.mainloop()