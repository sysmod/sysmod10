from Tkinter import *
import os
import string

class MP3SelectorGUI(Toplevel):

 def __init__(self, parent, eventhandler):
   self.drives=[]
   if os.name!="posix":  # search for drives in Windows
     letter='A'
     while letter<='Z':
       drive="%s:\\"%letter
       if os.path.isdir(drive):
         self.drives.append(drive)
       letter=chr(ord(letter)+1)

   Toplevel.__init__(self, parent)
   self.title("MP3 Selector")
   self.parent=parent
   self.eventhandler=eventhandler
   self.curdir=os.path.abspath('.')
   self.createWidgets()
   self.protocol("WM_DELETE_WINDOW", self.window_close)

 def window_close(self):
   pass

 def mp3_list_dblclick(self, e):
   index=self.mp3_list.nearest(e.y)
   if index>=0:
     bbox=self.mp3_list.bbox(index)
     if bbox[1]<=e.y and bbox[1]+bbox[3]>=e.y:
       fname=self.mp3_list.get(index)
       if fname=='.':
         itemname=self.curdir
       elif fname=='..':
         [dir1, dir2]=os.path.split(self.curdir)
         if dir2:
           itemname=dir1
         else:
           itemname=""  # top-level directory in Windows
       else:
         itemname=os.path.join(self.curdir, self.mp3_list.get(index))
       self.eventhandler.event('Select', [itemname])

 def set_folder_item(self, pos):
   if pos%2==0:
     self.mp3_list.itemconfig(pos, foreground='blue', background='#F0F000')
   else:
     self.mp3_list.itemconfig(pos, foreground='blue', background='#E0E000')

 def set_mp3_item(self, pos):
   if pos%2==0:
     self.mp3_list.itemconfig(pos, foreground='red', background='#FFFFFF')
   else:
     self.mp3_list.itemconfig(pos, foreground='red', background='#E0FFE0')

 def update_dir(self, path):
   if path!="":
     absdir=os.path.abspath(path)
     self.curdir=absdir
     try:
       files=os.listdir(absdir)
       files.sort()
     except:
       print "ERROR: could not list dir \"%s\""%absdir
       return
   else:
     absdir=""
     self.curdir=""
     files=self.drives
   pathsp=os.path.split(absdir)
   size=self.mp3_list.size()
   if size>0:
     self.mp3_list.delete(0, size-1)
   pos=0
   self.mp3_list.insert(pos, '.')
   self.set_folder_item(pos)
   pos=pos+1
   if path!="" and not ((self.drives!=[] and pathsp[0]=="") or (self.drives==[] and pathsp[0]==path) and pathsp[1]==''):
     self.mp3_list.insert(pos, '..')
     self.set_folder_item(pos)
     pos=pos+1

   # directories
   dirs=[]
   for f in files:
     if os.path.isdir(os.path.join(absdir, f)):
       dirs.append(f)

   # MP3 files
   mp3f=[]
   for f in files:
     if len(f)>4 and string.upper(f[len(f)-4:])=='.MP3' and not os.path.isdir(os.path.join(absdir, f)):
       mp3f.append(f)

   # insert
   apply(self.mp3_list.insert, [pos]+dirs+mp3f)
   for f in dirs:
     self.set_folder_item(pos)
     pos=pos+1
   for f in mp3f:
     self.set_mp3_item(pos)
     pos=pos+1

   # update the status bar
   self.status.delete(1.0, END)
   self.status.insert(1.0, absdir) 

 def createWidgets(self):
   f_top=Frame(self)
   f_top.pack(side=TOP, fill=X)

   panel_desc=Label(f_top, text='List of Current Folder',
                           fg="darkgreen", relief=GROOVE)
   panel_desc.pack(side=TOP, fill=X)

   f_mid=Frame(self)
   f_mid.pack(side=TOP, expand=1, fill=BOTH)

   self.mp3_list=Listbox(f_mid, bg='white', relief=GROOVE,
                      font=('Fixed', 9), height=20, width=30, cursor='hand2')
   mp3_yscroll=Scrollbar(f_mid, command=self.mp3_list.yview)
   mp3_yscroll.pack(side=RIGHT, fill=Y)
   mp3_xscroll=Scrollbar(f_mid, command=self.mp3_list.xview, orient=HORIZONTAL)
   mp3_xscroll.pack(side=BOTTOM, fill=X)
   self.mp3_list.config(xscrollcommand=mp3_xscroll.set, yscrollcommand=mp3_yscroll.set)
   self.mp3_list.pack(side=TOP, expand=1, fill=BOTH)

   self.status=Text(self, relief=GROOVE, font=('Fixed', 9), #wrap=CHAR,
                    height=1, width=0, background='lightblue')
   self.status.pack(side=BOTTOM, fill=X)

   self.mp3_list.bind('<Double-Button-1>', self.mp3_list_dblclick)

   self.update_dir(self.curdir)
