#!/usr/bin/env python3

import sys, os, time, math


def stopwatch():
    sys_time = time.process_time()
    sys_time_mod = sys_time % 60
    sys_time_sec = 60-(60-sys_time_mod)
    sys_time_min = sys_time/60
    
    return print('System Time:', math.floor(sys_time_min), 'min', math.ceil(sys_time_sec), 'sec')

def sysinto():
    info = os.uname()
    return print(info)

