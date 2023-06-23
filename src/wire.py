#!/usr/bin/env python3

import math as m
import time
import sys
sys.dont_write_bytecode = True
def wire(prefix, suffix):
    sc=0
    pc=0
    str = ''
    suf_dict = {}
    pre_dict = {}
    str_lst =[]
    numb_lst = []
    let_lst = []
    leftovers = 0
    offset_in_suffix = []
    null_sid = -1
    null_pid = -1
    largest_pid = 0
    pid = []    
    val_lst = []
    i = 0
    i2 = 0
    number = 0
    number2 = 0
    wireinfo = []
    loop_count = 0
    
    suffix_node = suffix
    for i in range(len(suffix_node)): 
        sc = sc+int(i)
    print("Total Number of Suffix Visits:", sc) #returns the value
    
    #calculate the sum of all the prefix visit counts of the node
    prefix_node = prefix
    for p in range(len(prefix_node)): 
        pc = pc+int(p)
    print("Total Number of Prefix Visits:",pc) #returns the value
    
    for nu in range(len(suffix_node)): #initialize and assign value to the null suffix
        #print("node:", suffix_node[nu],"len:",len(suffix_node[nu]))
        
        if(len(suffix_node[nu])==0):
            null_sid = nu
            suf_dict.update({1:(pc-sc)})

   
    for nu2 in range(len(prefix_node)): #initialize and assign value to the null prefix
        if(len(prefix_node[nu2])==0):
            null_pid = nu2
            pre_dict.update({1:(sc-pc)})
    
    leftovers = sc+null_sid
    
    #tests

    #Initialie an array to maintain the offsets within each suffix edge

    while(leftovers > 0):
        
        for y in pre_dict.keys(): #This loop does the actual sumation of the values
            valstr = pre_dict.get(y)
            valstr =valstr.strip(" ")
            val_lst.append(valstr)
            
            if(number < int(valstr)): 
                number = int(valstr)
            i += 1
        largest_pid = number
        val_lst.clear()
 
        for y in suf_dict.keys(): #This loop does the actual sumation of the values
            valstr = suf_dict.get(y)
            valstr =valstr.strip(" ")
            val_lst.append(valstr)
            
            if(number2 < int(valstr)): 
                number2 = int(valstr)
            i2 += 1
        
        largest_sid = number2
        for i in range(largest_sid):
            offset_in_suffix.append(0)
        
        offset_in_suffix.append(number2)
        val_lst.clear()
        
        counter = min(largest_pid,largest_sid)
       
        temp=[]
        
        temp.append(largest_sid)
        temp.append(offset_in_suffix[largest_sid])
        temp.append(counter)
        
        pid.append(temp)
        loop_count +=1
        
        leftovers -= counter
        
        update = offset_in_suffix[largest_sid] + counter
        offset_in_suffix.remove(largest_pid)
        offset_in_suffix.append(update) 
        
    for d in range(len(pid)):
        wireinfo.insert(d,pid[d])
    print("The Wiring is done")
    return offset_in_suffix
