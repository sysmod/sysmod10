import sys
import os
import string

sys.path.insert(0, 'DCharts')

from ATOM3 import *
from Tkinter import Tk

from ATOM3String import *
from ATOM3Integer import *
import SVMAToM3Plugin

# faked classes
class MyStatusBar:
  def getState(self, a):
    return (1, ('Nonamed',))

class MyConsole:
  def appendText(self, text):
    pass

class MyButtonImage:
  def append(self, image):
    pass
  def __getitem__(self, index):
    return None

class MyUMLModel:
  def __init__(self):
    self.itemconfigure=self.itemconfig
  def create_rectangle(self, coord, tags, fill, outline, width, stipple):
    pass
  def type(self, t):
    return None
  def itemcget(self, a, b):
    return None
  def create_line(self, coord, joinstyle=None, smooth=None, capstyle=None, arrow=None, arrowshape=None, splinesteps=None, width=None, stipple=None, fill=None, tags=None):
    pass
  def create_text(self, coord, tags, text, fill, anchor, font, justify, width, stipple):
    pass
  def addtag_withtag(self, a, b):
    pass
  def create_oval(self, coord, tags, stipple, width, outline, fill):
    pass
  def coords(self, a=None, b=None, c=None, d=None, e=None, f=None, g=None, h=None, i=None, j=None, k=None):
    return [0, 0, 0, 0]
  def itemconfig(self, a, stipple=None, width=None, outline=None, fill=None, text=None, font=None, anchor=None, justify=None, smooth=None, tags=None):
    pass
  def bbox(self, a):
    pass
  def gettags(self, a):
    return []
  def create_polygon(self, coord, tags=None, stipple=None, width=None, splinesteps=None, outline=None, smooth=None, fill=None):
    pass

# modified methods of ATOM3
def ATOM3_init(self, parent):
  self.tk=self.parent=parent

  # some attributes (I really don't know what they mean)
  self.ASGroot=None
  self.genGraphics=1
  self.numImg=-1
  self.editGGLabel=0
  self.userActionsMap={}
  self.ConnectivityMap={}
  self.CardinalityTable={}
  self.entitiesInMetaModel={}
  self.modes={}
  self.toolBar=None
  self.buttonImage=MyButtonImage()
  self.buttonList=MyButtonImage()
  self.openMetaModels=ATOM3List([0,0,1,0], ATOM3String)
  self.UMLmodel=MyUMLModel()
  self.statusbar=MyStatusBar()

  # fake a console
  self.console=MyConsole()

  # initialize the DCharts meta-model
  old_path=os.path.realpath(os.curdir)
  paths=sys.path
  for p in paths:
    n=os.path.join(p, 'py2des.py')
    if os.path.exists(n):
      os.chdir(p)
  self.openMetaModel("DCharts")
  os.chdir(old_path)

  self.ASGroot.Formalism_Name=ATOM3String('')
  self.ASGroot.Formalism_File=ATOM3String('')
  self.ASGroot.RowSize=ATOM3Integer(0)
  self.ASGroot.listNodes['ButtonConfig']=[]

def ATOM3_createMenu(self):
  pass

if __name__=='__main__':
  if len(sys.argv)<2:
    print 'Transform DCharts models (designed in AToM3) into model descriptions'
    print 'Usage: py2des <.des> <.des> ...'
    sys.exit(1)

  i=1
  while i<len(sys.argv):
    (fdir, fname)=os.path.split(sys.argv[i])
    if string.upper(fname[len(fname)-3:])!='.PY':
      print 'Unrecognized format of file "%s"' % fname
      sys.exit(2)
    fname=fname[:len(fname)-3]

    ATOM3.__init__=ATOM3_init
    ATOM3.createMenu=ATOM3_createMenu
    tk=Tk()
    atom3_instance=ATOM3(tk)

    # load model
    sys.path.insert(0, fdir)
    exec 'from %s import *' % fname

    if loadedMMName!='DCharts':
      print 'Unrecognized formalism "%s"' % loadedMMName
      sys.exit(3)

    newfunction(atom3_instance, atom3_instance.ASGroot)

    # transform (so simple!)
    desc=SVMAToM3Plugin.generate_description(atom3_instance, 0)['desc']

    # save
    desname=fname+'.des'
    file=open(desname, 'w')
    file.write(desc)
    file.close()

    # success
    print 'Model description successfully saved to "%s"' % desname

    i=i+1
