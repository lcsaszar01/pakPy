#!/usr/bin/env python3

import os, time, math
import matplotlib.pyplot as plt
import pandas as pd

def stopwatch():
    sys_time = time.process_time()
    sys_time_mod = sys_time % 60
    sys_time_sec = 60-(60-sys_time_mod)
    sys_time_min = sys_time/60
    
    return print('System Time:', math.floor(sys_time_min), 'min', math.ceil(sys_time_sec), 'sec')

def sysinto():
    info = os.uname()
    return print(info)

def pid_info():
    iD= os.getpid()
    who = os.getuid
    schedule = os.getpriority(os.PRIO_PROCESS, iD)
    t=time.CLOCK_PROCESS_CPUTIME_ID
    print("\nScheduler:",schedule, "pid:", iD, "Process time:", t)
    
def loop_stat(loops, loop_name):
    loop_tm = time.perf_counter() #in fractional seconds
    loop_per_sec = loops/loop_tm
    print("Loop - ", loop_name, " - numbers of loops:", loops, ", time in loop:", "%0.1f" % float(loop_tm),'sec', ", Loops per sec:", "%.08f" % float(loop_per_sec))
    return loop_name, loop_tm, loops

def data_chart(xs,ys,name): 
     d = dict()
     d.update({'time': xs})
     d.update({'number of loops': ys})
     df = pd.DataFrame(d)
     df.plot(kind='line',x='time',y='number of loops',color='blue')
     n = 'Line Graph of time vs. loops'+''+name
     plt.title(n)
     curdir = os.path.dirname(__file__)
     head, tail = os.path.split(curdir)
     plt.savefig(head+'/figures/fig1.png')
     
     
     
num_loops=[]
t=[]
def data_append(time, number_of_loops):
    t.append(time)
    num_loops.append(number_of_loops)
    return t, num_loops
    
    