#
# MP3PlayerGUI.py
#
# class MP3PlayerGUI provides a simple Tkinter GUI for an MP3 player
#
# Instantiating the class sets up the MP3 player widgets in a Frame
# and binds user-initiated GUI events such as clicking on a Button
# to methods of class MP3PlayerGUI.
#
# These methods (window_close, ..., fbackwd_released)
# send an event (a string such as 'GUI Forward Pressed') to
# the SVM executive so the Statechart can react to it.
#
# Events which the Statechart may receive
# (and hence needs to handle) are:
# 'GUI Quit'
# 'GUI Debug'
# 'GUI Play/Pause'
# 'GUI Stop'
# 'GUI Forward Pressed'
# 'GUI Forward Released'
# 'GUI Backward Pressed'
# 'GUI Backward Released'
#
# The methods set_time, hide_time, and show_time
# can be called from the Statechart to alter parts of the 
# visual appearance of the GUI.

from Tkinter import *
import os

DEBUGKEY='d'

#======================================================================#
# GUI class

class MP3PlayerGUI(Frame):

 def __init__(self, parent, eventhandler):
   Frame.__init__(self, parent)
   self.parent = parent
   self.eventhandler=eventhandler
   self.createWidgets()
   self.b_playpause.focus_force()
   self.parent.protocol("WM_DELETE_WINDOW", self.window_close)

 def find_file(self, name):
   paths=sys.path
   for p in paths:
     try:
       n=os.path.join(p, name)
       if os.path.exists(n):
         return n
     except:
       pass
   return name

 def window_close(self):
   self.eventhandler.event('GUI Quit')

 def key_stroke(self, e):
   self.eventhandler.event('GUI Debug')

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

 def createWidgets(self):

   f_left = Frame(self.parent)
   f_left.pack(side = LEFT, fill = Y)

   b_descr = Label(f_left, text='MP3 Player', 
                           width= 12, 
			   fg="darkgreen", relief=GROOVE) 
   b_descr.pack(side = LEFT, fill = Y)

   f_right = Frame(self.parent)
   f_right.pack(side = RIGHT)

   f_row1 = Frame(f_right)
   f_row1.pack(side = TOP)
   self.b_playpauseImg = PhotoImage(file=self.find_file("PlayPause.gif"))
   self.b_playpause = Button(f_row1, image=self.b_playpauseImg, 
                             height=25, width=49,
			     relief=RAISED, command = self.play_pressed)
   self.b_playpause.pack(side = LEFT)
   self.b_playpause.bind(DEBUGKEY, self.key_stroke)
   self.b_stopImg = PhotoImage(file=self.find_file("Stop.gif"))
   self.b_stop = Button(f_row1, image=self.b_stopImg, 
                        height=25, width=25,
                        relief=RAISED, command = self.stop_pressed)
   self.b_stop.pack(side = LEFT)
   self.b_stop.bind(DEBUGKEY, self.key_stroke)

   f_row2 = Frame(f_right)
   f_row2.pack(side = TOP)

   self.b_fbackImg = PhotoImage(file=self.find_file("Rew.gif"))
   self.b_fback = Button(f_row2, image=self.b_fbackImg,
                         height=25, width=37)
   self.b_fback.bind('<Button-1>', self.fbackwd_pressed)
   self.b_fback.bind('<ButtonRelease-1>', self.fbackwd_released)
   self.b_fback.pack(side = LEFT)
   self.b_fback.bind(DEBUGKEY, self.key_stroke)

   self.b_ffwdImg = PhotoImage(file=self.find_file("Fwd.gif"))
   self.b_ffwd = Button(f_row2, image=self.b_ffwdImg, 
                        height=25, width=38)
   #self.b_ffwd = Button(f_row2, relief=RAISED, image=self.b_ffwdImg), 
   self.b_ffwd.bind('<Button-1>', self.ffwd_pressed)
   self.b_ffwd.bind('<ButtonRelease-1>', self.ffwd_released)
   self.b_ffwd.pack(side = LEFT)
   self.b_ffwd.bind(DEBUGKEY, self.key_stroke)

   f_row3 = Frame(f_right)
   f_row3.pack(side = TOP)

   f_middle = Frame(self.parent, 
                     bg = 'black', relief = 'sunken', 
	             height = 100, width = 300, borderwidth = 1)
   f_middle.pack(side = LEFT, fill = Y)

   Label(f_middle, text = "", bg = 'black',
	                      width = 20, borderwidth = 1).pack(side = TOP)

   self.timestr = StringVar()
   self.timestr.set('00:00')
   self.timelb = Label(f_middle, textvariable = self.timestr, bg = 'black', 
                           font='lucidasans-24',
	                   fg = 'green', width = 10, borderwidth = 1)
   self.timelb.pack(fill = Y)

   Label(f_middle, text = "", bg = 'black',
	                      width = 20, borderwidth = 1).pack(side = TOP)

 def set_time(self, timestr='00:00'):
   self.timestr.set(timestr)

 def hide_time(self):
   self.timelb.config(fg='black')

 def show_time(self):
   self.timelb.config(fg='green')

