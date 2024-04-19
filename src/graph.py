#!/usr/bin/env python3
'''
An attempt to create a structure and class for the graphs 
Inspired by the class tutorials at https://stackoverflow.com/questions/40898482/defining-method-of-class-in-if-statement
'''
import os
import math as m
import wire as w 
import u as u
import stats as stats


def graph_maker(kmer_list):
    print("Setting up graph")
    coverage = 0.000215 #There is 928,320 DNA fragments in the ecoli.fasta file. The percent value of 1 string is the coverage value
    dict_str = () #takes a string from a dictonary value

    #A bunch of value initializations.
    num = 1
    lst = []
    visit_count = 0
    visit_count2= 0    
    counter_for_find = 0
    counter_for_find2 = 0
    enum = enumerate(kmer_list) #count the number of strings in the list to prep it for dictionary conversion

    kmer_dict = dict((x,y) for x,y in enum) #creating dictionary

    #send to a dictonary instead of a tuple because a tuple is immutable. 
    lmer1 = [] 
    lmer2 = []
    count = 0
    alpha = ('A','T','C','G') #The Alphabet of Amino Acid polymers
    counts=0
    
    for i in range(len(kmer_dict)):
        counts +=1
       
        kmer_str = kmer_dict[i]
        flag=True
        
        while(flag!=False):  #splits the kmer into a kmer-1, creating the string for if the suffix and if the prefix was removed.  
            count +=1
            if(count == 1):
                kmer_list_temp = list(kmer_str)      
                for j in range(0, len(kmer_list_temp)-1):
                    lmer1 += kmer_list_temp[j]      
            elif(count == 2):
                kmer_list_temp = list(kmer_str)   
                for j in range(1,len(kmer_list_temp)):
                    lmer2 += kmer_list_temp[j]
            else: 
                count -= 3
                flag=False

        lmerA = ''
        lmerB = ''
        for x in range(0,len(lmer1)): #In theory these should be the same length of k_size, load the values into strings. 
            lmerA+=lmer1[x] 
            lmerB+=lmer2[x]
        
        lmer1.clear()
        lmer2.clear()
        
        #LOOKS AT PREFIXES
        for a in alpha: #for the letter from our prefix alphabet
            count += 1
            
            temp_lmer = a+lmerB #creates the kmer-1 of the prefix letter
            
            #see if the string has a match in the dict
            for x in range(len(kmer_dict)):
                if(kmer_list[x] == temp_lmer):
                    counter_for_find += 1

                    kmers = len(kmer_dict)
                    if x == kmers or x==0:
                        term = 1
 
            if(counter_for_find > 0): 
         
                visit_count = m.ceil(counter_for_find/coverage)#Gives us the number of vertices that the string should have
                lst.append(counter_for_find) 
                lst.append(visit_count)
                
                if term==1:
                    u.macro_node.createNodes(lmerB, 'Prefix', a, lst.copy(), 1)
                else:
                    u.macro_node.createNodes(lmerB, 'Prefix', a, lst.copy(), 0) 
                    
            lst.clear()                 
            counter_for_find = 0
            
        
        lmerB=''
        
        
        #LOOKS AT SUFFIXES
        
        for a2 in alpha:
            count+=1
            
            temp_lmer = lmerA+a2
            #see if the string exits in the dict
            for x in range(len(kmer_dict)):
                if(kmer_list[x] == temp_lmer):
                    counter_for_find2 += 1
                    
                    kmers = len(kmer_dict)
                    if x == kmers or x==0:
                        term = 1
            
            if(counter_for_find2 > 0): 
                visit_count2 = m.ceil(counter_for_find2/coverage) #Gives us the number of vertices that the string should have  
                lst.append(counter_for_find2)
                lst.append(visit_count2)
                    
                if term == 1:
                    u.macro_node.createNodes(lmerA, 'Suffix', a2, lst.copy(), 1)
                else:
                    u.macro_node.createNodes(lmerA, 'Suffix', a2, lst.copy(), 0)
            lst.clear()
            counter_for_find2 = 0 #clears the count for the next letter 
              
        lmerA=''  #clears the lmer string
    lname, tm, lps = stats.loop_stat(counts, "graph values break down")    
    t, l =stats.data_append(tm, lps)
    num = num+1
    stats.data_chart(t,l,lname,t/l,"loop"+num.string())
    #saves a copy of the values found for analysis and debugging
    
    
    print("sending to wire...")
    wire_info = w.wire(u.macro_node.lmers_and_attrs)
    u.macro_node.wire_info.extend(wire_info)
    u.macro_node.updateNode(wire_info)
    
    
    curdir = os.path.dirname(__file__)
    head, tail = os.path.split(curdir)

    fd = open(head+"/dict/dictonary.txt", "w+")
   
    fd.write(str(u.macro_node.lmers_and_attrs))
    
    fd.close()
    
    return u.macro_node.lmers_and_attrs 
