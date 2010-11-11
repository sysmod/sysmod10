import thread
import time

lock=thread.allocate()

def start_thread(func, params):
  lock.acquire()
  thread.start_new_thread(thread_wrapper, (func, params))

def thread_wrapper(func, params):
  lock.release()
  apply(func, params)

def mythread(id):
  print 'id = %d'%id
  time.sleep(1)

for i in range(100):
  start_thread(mythread, (i,))

print 'Success!'
