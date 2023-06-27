#!/usr/bin/env python3

import math as m
import time

def wire(cnt_lst):
    sc=0
    pc=0
    
    suf_dict = []
    pre_dict = []
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
    suffix = []
    prefix = []
    temp = []
    
    #parses the list to get the visit count values, splits by affix value
    for item in cnt_lst:
        subitem = item[1]
        if subitem[0] =='Prefix':
            val = subitem[2]
            prefix.append(val[1])
        elif subitem[0] == 'Suffix':
            suffix.append(val[1])
            
    #calculate the sum of all the prefix visit counts of the node       
    suffix_node = suffix
    for i in suffix_node:  
        sc = sc+i
    print("Total Number of Suffix Visits:", sc) #returns the value

    #calculate the sum of all the prefix visit counts of the node
    prefix_node = prefix
    for p in prefix_node: 
        pc = pc+p
    print("Total Number of Prefix Visits:",pc) #returns the value
    

    for nu in suffix_node: #initialize and assign value to the null suffix
        if(len(str(nu))==0):
            null_sid = nu
            temp.append(1)
            temp.append(pc-sc)
            suf_dict.append(temp.copy())
            temp.clear()
        
    for nu2 in prefix_node: #initialize and assign value to the null prefix
        if(len(str(nu2))==0):
            null_pid = nu2
            temp.append(1)
            temp.append(sc-pc)
            pre_dict.append(temp.copy())
            temp.clear()
    leftovers = sc+suffix_node[null_sid]
    '''EVERYTHING WORKS UP TO HERE!!!'''
    
    #Initialie an array to maintain the offsets within each suffix edge
    while(leftovers > 0):
        
        for y in prefix_node: #This loop does the actual sumation of the values
            
            valstr = y
            val_lst.append(valstr)
            if(number < valstr): 
                number = valstr
            i += 1
          
        largest_pid = number
      
        val_lst.clear()
        
        for y in prefix_node: #This loop does the actual sumation of the values
            valstr = y
            val_lst.append(valstr)
            if(number2 < int(valstr)): 
                number2 = int(valstr)
            i2 += 1
        
        largest_sid = number2

        for i in range(largest_sid):
            offset_in_suffix.append(0)

        offset_in_suffix.append(number2)
        val_lst.clear()
        #print(largest_pid,largest_sid)
        counter = min(largest_pid,largest_sid)
        #print("COUNTER",counter)
        temp2 = []
        temp2.append(largest_sid)
        temp2.append(offset_in_suffix[largest_sid])
        temp2.append(counter)
        
        pid.append(temp2)
        temp2.clear()
        loop_count +=1
        
        leftovers -= counter
        
        update = offset_in_suffix[largest_sid] + counter
        offset_in_suffix.remove(largest_pid)
        offset_in_suffix.append(update) 
        if loop_count != i:
            break
    for d in range(len(pid)):
        wireinfo.insert(d,pid[d])
    print("The Wiring is done")
    return wireinfo
