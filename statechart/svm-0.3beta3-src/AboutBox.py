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
from string import *
import thread
import time

class SimpleDialog:

    def __init__(self, master,
                 text=[], text_expand=0, buttons=[], default=None, cancel=None,
                 title=None, class_=None):
        if class_:
            self.root = Toplevel(master, class_=class_)
        else:
            self.root = Toplevel(master)
	self.root.state("withdrawn")
        if title:
            self.root.title(title)
            self.root.iconname(title)
        self.message = []
        index=0
        self.messagepan=Frame(self.root)
        self.messagepan.pack(side=TOP, expand=1, fill=BOTH)
        self.bottompan=Frame(self.root)
        self.bottompan.pack(side=BOTTOM, fill=X)
        for msg in text:
          m = Label(self.messagepan, text=msg)
          m.pack(side=TOP, expand=(index==text_expand), fill=BOTH)
          index=index+1
          self.message.append(m)
        self.frame = Frame(self.bottompan)
        self.frame.pack()
        self.num = default
        self.cancel = cancel
        self.default = default
        self.root.bind('<Return>', self.return_event)
        self.buttons=[]
        for num in range(len(buttons)):
            s = buttons[num]
            b = Button(self.frame, text=s,
                       command=(lambda self=self, num=num: self.done(num)))
            if num == default:
                b.config(relief=RIDGE, borderwidth=8)
            b.pack(side=LEFT, fill=BOTH, expand=1)
            self.buttons.append(b)
        self.root.protocol('WM_DELETE_WINDOW', self.wm_delete_window)
        self._set_transient(master)
	self.root.resizable(height=0, width=0)
	self.place_window()
	self.root.state("normal")

    def place_window(self):
        widget=self.root
        m_width=widget.winfo_screenwidth()
        m_height=widget.winfo_screenheight()
        x=(m_width-widget.winfo_reqwidth())/2
        y=(m_height-widget.winfo_reqheight())/2
        widget.geometry("+%d+%d" % (x, y))

    def _set_transient(self, master):
        widget = self.root
        widget.transient(master)
        widget.update_idletasks() # Actualize geometry information

    def go(self):
        self.root.grab_set()
        self.root.mainloop()
        self.root.destroy()
        return self.num

    def return_event(self, event):
        if self.default is None:
            self.root.bell()
        else:
            self.done(self.default)

    def wm_delete_window(self):
        if self.cancel is None:
            self.root.bell()
        else:
            self.done(self.cancel)

    def done(self, num):
        self.num = num
        self.root.quit()

ABOUT_LOGO1='Python Implementation of Statechart Virtual Machine\n\
Version 0.3\n\
Presented by Thomas Feng, Nov. 2003'
ABOUT_LOGO2='Usage: svm [options...] <.des|.snp file> [parameters...]\n\
-c: force curses interface (Linux)\n\
-t: force textual interface\n\
-i <file>: include a file (to the head)\n\
-I <file>: include a file (to the tail)\n\
parameter: "name=value"'

EXAMPLE='Example:%s\nsvm DataTypes/Integer.des "INIT=5"'%ljust('', 48)

class AboutBox (SimpleDialog):
 def __init__(self, master):
   SimpleDialog.__init__(self, master, [ABOUT_LOGO1, ABOUT_LOGO2, EXAMPLE], 0, ['Close'], 1, 0, 'About SVM')
   self.message[0].config(font=('Arial', 9, 'bold'), fg='red', relief=GROOVE, bg='lightblue')
   self.message[1].config(font=('Fixed', 10), fg='blue', bd=5, bg='#FFC0C0')
   self.message[2].config(font=('Fixed', 10), fg='blue', bg='#FFC0C0', relief=GROOVE)
   self.bottompan.config(bg='#FFC0C0')
   self.buttons[0].config(fg='brown', font=('Arial', 8, 'bold'), relief=GROOVE, bg='lightyellow', cursor='hand1')
   self.buttons[0].focus_force()
   
