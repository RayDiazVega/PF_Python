import os
import time
import threading
import multiprocessing

NUM_WORKERS = 4

def only_sleep():
    #Do nothing, wait for a timer to expire
    print("PID: %s, Process Name: %s, Thread Name: %s" % (
        os.getpid(),
        multiprocessing.current_process().name,
        threading.current_thread().name))
    time.sleep(1)
 
def crunch_numbers():
    #Do some computations
    print("PID: %s, Process Name: %s, Thread Name: %s" % (
        os.getpid(),
        multiprocessing.current_process().name,
        threading.current_thread().name))
    x = 0
    while x < 10000000: x += 1

for f in [only_sleep,crunch_numbers]:
  print("\nTesting the funtion:",f.__name__)
  # Run tasks serially
  start_time = time.time()
  for _ in range(NUM_WORKERS): f()
  print("Serial time=", time.time() - start_time)
  
  # Run tasks using threads
  start_time = time.time()
  threads = [threading.Thread(target=f) for _ in range(NUM_WORKERS)]
  for thread in threads: thread.start()
  for thread in threads: thread.join()
  print("Parallel time=", time.time() - start_time)
  
  # Run tasks using processes
  start_time = time.time()
  processes = [multiprocessing.Process(target=f) for _ in range(NUM_WORKERS)]
  for process in processes: process.start()
  for process in processes: process.join()
  print("Concurrent time=", time.time() - start_time)
