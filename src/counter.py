#!/usr/bin/env python3

'''This func gives a number increment'''

def globe_count():
    count = 1
    global cnt 
    cnt.append(count)
    return len(cnt) 

def count_clear():
    cnt.clear()