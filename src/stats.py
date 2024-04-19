#!/usr/bin/env python3

import os, time, math
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb
import numpy as np
sb.set_theme()

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
    print("Loop - ", loop_name, " - numbers of loops:", loops, ", time in loop:", "%0.1f" % float(loop_tm),'sec', ", loops per sec:", "%.08f" % float(loop_per_sec))
    return loop_name, loop_tm, loops

def data_chart(kmer_strNum,xs,ys,sloops,name): 
     d = dict()
     d.name(name)
     d.keys(kmer_strNum)
     d.values({'time in loop': xs},{'number of loops': ys},{'loops per sec': sloops})

     df = pd.DataFrame(d)
     print('\n',df.to_markdown,'\n')
     
     

     
     sb.catplot(
     data=df, x="time", y="number of loops", hue="weight",
     native_scale=True, zorder=1
     )
     sb.regplot(
     data=df, x="time", y="number of loops",
     scatter=False, truncate=False, order=2, color=".2",
     )

     
     #File name & save path
     curdir = os.path.dirname(__file__)
     head, tail = os.path.split(curdir)
     plt.savefig(head+'/figures/figSEABORN.png')
     
     
     
num_loops=[]
t=[]
def data_append(time, number_of_loops):
    t.append(time)
    num_loops.append(number_of_loops)
    return t, num_loops
    
    