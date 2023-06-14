#!/usr/bin/env python3

import time

def start():
    return time.process_time_ns()
    
def stop():
    return time.process_time_ns()

def stopwatch():
    lap_time = stop()-start()
    return print("lapsed time", lap_time)