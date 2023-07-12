#!/usr/bin/env python3

'''This func gives a number increment'''

cnt = []
cnt2 = []
nameCnt = []
count = 0
loopCnt = []
def globe_count():
    count = 1
    cnt.append(count)
    return len(cnt) 

def count_clear():
    cnt.clear()
    
def globe_count2():
    count = 1
    cnt2.append(count)
    return len(cnt2)

def nameCount():
    count = 1
    nameCnt.append(count)
    return len(nameCnt)

def loop_count():
    count = 1
    loopCnt.append(count)

        
def loop_total():
    n = len(loopCnt)
    return n
    
def clear():
    loopCnt.clear()
      