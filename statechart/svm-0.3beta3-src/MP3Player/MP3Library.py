#
# MP3Library.py
#
# Class MP3Handle provides a wrapper around the
# details of accessing MP3 files as well as the audio device.
# Note how access to the audio device is implicit: 
# mp3.play() plays the current MP3 file and audio is produced.
# 
# This wrapper can generate the following (hardware) events
# to be handled (update state, send messages to the GUI) by the Statechart:
#  "Playing Started"
#  "Playing Stopped"
#  "Time Advance"
#  "Hardware Quit"
#
# From the Statechart, the modeller may access
# the wrapper's methods, to query or to control the devices.
#  Query: get_time
#  Control: load, play, pause, stop, resume, forward, rewind
# All of the above have the obvious meaning. resume() resumes
# playing after playing has been paused.
#

import pygame
from pygame.movie import Movie
from thread import *
from threading import Condition
from time import *

class MP3Handler:

  def __init__(self, eventhandler):
    self.bgthread = None
    self.bglock = allocate()
    self.lastbusy = 0
    self.time = 0
    self.loadfile = None
    self.loadcond = Condition()
    self.mp3 = None
    self.paused = 0
    self.eventhandler = eventhandler

  def start_bgthread(self):
    self.bgthread = 1
    self.bgthread = start_new_thread(self.bgthread_proc, ())

  def is_bgthread_stopped(self):
    self.bglock.acquire()
    stopped = (self.bgthread == None)
    self.bglock.release()
    return stopped

  def bgthread_proc(self):
    while (not self.is_bgthread_stopped()):
      sleep(0.1)
      self.bglock.acquire()
      self.loadcond.acquire()
      if self.loadfile:
        if self.mp3:
          del self.mp3
        self.mp3 = Movie(self.loadfile)
        self.set_time(0)
        self.loadfile = None
        self.loadcond.notify()
      self.loadcond.release()
      if self.paused:
	self.bglock.release()
	continue
      is_busy = self.is_busy()
      if is_busy:
        t = self.get_time()+0.1
        self.set_time(t)
        if not self.lastbusy:
          self.eventhandler.event("Playing Started")
        self.eventhandler.event("Time Advance")
      else:
        if self.lastbusy:
	  self.set_time(0)
          self.eventhandler.event("Playing Stopped")
      self.lastbusy = is_busy
      self.bglock.release()
    self.eventhandler.event("Hardware Quit")

  def stop_bgthread(self):
    self.bglock.acquire()
    self.bgthread = None
    self.bglock.release()

  def set_time(self, t):
    if t<0:
      t = 0
    elif self.mp3 and t>self.mp3.get_length():
      t = self.mp3.get_length()
    self.time = t

  def get_time(self):
    t = self.time
    return t

  def load(self, mp3file):
    self.bglock.acquire()
    self.loadcond.acquire()
    self.bglock.release()
    self.loadfile = mp3file
    # wait for the background thread to load the MP3 file
    self.loadcond.wait()
    self.loadcond.release()

  def play(self):
    self.bglock.acquire()
    if self.mp3:
      self.mp3.play()
      self.set_time(0)
    self.bglock.release()

  def stop(self):
    self.bglock.acquire()
    if self.mp3:
      if self.paused:
        self.paused = 0
        self.lastbusy = 1
      self.mp3.stop()
    self.bglock.release()

  def rewind(self):
    self.bglock.acquire()
    if self.mp3:
      self.mp3.rewind()
      self.set_time(0)
    self.bglock.release()

  def forward(self, n_sec):
    self.bglock.acquire()
    self.set_time(self.get_time()+n_sec)
    self.bglock.release()

  def backward(self, n_sec):
    self.bglock.acquire()
    self.set_time(self.get_time()-n_sec)
    self.bglock.release()

  def pause(self):
    self.bglock.acquire()
    if self.mp3:
      if self.is_busy():
        self.mp3.pause()
        self.last_pause_time=self.get_time()
        self.paused = 1
        self.lastbusy = 0
    self.bglock.release()

  def resume(self):
    self.bglock.acquire()
    if self.mp3:
      if not self.is_busy() and self.paused:
        self.lastbusy = 0
        if self.get_time()!=self.last_pause_time:
          self.mp3.stop()
          self.mp3.rewind()
          self.mp3.skip(self.get_time())
          self.mp3.play()
        else:
          self.mp3.pause()
        self.paused=0
    self.bglock.release()

  def is_busy(self):
    return self.mp3 and self.mp3.get_busy()
