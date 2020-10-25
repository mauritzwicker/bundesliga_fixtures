#this is to practice the threading, used for looping through the games

import threading
import time

def function_do():
    print('in function')
    time.sleep(1)


#create thread objects
thread_1 = threading.Thread(target=function_do)
thread_2 = threading.Thread(target=function_do)

#to start the thread
thread_1.start()
thread_2.start()

#to join them to the man script (i.e let the main script only continue when all threads done)
thread_1.join()
thread_2.join()


#initialize list of threads
threads = []

#for threading in a loop (10 times)
for _ in range(10):
    t = threading.Thread(target=function_do)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

print('DOne ALL')




#if we want to do a statement with arguments we use threading.Thread(target = function, args = [arguments, ...])

