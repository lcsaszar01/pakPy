#!/usr/bin/env python3

import math as m

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
    null_sid =-1
    null_pid=-1
    largest_pid = 0
    pid = []    
    val_lst = []
    i = 0
    i2 = 0
    number = 0
    number2 = 0
    wireinfo = []
    loop_count = 0
    
    #prefrocessing the values into strings

    pre_str = prefix[1:-1]
    suf_str = suffix[1:-1]
    
    for i in pre_str:
        pre_str = pre_str.replace("}",'')
        pre_str = pre_str.replace("{",'')
    for i in suf_str:
        suf_str = suf_str.replace("{",'')
        suf_str = suf_str.replace("}",'')
        
    prefix_node = list(pre_str.split(','))
    suffix_node = list(suf_str.split(','))

    #calculate the sum of all suffix visit counts of node
    for i in range(len(suffix_node)): 
        str = suffix_node[i]
        str = str.replace("'","")
        str = (str.split(':'))
        
        for e in str:
            str_lst.append(e)
     
        t = {str_lst[0]:str_lst[-1]}
        numb_lst.append(str_lst[-1])
        let_lst.append(str_lst[0])
        str_lst.clear()
        
        suf_dict.update(t) #The code traverses the data set to strip the data string down to append it to a dict before summing the values for each key

    for y in suf_dict.keys(): #This loop does the actual sumation of the values
        val = suf_dict.get(y)
        sc = sc+int(val)
    print("Total Number of Suffix Visits:", sc) #returns the value
    
    #calcue the sum of all the prefix visit counts of the node
    for p in range(len(prefix_node)): 
        str = prefix_node[p]
        str = str.replace("'","")
        str = (str.split(':'))
        
        for e in str:
            str_lst.append(e)
     
        t = {str_lst[0]:str_lst[-1]}
        numb_lst.append(str_lst[-1])
        let_lst.append(str_lst[0])
        str_lst.clear()
        
        pre_dict.update(t) #The code traverses the data set to srip the data string down to append it to a dict before summing the values for each key

    for t in pre_dict.keys(): #This loop does the actual sumation of the values
        val = pre_dict.get(t)
        pc = pc+int(val)
    print("Total Number of Prefix Visits:",pc) #returns the value
    
    for nu in range(len(prefix_node)): #initialize and assign value to the null suffix
        if(len(suffix_node[nu])==0):
            null_sid = 1
            suf_dict.update({1:(pc-sc)})
    
    leftovers = sc+null_sid
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

'''     CALLING THE FUNCTION FOR TESTING  
def run():
    
    import os
    curdir = os.path.dirname(__file__)

    path = os.path.join(curdir+"/fasta_files/gd_prefix.txt")
    fd = open(path, 'r')
    pre_str = fd.read()
    fd.close()
    path2 = os.path.join(curdir+"/fasta_files/gd_suffix.txt")
    fd = open(path2, 'r')
    suf_str = fd.read()
    
    wire(pre_str,suf_str)
    
run()'''