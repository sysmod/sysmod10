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


import time
import pygame
import thread
import ThreadUtil

#======================================================================#
# CD hardware class

class CDHardware:

 def __init__(self, eventhandler, CDRomNumber=0):
   self.eject_received=0
   self.init_received=0
   self.play_received=0
   self.stop_received=0
   self.pause_received=0
   self.resume_received=0
   self.next_received=0
   self.restart_received=0
   self.forward_received=None
   self.change_cdrom=-1
   self.playing=0
   self.CD=0
   self.cd_count=0
   self.eventhandler=eventhandler
   self.CDRomNumber=CDRomNumber
   self.TrackSel=0
   self.HWS={}
   ThreadUtil.StartThread(self.ThreadCheckEvent, ())

 def FormatTime(self, time):
   t=int(time)
   t1=t/60
   t2=t-t1*60
   s1=str(t1)
   if len(s1)<2:
     s1='0'+s1
   s2=str(t2)
   if len(s2)<2:
     s2='0'+s2
   return s1+':'+s2

 def CheckHardwareState(self):
   if not self.CD.get_empty():
     gc=self.CD.get_current()
     trlen=self.CD.get_track_length(gc[0])
   else:
     gc=[0,0]
     trlen=0
   self.HWS={ 'CDRom_Empty' : self.CD.get_empty(),
              'CDRom_Name' : self.CD.get_name(),
              'Track_Number' : self.CD.get_numtracks(),
              'Current_TrackNumber' : gc[0],
              'Current_TrackLength' : trlen,
              'Current_ElapsedTime' : gc[1],
              'CD_Playing' : self.CD.get_busy(),
              'CD_Paused' : self.CD.get_paused(),
              'CD_Stopped' : not (self.CD.get_busy() or self.CD.get_paused()) }
   if self.HWS['CDRom_Empty']:
     self.HWS['Current_TrackNumber']=0
   
 def ThreadCheckEvent(self):

   while 1:

     if (self.init_received):
       self.init_received=0
       pygame.init()
       self.cd_count=pygame.cdrom.get_count()
       self.CD=pygame.cdrom.CD(self.CDRomNumber)
       self.CD.init()
       
       if self.HWS.has_key('CD_Playing') and self.HWS.has_key('CD_Paused') and self.HWS.has_key('CD_Stopped'):
         if not self.HWS['CD_Stopped']:
           self.CD.play(self.HWS['Current_TrackNumber'], self.HWS['Current_ElapsedTime'])
         if self.HWS['CD_Paused']:
           self.CD.pause()
       else:
         self.CheckHardwareState()
       # When hardware is ready, it raises an init_display event
       self.eventhandler.event('Hardware Initiated')
       if self.HWS['CD_Playing']:
         self.TrackSel=self.HWS['Current_TrackNumber']
         self.eventhandler.event('Hardware Played')
     
     if (self.change_cdrom>=0):
       self.eventhandler.event('Hardware Eject')
       self.CDRomNumber=self.change_cdrom
       self.change_cdrom=-1
       self.CD.stop()
       self.CD.quit()
       self.CD=pygame.cdrom.CD(self.CDRomNumber)
       self.CD.init()
       self.CheckHardwareState()
       if not self.HWS['CDRom_Empty']:
         self.eventhandler.event('Hardware Insert')
         if self.HWS['CD_Playing']:
           self.TrackSel=self.HWS['Current_TrackNumber']
           self.eventhandler.event('Hardware Played')

     time.sleep(0.1)

     if (self.CD==0):
       continue

     if (self.eject_received):
       self.CD.eject()
       self.eject_received=0
       self.playing=0
     
     if (self.play_received):
       self.CD.play(self.TrackSel, self.HWS['Current_ElapsedTime'])
       self.play_received=0
       self.playing=1
       self.forward_received=None
     
     if (self.restart_received):
       self.CD.play(self.HWS['Current_TrackNumber'])
       self.restart_received=0
       self.playing=1

     if (self.pause_received):
       self.CD.resume()
       self.CD.pause()
       self.pause_received=0
       self.playing=0
       self.eventhandler.event('Hardware Paused')

     if (self.resume_received):
       self.CD.resume()
       if (self.HWS['Current_TrackNumber']!=self.CD.get_current()[0]
           or self.HWS['Current_ElapsedTime']!=self.CD.get_current()[1]):
         self.CD.stop()
         ti=self.HWS['Current_ElapsedTime']
         tr=self.TrackSel
         self.forward_received=None
         self.CD.play(tr, ti)
       elif (self.HWS['Current_TrackNumber'])!=self.TrackSel:
         self.CD.play(self.TrackSel)
       self.resume_received=0
       self.playing=1
       self.eventhandler.event('Hardware Resumed')
     
     if (self.next_received):
       self.HWS['Current_ElapsedTime']=0
       self.forward_received=None
       if self.playing:
         self.CD.play(self.TrackSel)
       elif self.CD.get_paused():
         self.CD.resume()
         self.CD.play(self.TrackSel)
         self.CD.pause()
       self.next_received=0

     if (self.stop_received):
       self.stop_received=0
       self.playing=0
       self.forward_received=None
       if self.CD.get_paused():
         self.CD.resume()
         self.CD.stop()
         self.HWS['CD_Stopped']=0	# Just to force the hardware event 'Hardware Stopped' to be raised
       elif self.CD.get_busy():
         self.CD.stop()

     if (self.forward_received!=None):
       et=self.HWS['Current_ElapsedTime']+self.forward_received-self.lastforward
       self.lastforward=self.forward_received
       tr=self.TrackSel
       trlen=self.CD.get_track_length(tr)
       while et>=trlen:
         et=et-trlen
         tr=tr+1
         if tr>self.CD.get_numtracks()-1:
           tr=tr-1
           et=trlen-1
           break;
         trlen=self.CD.get_track_length(tr)
         self.TrackSel=self.TrackSel+1
       while et<0:
         tr=tr-1
         if tr<0:
           tr=0
           et=0
           break;
         et=et+self.CD.get_track_length(tr)
         self.TrackSel=self.TrackSel-1
       self.HWS['Current_ElapsedTime']=et
       self.HWS['Current_TrackNumber']=tr
       self.HWS['Current_TrackLength']=self.CD.get_track_length(tr)

     OldHWS=self.HWS;
     if self.forward_received==None:
       self.CheckHardwareState();

     # Update Display event is raised whenever the time or track is changed
     if (self.HWS['Current_ElapsedTime']!=OldHWS['Current_ElapsedTime'] or
         self.HWS['Current_TrackNumber']!=OldHWS['Current_TrackNumber']):
       self.eventhandler.event('Update Display')

     # Hardware Eject event is raised whenever a CD is ejected
     if (not OldHWS['CDRom_Empty'] and self.HWS['CDRom_Empty']):
       self.playing=0
       self.eventhandler.event('Hardware Eject')

     # Hardware Insert event is raised whenever a CD is inserted
     if (OldHWS['CDRom_Empty'] and not self.HWS['CDRom_Empty']):
       self.eventhandler.event('Hardware Insert')

     if (not OldHWS['CD_Playing'] and self.HWS['CD_Playing']):
       self.eventhandler.event('Hardware Played')

     if (not OldHWS['CD_Stopped'] and self.HWS['CD_Stopped']):
       self.eventhandler.event('Hardware Stopped')	# When the CD player is successfully stopped, the hardware sends back a event

# Hardware state checking functions
 
 def RawElapsedTime(self):
   if self.HWS['Current_TrackNumber']!=self.TrackSel:
     return 0
   else:
     return self.HWS['Current_ElapsedTime']

 def ElapsedTime(self):
   return self.FormatTime(self.RawElapsedTime())
 
 def TrackNumber(self):
   return self.TrackSel+1
 
 def CDCount(self):
   return self.cd_count
 
 def CDNumber(self):
   return self.CDRomNumber
 
 def IsEmpty(self):
   return self.HWS['CDRom_Empty']
 
 def TrackCount(self):
   return self.HWS['Track_Number']
 
 def TrackLength(self):
   return self.HWS['Current_TrackLength']
 
 def IsStopped(self):
   return self.HWS['CD_Stopped']
   
 # CD controlling commands are listed below.
 # Note that no command can be directly sent to the CDRom,
 # because there is always a thread running behind this one checking the state of CDRom periodically.
 # If commands are not redirected to the background thread,
 # the CDRom hardware may be confused by two instructions sent to it at the same time.
 # So, corresponding flags are set and appropriate commands are committed in the background thread.

 def InitiateHardware(self):
   self.init_received=1

 def Eject(self):
   self.eject_received=1
 
 def Play(self):
   self.play_received=1
 
 def Stop(self):
   self.stop_received=1

 def Pause(self):
   self.pause_received=1

 def Resume(self):
   self.resume_received=1
 
 def Next(self):
   self.next_received=1
   self.TrackSel=self.TrackSel+1
 
 def First(self):
   self.next_received=1
   self.TrackSel=0
   self.HWS['Current_ElapsedTime']=0
 
 def Previous(self):
   self.next_received=1
   self.TrackSel=self.TrackSel-1
 
 def Restart(self):
   self.restart_received=1
 
 def Forward(self, sec):
   if self.forward_received==None:
     self.lastforward=0
     self.forward_received=0
   self.forward_received=self.forward_received+sec
 
 def HardStop(self):
   self.CD.stop()
 
 def ChangeCDRom(self, cdrom):
   if cdrom<self.cd_count:
     self.TrackSel=0
     self.forward_received=None
     self.change_cdrom=cdrom
