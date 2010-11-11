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


from string import *
from Tkinter import *
import tkFont
import Debugger
import sys
import StringUtil
from AboutBox import AboutBox
import os.path
import re
from string import *
import thread
import time
import ThreadUtil
from Clock import *
from StringUtil import *

DEBUG_STRING='debug'

class FakedLock:
  def acquire(self):
    pass
  def release(self):
    pass

gui_lock=ThreadUtil.AllocateLock()

#======================================================================#
# GUI classes

class DefaultGUI(Frame):

 def __init__(self, parent, eventhandler, debugger, showhierarchy=1):
   gui_lock.acquire()
   parent.state("withdrawn")
   Frame.__init__(self, parent)
   self.eventhandler=eventhandler
   self.debugger=debugger
   self.debug=0
   self.show_stateH=0
   self.path_index=[]
   self.current_states=[]
   self.command_list=[]
   self.events=[]
   self.state_list_init=0
   self.syn=re.compile('([a-zA-Z0-9_]+)|(".*?")|(\'.*?\')|([%s]+)' % StringUtil.OPERATORS)
   self.command_index=-1
   parent.title('Statechart Virtual Machine - Thomas (Nov. 2003)')
   self.parent = parent
   parent.protocol("WM_DELETE_WINDOW", self.window_close)
   self.createWidgets(showhierarchy)
   self.debugger.CustomizeEvent(self.event_callback, None, 1)
   self.place_windows()
   parent.state("normal")
   if showhierarchy:
     self.hierarchy.state("normal")
   gui_lock.release()
   
 def place_windows(self):
   self.bwidth=(self.parent.winfo_screenwidth()-self.parent.maxsize()[0])/2
   sw=self.parent.winfo_screenwidth()
   sh=self.parent.winfo_screenheight()
   self.parent.update_idletasks()
   mw=self.parent.winfo_reqwidth()
   mh=self.parent.winfo_reqheight()
   if hasattr(self, "hierarchy"):
     hw=self.hierarchy.winfo_reqwidth()
     hh=self.hierarchy.winfo_reqheight()
   else:
     hw=0
     hh=mh

   left=(sw-mw-hw-self.bwidth*2)/2
   top=(sh-hh)/2
   if hasattr(self, "hierarchy"):
     self.hierarchy.geometry("+%d+%d"%(left,top))
   left=left+hw+self.bwidth
   self.parent.geometry("+%d+%d"%(left,top))
   self.settop=top
   self.setleft=left
   #self.parent.protocol("WM_TAKE_FOCUS", self.record_btop)
   ThreadUtil.StartThread(self.record_btop, ())

 def record_btop(self):
   #import time
   time.sleep(0.05)
   gui_lock.acquire()
   self.bwidth=self.parent.winfo_x()-self.setleft
   self.btop=self.parent.winfo_y()-self.settop
   gui_lock.release()
   del self.settop
   del self.setleft

 def dummy_fnc(self):
   pass

 def show_about_box(self):
   gui_lock.acquire()
   about=AboutBox(self)
   gui_lock.release()
   about.go()

 def window_close(self):
   if hasattr(self, "hierarchy"):
     self.hierarchy.destroy()
   if self.debug:
     self.stop_debug()
   gui_lock.acquire()
   self.eventhandler.stop_all_clocks()
   #self.eventhandler.handle_event_lock.acquire()
   gui_lock.release()
   self.eventhandler.shutdown()
   gui_lock.acquire()
   self.parent.destroy()
   gui_lock.release()
 
 def send_output(self, data, tag=None):
   gui_lock.acquire()
   self.output_text.insert(END, data, tag)
   self.output_text.see(END)
   gui_lock.release()
 
 def up_command(self, e):
   gui_lock.acquire()
   command=self.command_text.get(1.0, '%s-1c'%END)
   l=len(self.command_list)
   if l>0 and self.command_index>0 and (not command or \
          (self.command_index<l and self.command_list[self.command_index]==command)):
     self.command_index=self.command_index-1
     self.command_text.delete(1.0, END)
     self.command_text.insert(1.0, self.command_list[self.command_index])
     self.command_text.see(INSERT)
   gui_lock.release()
   self.check_syntax()
 
 def down_command(self, e):
   gui_lock.acquire()
   command=self.command_text.get(1.0, '%s-1c'%END)
   l=len(self.command_list)
   if l>0 and self.command_index<l-1 and (not command or \
          (self.command_index>=0 and self.command_list[self.command_index]==command)):
     self.command_index=self.command_index+1
     self.command_text.delete(1.0, END)
     self.command_text.insert(1.0, self.command_list[self.command_index])
     self.command_text.see(INSERT)
   gui_lock.release()
   self.check_syntax()
 
 def toggle_debug(self, e):
   if self.debug:
     self.stop_debug()
   else:
     self.start_debug()

 def is_keyword(self, word, level=None, keywords=StringUtil.KEYWORDS):
   if not level:
     for k in keywords:
       if word in k:
         return 1
     return 0
   else:
     return word in keywords[level-1]

 def check_syntax_thread(self):
   time.sleep(0.1)
   gui_lock.acquire()
   text=self.command_text.get(1.0, '%s-1c'%END)
   cl=int(split(self.command_text.index(INSERT), '.')[0])-1
   text=split(text, '\n')
   i=0
   left=''
   while i<=cl:
     left=left+text[i]
     if i<cl:
       left=left+'\n'
     i=i+1
   startpos=rfind(left, '\n')+1
   maxline=len(split(left, '\n'))
   line=text[maxline-1]
   if self.debug:
     keywords=StringUtil.KEYWORDS+[StringUtil.DEBUG_KEYWORDS]
   else:
     keywords=[StringUtil.NONDEBUG_KEYWORDS+self.events]
   if line in self.events and not self.debug:
     self.command_text.tag_add('ultra', 1.0, "end-1c")
   else:
     pos=0
     while pos>=0:
       s=self.syn.search(line, pos)
       if s:
         pos=s.end()
         word=line[s.start():s.end()]
         for t in range(len(keywords)):
           if self.is_keyword(word, t+1, keywords):
             self.command_text.tag_remove('string', "%d.%d" % (maxline, s.start()), "%d.%d" % (maxline, s.end()))
             if t+1==len(keywords):
               self.command_text.tag_add('ultra', "%d.%d" % (maxline, s.start()), "%d.%d" % (maxline, s.end()))
             else:
               self.command_text.tag_add('level_%d' % (t+1), "%d.%d" % (maxline, s.start()), "%d.%d" % (maxline, s.end()))
           else:
             if len(word)>=2 and ((word[0]=='"' and word[len(word)-1]=='"') or (word[0]=='\'' and word[len(word)-1]=='\'')):
               self.command_text.tag_add('string', "%d.%d" % (maxline, s.start()+1), "%d.%d" % (maxline, s.end()-1))
             else:
               self.command_text.tag_remove('string', "%d.%d" % (maxline, s.start()), "%d.%d" % (maxline, s.end()))
               if t+1==len(keywords):
                 self.command_text.tag_remove('ultra', "%d.%d" % (maxline, s.start()), "%d.%d" % (maxline, s.end()))
               else:
                 self.command_text.tag_remove('level_%d' % (t+1), "%d.%d" % (maxline, s.start()), "%d.%d" % (maxline, s.end()))
       else:
         pos=-1
   gui_lock.release()

 def check_syntax(self):
   ThreadUtil.StartThread(self.check_syntax_thread, ())

 def handle_keystroke(self, e):
   gui_lock.acquire()
   self.command_index=len(self.command_list)
   gui_lock.release()
   self.check_syntax()
   
 def create_command_text(self, height=1):
   self.command_height=height
   self.command_text=Text(self.commandbar, relief=GROOVE, height=1, wrap=NONE, font=('Fixed', 10), width=60)
   self.command_text.pack(side=BOTTOM, fill=X)
   self.command_text.config(height=height)
   self.command_text.bind('<Return>', self.command_enter)
   self.command_text.bind('<Up>', self.up_command)
   self.command_text.bind('<Down>', self.down_command)
   self.command_text.bind('<Control-s>', self.take_snapshot)
   self.command_text.bind('<Control-d>', self.toggle_debug)
   self.command_text.bind('<Key>', self.handle_keystroke)
   self.command_text.tag_config('normal', foreground='black')
   self.command_text.tag_config('level_1', foreground='blue')
   self.command_text.tag_config('level_2', foreground='red')
   self.command_text.tag_config('level_3', foreground='magenta')
   self.command_text.tag_config('ultra', foreground='red', background='yellow', borderwidth='1', relief=GROOVE)
   self.command_text.tag_config('string', foreground='#008000')
   self.command_text.focus_force()
 
 def command_enter(self, e):
   gui_lock.acquire()
   command=self.command_text.get(1.0, '%s-1c'%END)
   gui_lock.release()
   self.execute_command(command)
 
 def append_command(self, command):
   l=len(self.command_list)
   if l==0 or command!=self.command_list[l-1]:
     self.command_list.append(command)
     self.command_index=self.command_index+1
     
 def start_debug(self):
   self.eventhandler.handle_event_lock.acquire()
   Debugger.DefaultInterpreter.output=self.send_output
   self.old_stdout=sys.__stdout__
   sys.stdout=Debugger.DefaultInterpreter
   self.debug=1
   self.lastprompt=''
   self.debugger.OutputInterruptLogo(DEBUG_STRING)
   gui_lock.acquire()
   self.command_height=5
   self.command_text.config(height=self.command_height)
   gui_lock.release()
   self.clear_command_text()
   
 def stop_debug(self):
   sys.stdout=self.old_stdout
   self.debug=0
   self.debugger.OutputLeaveMessage()
   gui_lock.acquire()
   self.command_height=1
   self.command_text.config(height=self.command_height)
   gui_lock.release()
   self.clear_command_text()
   self.update_event_list()
   self.eventhandler.handle_event_lock.release()
      
 def execute_command(self, command):
   scommand=strip(command)
   self.command_index=len(self.command_list)
   if scommand=='exit' and not self.debug:
     self.window_close()
   elif scommand=='exit' and self.debug:
     self.append_command('exit')
     self.send_output('>>> exit\n', 'debug')
     self.stop_debug()
   elif scommand==DEBUG_STRING and not self.debug:
     self.append_command(DEBUG_STRING)
     self.send_output('[EVENT] > %s\n'%DEBUG_STRING, 'event')
     self.start_debug()
   elif self.debug:
     err=self.debugger.CheckSource(command)
     if err!=2:
       self.send_output('>>> '+replace(command, '\n', '\n... ')+'\n', 'debug')
     self.lastprompt=self.debugger.RunSource(command)
     if not self.lastprompt:
       self.append_command(command)
       self.clear_command_text()
   else:
     self.append_command(scommand)
     self.send_output('[EVENT] > '+scommand+'\n', 'event')

     self.eventhandler.event(EventObject(scommand))
     
     self.clear_command_text()

 def clear_command_text(self):
   ThreadUtil.StartThread(self.clear_command_text_thread, ())

 def clear_command_text_thread(self):
   gui_lock.acquire()
   self.command_text.delete(1.0, END)
   gui_lock.release()
 
 def update_event_list(self):
   gui_lock.acquire()
   self.events=self.eventhandler.get_enabled_events()
   self.event_list.delete(0, END)
   self.light_state=0
   index=0
   for e in self.events:
     if len(e)>=2 and e[:2]=='__':  # hide internal events starting with "__"
       continue
     self.event_list.insert(index, e)
     index=index+1
     self.set_list_item_color(self.event_list)
   gui_lock.release()
 
 def set_list_item_color(self, l, highlighted=0, index=END, check_in_list=0):
   try:
     if highlighted:
       if not check_in_list or self.current_states[index]!='h':
         l.itemconfig(index, foreground='red', background='yellow')
         l.see(index)
         if check_in_list:
           self.current_states[index]='h'
     elif self.light_state:
       if not check_in_list or self.current_states[index]!='l':
         l.itemconfig(index, foreground='darkblue', background='white')
         if check_in_list:
           self.current_states[index]='l'
     else:
       if not check_in_list or self.current_states[index]!='d':
         l.itemconfig(index, foreground='darkblue', background='#F0F0FF')
         if check_in_list:
           self.current_states[index]='d'
     self.light_state=not self.light_state
   except:
     return

 def insert_list_item(self, l, name, index=END, check_in_list=0):
   l.insert(index, name)
   if check_in_list:
     self.current_states.insert(index, None)

 def update_state_list_rec(self, states, path, level, update_color_only=0):
   for s in sortlist(states.keys()):
     if not s in StringUtil.StateProperties:
       has_substate=0
       for ss in states[s].keys():
         if not ss in StringUtil.StateProperties:
           has_substate=1
           break
       state=''
       for i in range(level):
         state=state+'   '
       if has_substate:
         state=state+'+ '
       else:
         state=state+'- '
       state=state+s
       p=self.eventhandler.append_path(path, s)
       if self.state_index<0:
         index=0
       else:
         index=self.state_index
       try:
         if not update_color_only:
           self.insert_list_item(self.state_list, state, index+1, 1)
           self.path_index.insert(index+1, p)
         self.set_list_item_color(self.state_list, p in self.eventhandler.state, index, 1)
       except:
         1
       self.state_index=self.state_index+1
       if has_substate:
         self.update_state_list_rec(states[s], p, level+1, update_color_only)
 
 def get_state_index_rec(self, curpath, path, states):
   self.state_index=self.state_index+1
   for s in sortlist(states.keys()):
     if not s in StringUtil.StateProperties:
       cp=self.eventhandler.append_path(curpath, s)
       if curpath==path:
         return 1
       res=self.get_state_index_rec(cp, path, states[s])
       if res:
         return 1
   return 0
 
 def get_state_index(self, path, states):
   gui_lock.acquire()
   self.state_index=0
   self.get_state_index_rec('', path, states)
   self.state_index=self.state_index-2
   gui_lock.release()

 def insert_states(self, path):
   gui_lock.acquire()
   states=self.eventhandler.stateH
   ps=split(path, '.')
   level=0
   for p in ps:
     if p:
       level=level+1
       states=states[p]
   self.update_state_list_rec(states, path, level)
   gui_lock.release()
 
 def update_state_list(self, is_import, path=''):
   states=self.eventhandler.stateH
   if is_import or not self.state_list_init:
     self.state_list_init=1
     self.get_state_index(path, states)
     self.insert_states(path)

   self.light_state=0
   self.state_index=0
   gui_lock.acquire()
   self.update_state_list_rec(states, '', 0, 1)
   gui_lock.release()
 
 def event_list_dblclick(self, e):
   if not self.debug:
     for sel in self.event_list.curselection():
       self.execute_command(self.event_list.get(sel))
 
 def remove_input(self, e):
   gui_lock.acquire()
   self.status_str.set(str(self.eventhandler.state))
   gui_lock.release()
 
 def createWidgets(self, showhierarchy):
   label_font=('Arial', 10, 'bold')
   button_font=('Arial', 9, 'bold')
   
   mainframe=Frame(self.parent)
   mainframe.pack(side=TOP, fill=BOTH, expand=1)

   eventbar=Frame(mainframe)
   eventbar.pack(side=LEFT, fill=Y)
   eventxbar=Frame(eventbar)
   eventxbar.pack(side=BOTTOM, fill=X)
   
   event_label=Label(eventbar, text='Enabled Events', relief=GROOVE,
                     font=label_font, fg='blue', bg='lightblue')
   event_label.pack(side=TOP, fill=X)
   
   event_list=Listbox(eventbar, bg='white', relief=GROOVE, font=('Fixed', 10), cursor='hand2')
   event_list.pack(side=LEFT, fill=BOTH)
   
   event_yscroll=Scrollbar(eventbar, command=event_list.yview)
   event_yscroll.pack(side=RIGHT, fill=Y)
   event_xscroll=Scrollbar(eventxbar, command=event_list.xview, orient=HORIZONTAL)
   event_xscroll.pack(side=TOP, fill=X)
   event_list.config(xscrollcommand=event_xscroll.set)
   event_list.config(yscrollcommand=event_yscroll.set)
   event_list.bind('<Double-Button-1>', self.event_list_dblclick)
   
   mainframe=Frame(mainframe)
   mainframe.pack(side=TOP, fill=BOTH, expand=1)
   
   commandbar=Frame(mainframe)
   commandbar.pack(side=TOP, fill=BOTH, expand=1)
   
   outputbar=Frame(commandbar)
   outputbar.pack(side=TOP, fill=BOTH, expand=1)
   
   output_label=Label(outputbar, text='Output', relief=GROOVE,
                      font=label_font, fg='blue', bg='lightblue')
   output_label.pack(side=TOP, fill=X)
   
   output_text=Text(outputbar, relief=GROOVE, wrap=NONE, font=('Fixed', 10), height=15, width=0)
   output_text.pack(side=LEFT, fill=BOTH, expand=1)
   
   output_yscroll=Scrollbar(outputbar, command=output_text.yview)
   output_yscroll.pack(side=RIGHT, fill=Y)
   output_xscroll=Scrollbar(commandbar, command=output_text.xview, orient=HORIZONTAL)
   output_xscroll.pack(side=TOP, fill=X)
   output_text.config(xscrollcommand=output_xscroll.set)
   output_text.config(yscrollcommand=output_yscroll.set)
   output_text.tag_config('event', foreground='blue')
   output_text.tag_config('debug', foreground='magenta')
   output_text.tag_config('message', foreground='red', background='yellow')
   
   command_label=Label(commandbar, text='Command', relief=GROOVE,
                       font=label_font, fg='blue', bg='#FFC0C0')
   command_label.pack(side=TOP, fill=X)

   controlbar=Frame(mainframe)
   controlbar.pack(side=BOTTOM, fill=X)
   
   controlbar1=Frame(controlbar)
   controlbar1.pack(side=LEFT, fill=Y, expand=1)
   
   state_list_btn=Button(controlbar1, text='Show State Hierarchy', font=button_font,
                         fg='brown', relief=GROOVE, command=self.show_state_list,
                         cursor='hand1', bg='lightyellow')
   state_list_btn.pack(side=TOP, fill=Y)
   
   snap_btn=Button(controlbar, text='Snapshot', font=button_font,
                    fg='brown', relief=GROOVE, command=self.take_snapshot,
                    cursor='hand1', bg='lightyellow')
   snap_btn.pack(side=LEFT)

   about_btn=Button(controlbar, text='About SVM', font=button_font,
                    fg='brown', relief=GROOVE, command=self.show_about_box,
                    cursor='hand1', bg='lightyellow')
   about_btn.pack(side=LEFT)
   
   exit_btn=Button(controlbar, text='Exit', font=button_font,
                    fg='brown', relief=GROOVE, command=self.window_close,
                    cursor='hand1', bg='lightyellow')
   exit_btn.pack(side=RIGHT)

   self.status_str=StringVar()
   status_text=Entry(self.parent, relief=GROOVE, textvariable=self.status_str,
                     font=('Fixed', 10), justify=RIGHT, bg='lightblue')
   status_text.pack(side=BOTTOM, fill=X)
   status_text.bind('<KeyRelease>', self.remove_input)
   
   self.event_list=event_list
   self.output_text=output_text
   self.commandbar=commandbar
   self.status_text=status_text
   self.state_list_btn=state_list_btn
   self.label_font=label_font

   if showhierarchy:
     gui_lock.release()
     self.show_state_list(1)
     gui_lock.acquire()
   
   self.create_command_text()
 
 def show_state_list(self, withdrawn=0):
   gui_lock.acquire()
   self.create_hierarchy_window(withdrawn)
   gui_lock.release()
   self.update_state_list(1)
   self.show_stateH=1
   self.state_list_btn.config(state=DISABLED)
 
 def close_state_list(self):
   self.eventhandler.handle_event_lock.acquire()
   gui_lock.acquire()
   self.show_stateH=0
   self.hierarchy.destroy()
   self.state_list_btn.config(state=NORMAL)
   self.state_list_init=0
   gui_lock.release()
   self.eventhandler.handle_event_lock.release()

 def select_state_from_list(self, e):
   gui_lock.acquire()
   self.stateH_text.delete(1.0, END)
   for sel in self.state_list.curselection():
     if sel:
       self.stateH_text.insert(1.0, self.path_index[int(sel)])
       break
   gui_lock.release()
 
 def create_hierarchy_window(self, withdrawn=0):
   hierarchy=Toplevel()
   if withdrawn:
     hierarchy.state("withdrawn")
   hierarchy.title('State Hierarchy')
   hierarchy.protocol("WM_DELETE_WINDOW", self.close_state_list)
   
   name_label=Label(hierarchy, text=self.eventhandler.model_name, relief=GROOVE,
                       font=self.label_font, fg='blue', bg='lightblue')
   name_label.pack(side=TOP, fill=X)
   
   statebar=Frame(hierarchy)
   statebar.pack(side=TOP, fill=BOTH, expand=1)
   statexbar=Frame(hierarchy)
   statexbar.pack(side=TOP, fill=X)

   state_list=Listbox(statebar, bg='white', relief=GROOVE,
                      font=('Fixed', 10), height=20, width=30, cursor='hand2')
   state_list.pack(side=LEFT, expand=1, fill=BOTH)
   
   state_yscroll=Scrollbar(statebar, command=state_list.yview)
   state_yscroll.pack(side=RIGHT, fill=Y)
   state_xscroll=Scrollbar(statexbar, command=state_list.xview, orient=HORIZONTAL)
   state_xscroll.pack(side=TOP, fill=X)
   state_list.config(xscrollcommand=state_xscroll.set)
   state_list.config(yscrollcommand=state_yscroll.set)
   state_list.bind('<<ListboxSelect>>', self.select_state_from_list)
   
   stateH_text=Text(hierarchy, relief=GROOVE, wrap=WORD, font=('Fixed', 10),
                    height=3, width=0, bg='lightblue')
   stateH_text.pack(side=BOTTOM, fill=X, expand=0)

   self.hierarchy=hierarchy
   self.state_list=state_list
   self.stateH_text=stateH_text

   if hasattr(self, "bwidth") and hasattr(self, "btop"):
     left=self.parent.winfo_x()-self.bwidth*5-self.hierarchy.winfo_reqwidth()
     self.hierarchy.geometry("+%d+%d"%(left, self.parent.winfo_y()-self.btop))

 def event_callback(self, event, before, oldstate, newstate):
   gui_lock.acquire()
   self.status_str.set(str(self.eventhandler.state))
   gui_lock.release()
   self.update_event_list()
   if self.show_stateH:
     self.update_state_list(event==StringUtil.IMPORT_EVENT, oldstate)
 
 def take_snapshot(self, e=None):
   name=os.path.splitext(self.eventhandler.model_name)[0]+'.snp'
   self.eventhandler.snap_to_file(name)
   self.send_output('*** Execution snapshot saved to file "'+name+'" ***\n', 'message')

class DefaultCurses:
 def __init__(self, eventhandler, debugger):
   self.syn=re.compile('([a-zA-Z0-9_]+)|(".*?")|(\'.*?\')|([%s]+)' % StringUtil.OPERATORS)
   self.debugger=debugger
   self.events=[]
   self.eventhandler=eventhandler
   self.command_list=[]
   self.command_index=-1
   self.debugger.CustomizeEvent(self.event_callback, None, 1)

 def update_event_list(self):
   self.events=self.eventhandler.get_enabled_events()
   
 def event_callback(self, event, before, oldstate, newstate):
   self.update_event_list()
 
 def curses_get_str(self, isdebug=0):
   curses.noecho()
   s=''
   pos=0
   DefaultCurses.stdscr.keypad(1)
   startpos=DefaultCurses.stdscr.getyx()
   maxpos=DefaultCurses.stdscr.getmaxyx()
   ch=DefaultCurses.stdscr.getch()
   while not ch in [curses.KEY_ENTER, 10]:
     if ch==curses.ascii.ESC:
       (y, x)=self.get_cursor_pos(startpos, maxpos, 0, len(s))
       DefaultCurses.stdscr.addstr(y, x, ' '*len(s))
       s=''
       pos=0
       DefaultCurses.stdscr.move(y, x)
     elif ch==curses.KEY_LEFT and pos>0:
       pos=pos-1
       (y, x)=self.get_cursor_pos(startpos, maxpos, pos, len(s))
       DefaultCurses.stdscr.move(y, x)
     elif ch==curses.KEY_RIGHT and pos<len(s):
       pos=pos+1
       (y, x)=self.get_cursor_pos(startpos, maxpos, pos, len(s))
       DefaultCurses.stdscr.move(y, x)
     elif ch==curses.KEY_UP:
       l=len(self.command_list)
       if l>0 and self.command_index>0 and (not s or (self.command_index<l and self.command_list[self.command_index]==s)):
	 self.command_index=self.command_index-1
	 (y, x)=self.get_cursor_pos(startpos, maxpos, 0, len(s))
	 ss=s
	 s=self.command_list[self.command_index]
	 if len(s)<len(ss):
	   DefaultCurses.stdscr.addstr(y, x, s+' '*(len(ss)-len(s)))
	 else:
	   DefaultCurses.stdscr.addstr(y, x, s)
	 pos=len(s)
	 (y, x)=self.get_cursor_pos(startpos, maxpos, pos, len(s))
	 self.check_syntax(s, startpos, maxpos, isdebug)
	 DefaultCurses.stdscr.move(y, x)
     elif ch==curses.KEY_DOWN:
       l=len(self.command_list)
       if l>0 and self.command_index<l-1 and (not s or (self.command_index>=0 and self.command_list[self.command_index]==s)):
	 self.command_index=self.command_index+1
	 (y, x)=self.get_cursor_pos(startpos, maxpos, 0, len(s))
	 ss=s
	 s=self.command_list[self.command_index]
	 if len(s)<len(ss):
	   DefaultCurses.stdscr.addstr(y, x, s+' '*(len(ss)-len(s)))
	 else:
	   DefaultCurses.stdscr.addstr(y, x, s)
	 pos=len(s)
	 (y, x)=self.get_cursor_pos(startpos, maxpos, pos, len(s))
	 self.check_syntax(s, startpos, maxpos, isdebug)
	 DefaultCurses.stdscr.move(y, x)	 
     elif ch==curses.KEY_BACKSPACE and pos>0:
       s=s[0:pos-1]+s[pos:]
       pos=pos-1
       (y, x)=self.get_cursor_pos(startpos, maxpos, pos, len(s))
       DefaultCurses.stdscr.addstr(y, x, s[pos:]+' ')
       self.check_syntax(s, startpos, maxpos, isdebug)
       DefaultCurses.stdscr.move(y, x)
       self.command_index=len(self.command_list)
     elif ch==curses.KEY_DC and pos<len(s):
       s=s[0:pos]+s[pos+1:]
       (y, x)=self.get_cursor_pos(startpos, maxpos, pos, len(s))
       DefaultCurses.stdscr.addstr(y, x, s[pos:]+' ')
       self.check_syntax(s, startpos, maxpos, isdebug)
       DefaultCurses.stdscr.move(y, x)
       self.command_index=len(self.command_list)
     elif ch==curses.KEY_HOME:
       pos=0
       (y, x)=self.get_cursor_pos(startpos, maxpos, pos, len(s))
       DefaultCurses.stdscr.move(y, x)
     elif ch==curses.KEY_END:
       pos=len(s)
       (y, x)=self.get_cursor_pos(startpos, maxpos, pos, len(s))
       DefaultCurses.stdscr.move(y, x)
     else:
       try:
	 c=chr(ch)
	 if c in printable:
	   s=s[0:pos]+c+s[pos:]
	   DefaultCurses.stdscr.addstr(s[pos:])
	   pos=pos+1
	   l=len(s)
	   (y, x)=self.get_cursor_pos(startpos, maxpos, pos, len(s))
	   self.check_syntax(s, startpos, maxpos, isdebug)
	   DefaultCurses.stdscr.move(y, x)
	   self.command_index=len(self.command_list)
       except:
	 pass #DefaultCurses.stdscr.addstr(str(ch))
     ch=DefaultCurses.stdscr.getch()
   (y, x)=self.get_cursor_pos(startpos, maxpos, len(s), len(s))
   DefaultCurses.stdscr.move(y, x)
   DefaultCurses.stdscr.addch('\n')
   curses.echo()
   l=len(self.command_list)
   if l==0 or s!=self.command_list[l-1]:
     self.command_list.append(s)
     self.command_index=self.command_index+1
   return s

 def check_syntax(self, line, startpos, maxpos, isdebug):
   if isdebug:
     keywords=StringUtil.KEYWORDS+[StringUtil.DEBUG_KEYWORDS]
   else:
     keywords=[StringUtil.NONDEBUG_KEYWORDS+self.events]
   pos=0
   while pos>=0:
     s=self.syn.search(line, pos)
     if s:
       pos=s.end()
       word=line[s.start():s.end()]
       found=0
       for t in range(len(keywords)):
         if self.is_keyword(word, t+1, keywords):
           if t+1==len(keywords):
	     (sy, sx)=self.get_cursor_pos(startpos, maxpos, s.start(), len(line))
	     DefaultCurses.stdscr.addstr(sy, sx, word, curses.color_pair(3))
	     found=1
           else:
	     (sy, sx)=self.get_cursor_pos(startpos, maxpos, s.start(), len(line))
	     DefaultCurses.stdscr.addstr(sy, sx, word, curses.color_pair(t+4))
	     found=1
       if not found:
         if isdebug and len(word)>=2 and ((word[0]=='"' and word[len(word)-1]=='"') or (word[0]=='\'' and word[len(word)-1]=='\'')):
	   (sy, sx)=self.get_cursor_pos(startpos, maxpos, s.start()+1, len(line))
	   DefaultCurses.stdscr.addstr(sy, sx, word[1:len(word)-1], curses.color_pair(7))
         else:
	   (sy, sx)=self.get_cursor_pos(startpos, maxpos, s.start(), len(line))
	   DefaultCurses.stdscr.addstr(sy, sx, word)
     else:
       pos=-1

 def is_keyword(self, word, level=None, keywords=StringUtil.KEYWORDS):
   if not level:
     for k in keywords:
       if word in k:
         return 1
     return 0
   else:
     return word in keywords[level-1]

 def get_cursor_pos(self, startpos, maxpos, offset, length):
   (y, x)=startpos
   (maxy, maxx)=maxpos
   
   xe=x+length
   ye=y+xe/maxx
   xe=xe%maxx

   x=x+offset
   y=y+x/maxx
   x=x%maxx
    
   while ye>=maxy:
     startpos=(startpos[0]-1, startpos[1])
     ye=ye-1
     y=y-1
   return (y, x)

DefaultGUI.gui=None
DefaultCurses.stdscr=None

try:
  import curses
  import curses.ascii
  curses_enabled=1
except:
  curses_enabled=0

def setup_gui_debugger(eventhandler, debugger, mainloop=1, showhierarchy=1):
  try:
    root=Tk()
  except:
    setup_tui_debugger(eventhandler, debugger)
    return
  DefaultGUI.gui=DefaultGUI(root, eventhandler, debugger, showhierarchy)
  eventhandler.start()
  DefaultGUI.gui.status_str.set(str(eventhandler.state))
  DefaultGUI.gui.update_event_list()
  if mainloop:
    root.mainloop()

def setup_tui_debugger(eventhandler, debugger):
  DefaultGUI.gui=None
  debugger.InterruptEvent('debug')
  lock=ThreadUtil.AllocateLock()
  lock.acquire()
  eventhandler.start(lock)
  lock.acquire()
  lock.release()
  sys.__stdout__.write(str(eventhandler.state)+' > ')
  prompt=strip(sys.__stdin__.readline())
  while prompt!='exit':
    eventhandler.synchronous_event(EventObject(prompt))
    sys.__stdout__.write(str(eventhandler.state)+' > ')
    prompt=strip(sys.__stdin__.readline())
  eventhandler.shutdown()

def setup_cui_debugger(eventhandler, debugger):
  if not curses_enabled:
    setup_tui_debugger(eventhandler, debugger)
  DefaultGUI.gui=None
  DefaultCurses.stdscr=curses.initscr()
  DefaultCurses.stdscr.scrollok(1)
  DefaultCurses.curses=DefaultCurses(eventhandler, debugger)
  curses.echo()
  curses.start_color()
  
  curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)  # default
  curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_WHITE)   # highlight
  curses.init_pair(3, curses.COLOR_RED, curses.COLOR_CYAN)     # snapshot
  curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_WHITE)   # level 1
  curses.init_pair(5, curses.COLOR_RED, curses.COLOR_WHITE)    # level 2
  curses.init_pair(6, curses.COLOR_MAGENTA, curses.COLOR_WHITE)# level 3
  curses.init_pair(7, curses.COLOR_GREEN, curses.COLOR_WHITE)  # string
  
  DefaultCurses.stdscr.bkgd(' ', curses.color_pair(1))
  debugger.InterruptEvent('debug')
  lock=ThreadUtil.AllocateLock()
  lock.acquire()
  eventhandler.start(lock)
  lock.acquire()
  lock.release()
  DefaultCurses.stdscr.addstr(str(eventhandler.state)+' > ', curses.color_pair(2))
  DefaultCurses.stdscr.refresh()
  #prompt=DefaultCurses.stdscr.getstr()
  DefaultCurses.curses.update_event_list()
  prompt=DefaultCurses.curses.curses_get_str()
  lock=ThreadUtil.AllocateLock()
  while prompt!='exit':
    eventhandler.synchronous_event(EventObject(prompt))
    DefaultCurses.stdscr.addstr(str(eventhandler.state)+' > ', curses.color_pair(2))
    DefaultCurses.stdscr.refresh()
    #prompt=DefaultCurses.stdscr.getstr()
    DefaultCurses.curses.update_event_list()
    prompt=DefaultCurses.curses.curses_get_str()
  curses.endwin()

def sortlist(s):
  s.sort()
  return s

def dump_message(s):
  if DefaultGUI.gui:
    DefaultGUI.gui.send_output('%s\n'%s)
  elif DefaultCurses.stdscr:
    DefaultCurses.stdscr.addstr(s+"\n")
    DefaultCurses.stdscr.refresh()
  else:
    print s
