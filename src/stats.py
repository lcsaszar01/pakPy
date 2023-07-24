#!/usr/bin/env python3

import os, time, math

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

    
    