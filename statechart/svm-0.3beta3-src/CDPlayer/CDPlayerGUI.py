#---------------------------------------------------------------------
#    SVM (Statechart Virtual Machine)
#         -- an interpreter for an extended statechart formalism
#---------------------------------------------------------------------
#
# Copyright (C) 2003 Thomas Huining Feng
#
#---------------------------------------------------------------------
# Address:      MSDL, SOCS, McGill Univ., Montreal, Canada
# HomePage:     http://msdl.cs.mcgill.ca/people/tfeng/
# SVM HomePage: http://msdl.cs.mcgill.ca/people/tfeng/?research=svm
# Download:     http://savannah.nongnu.org/files/?group=svm
# CVS:          :pserver:anoncvs@subversions.gnu.org:/cvsroot/svm
#               (projects "svm" and "jsvm")
# Email:        hfeng2@cs.mcgill.ca
#---------------------------------------------------------------------
#
# This file is part of SVM.
#
#---------------------------------------------------------------------
# SVM is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your
# option) any later version.
#
# SVM is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public
# License for more details.
#
# You should have received a copy of the GNU General Public License
# along with SVM; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
#---------------------------------------------------------------------


from Tkinter import *
import os.path

DEBUGKEY='d'
SNAPKEY='s'

#======================================================================#
# GUI class

class CDPlayerGUI(Frame):

 def __init__(self, parent, eventhandler, cdcount=1):
   Frame.__init__(self, parent)
   self.parent = parent
   self.eventhandler=eventhandler
   self.createWidgets()
   self.b_eject.focus_force()
   self.parent.resizable(0, 0)
   parent.protocol("WM_DELETE_WINDOW", self.window_close)

 def window_close(self):
   self.eventhandler.event('GUI Quit')

 def key_stroke(self, e):
   if e.keysym==DEBUGKEY:
     self.debug()
   elif e.keysym==SNAPKEY:
     self.take_snapshot()
 
 def debug(self):
   self.eventhandler.event('GUI Debug')

 def take_snapshot(self):
   self.eventhandler.event('Take Snapshot')
 
 def change_cdrom(self, e):
   self.eventhandler.event('CD '+str(self.cd_list.curselection()[0]))

 def eject_pressed(self):
   self.eventhandler.event('GUI Eject')

 def play_pressed(self):
   self.eventhandler.event('GUI Play/Pause')

 def stop_pressed(self):
   self.eventhandler.event('GUI Stop')

 def ffwd_pressed(self, e):
   self.eventhandler.event('GUI Forward Pressed')

 def ffwd_released(self, e):
   self.eventhandler.event('GUI Forward Released')

 def fbackwd_pressed(self, e):
   self.eventhandler.event('GUI Backward Pressed')

 def fbackwd_released(self, e):
   self.eventhandler.event('GUI Backward Released')

 def track_Forward(self):
   self.eventhandler.event('GUI Track Forward')

 def track_back(self):
   self.eventhandler.event('GUI Track Backward')

 def createWidgets(self):

   toppan = Frame(self.parent)
   toppan.pack(side=TOP, fill=X)
   midpan = Frame(self.parent)
   midpan.pack(side=TOP, fill=X, expand=1)
   botpan = Frame(self.parent)
   botpan.pack(side=TOP, fill=X)
   
   f_left = Frame(toppan)
   f_left.pack(side = LEFT)

   b_descr = Label(f_left, text='CDplay', 
                           height = 4, width= 12, 
			   fg="darkgreen", relief=GROOVE) 
   b_descr.pack(side = TOP)

   self.b_eject = Button(f_left, text='Eject', 
                            width = 10, 
			    command = self.eject_pressed )

   self.b_eject.pack(side = TOP)
   self.b_eject.bind('<KeyPress>', self.key_stroke)

   f_right = Frame(toppan)
   f_right.pack(side = RIGHT)

   f_row1 = Frame(f_right)
   f_row1.pack(side = TOP)
   self.b_playpause = Button(f_row1, text='Play/Pause', 
                               width=8, 
			       command = self.play_pressed)
   self.b_playpause.pack(side = LEFT)
   self.b_playpause.bind(DEBUGKEY, self.key_stroke)
   self.b_stop = Button(f_row1, text='Stop', 
                           width=8,
                           command = self.stop_pressed)
   self.b_stop.pack(side = LEFT)
   self.b_stop.bind(DEBUGKEY, self.key_stroke)

   f_row2 = Frame(f_right)
   f_row2.pack(side = TOP)

   self.b_fback = Button(f_row2, text='<<', 
                            width = 8)
   self.b_fback.bind('<Button-1>', self.fbackwd_pressed)
   self.b_fback.bind('<ButtonRelease-1>', self.fbackwd_released)
   self.b_fback.pack(side = LEFT)
   self.b_fback.bind(DEBUGKEY, self.key_stroke)

   self.b_ffwd = Button(f_row2, text='>>', 
                           width = 8)
   self.b_ffwd.bind('<Button-1>', self.ffwd_pressed)
   self.b_ffwd.bind('<ButtonRelease-1>', self.ffwd_released)
   self.b_ffwd.pack(side = LEFT)
   self.b_ffwd.bind(DEBUGKEY, self.key_stroke)

   f_row3 = Frame(f_right)
   f_row3.pack(side = TOP)

   self.b_tback = Button(f_row3, text='|<<', 
                            width = 8, 
	  		    command = self.track_back)
   self.b_tback.pack(side = LEFT)
   self.b_tback.bind(DEBUGKEY, self.key_stroke)

   self.b_tfwd = Button(f_row3, text='>>|', 
                           width = 8, 
		           command = self.track_Forward)
   self.b_tfwd.pack(side = LEFT)
   self.b_tfwd.bind(DEBUGKEY, self.key_stroke)

   f_middle = Frame(toppan, 
                     bg = 'black', relief = 'sunken', 
	             height = 100, width = 300, borderwidth = 1)
   f_middle.pack(side = TOP, expand=1, fill=X)

   Label(f_middle, text = "", bg = 'black',
	                      width = 20, borderwidth = 1).pack(side = TOP, expand=1, fill=X)

   self.timestr = StringVar()
   l_timestr = Label(f_middle, textvariable = self.timestr, bg = 'black', 
                           font='lucidasans-24',
	                   fg = 'green', width = 10, borderwidth = 1)
   l_timestr.pack()

   self.trackstr = StringVar()
   self.trackstr.set('[track 12]')
   l_trackstr = Label(f_middle, textvariable = self.trackstr, bg = 'black',
	                   fg = 'green', width = 20, borderwidth = 1)
   l_trackstr.pack(side = TOP)
   
   Label(midpan, height=0, relief=GROOVE, text='Advanced', fg='red').pack(side=TOP, fill=X, expand=1)
   
   dbg_btn = Button(botpan, text='Debug (d)', command=self.debug)
   dbg_btn.pack(side=LEFT, fill=Y)
   dbg_btn.bind('<KeyPress>', self.key_stroke)

   snp_btn = Button(botpan, text='Snapshot (s)', command=self.take_snapshot)
   snp_btn.pack(side=LEFT, fill=Y)
   snp_btn.bind('<KeyPress>', self.key_stroke)

   Label(botpan, width=10, text='CDRom', fg='blue').pack(side=LEFT)
   self.cd_list = Listbox(botpan, height=2)
   self.cd_list.pack(side=LEFT, fill=BOTH, expand=1)
   y_scroll=Scrollbar(botpan, command=self.cd_list.yview)
   y_scroll.pack(side=RIGHT, fill=Y)
   y_scroll.bind('<KeyPress>', self.key_stroke)
   self.cd_list.config(yscrollcommand=y_scroll.set)
   self.cd_list.bind('<<ListboxSelect>>', self.change_cdrom)
   self.cd_list.bind('<KeyPress>', self.key_stroke)

   Label(f_middle, text = "", bg = 'black',
	                      width = 20, borderwidth = 1).pack(side = TOP)

 def set_cd_count(self, cdcount):
   self.cd_list.delete(0, END)
   for i in range(cdcount):
     self.cd_list.insert(i, 'CD '+str(i))
 
 def select_cd(self, cdnum):
   self.cd_list.select_set(cdnum)
