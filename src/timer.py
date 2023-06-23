#!/usr/bin/env python3

import time
import sys
sys.dont_write_bytecode = True

def start():
    return time.process_time_ns()
    
def stop():
    return time.process_time_ns()

def stopwatch():
    lap_time = stop()-start()
    return print("lapsed time", lap_time)