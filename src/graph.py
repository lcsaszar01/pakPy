#!/usr/bin/env python3
'''
An attempt to create a structure and class for the graphs 
Inspired by the class tutorials at https://stackoverflow.com/questions/40898482/defining-method-of-class-in-if-statement
'''
import os
import math as m
import wire as w 
import u as u
import draw_graph as dg
import time

def graph_maker(kmer_list):
    print("Setting up graph")
    coverage = 100 #assuming 100 for the fake_dna sample that chatGPT created
    dict_str = () #takes a string from a dictonary value

    #A bunch of value initializations.
    prefix_dict = {}
    suffix_dict = {}
    found_countA = 0
    found_countB = 0
    vertex_count = 0
    vertex_count2= 0    
    counter_for_find = 0
    counter_for_find2 = 0
    enum = enumerate(kmer_list) #count the number of strings in the list to prep it for dictionary conversion

    kmer_dict = dict((x,y) for x,y in enum) #creating dictionary

    #send to a dictonary instead of a tuple because a tuple is immutable. 
    lmer1 = [] 
    lmer2 = []
    count = 0
    alpha = ('A','T','C','G') #The Alphabet of Amino Acid polymers
    
    for i in range(len(kmer_dict)):
        kmer_str = kmer_dict[i]
        flag=True
        while(flag!=False):  #splits total string of dna bases of the best kmer size between 32 and 42
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
        for x in range(0,len(lmer1)): #In theory these should be the same length of k_size
            lmerA+=lmer1[x] 
            lmerB+=lmer2[x]
        
        lmer1.clear()
        lmer2.clear()
        
        affix = u.u('prefix')#Initialize the data structure for the prefix type in the class 
        for d in range(len(kmer_dict)-1): #FIND EDGES FOR PREFIX
            found_countA = 0
            for a in alpha:
                dict_str = kmer_dict.get(d)
                
                temp_lmer = a+lmerB
                
                #see if the string exits in the dict
                
                for x in range(len(kmer_dict)):
                    if(kmer_list[x] == temp_lmer):
                        counter_for_find += 1
                           
                #print("found count:", counter_for_find)
                #print("Letter:", a)
                #print("new kmer", temp_lmer)
                
                
                #If the string exists in the dictionary
                u.u.label(lmerB)
                u.u.prefixes.append(a) #appended the prefix letter to the prefixes list
                #Gives us the number of vertices that the string should have
                vertex_count = m.ceil(counter_for_find/coverage)
                app = {counter_for_find:vertex_count}
                prefix_dict.update(app)
                logic = vertex_count==1
                temp=[]
                temp = app.copy()
                
                if(logic is True): #Marks a terminal node if edge is 1
                    affix.prefix_info(temp, 1)    
                else:
                    affix.prefix_info(temp, 0)                        
                counter_for_find = 0
            found_countA = 0
        lmerB=''
    
        
        affix2 = u.u('suffix') #Initialize the data structure for the suffix type in the class
        for d2 in range(len(kmer_dict)-1): #FIND EDGES FOR SUFFIX
            for a2 in alpha:
                dict_str2 = kmer_dict.get(d2)
                temp_lmer2 = lmerA+a2
                
                #see if the string exits in the dict
                for x in range(len(kmer_dict)):
                    if(kmer_list[x] == temp_lmer):
                        counter_for_find2 += 1
                           
                #print("found count:", counter_for_find2)
                #print("Letter:", a)
                #print("new kmer", temp_lmer)
                   
                #If the string exits in the dictionary
                u.u.label(lmerA)
                u.u.suffixes.append(a2) #appends the letter which makes the string match to the list
                #Gives us the number of vertices that the string should have
                vertex_count2 = m.ceil(counter_for_find2/coverage)          
                app2 = {counter_for_find2:vertex_count2}
                suffix_dict.update(app2)
                logic2 = vertex_count2==1
                temp2=[]
                temp2 = app2.copy()
        
                if(logic2 is True): #Marks a terminal node if edge is 1
                    affix2.suffix_info(temp2, 1)
                else:
                    affix2.suffix_info(temp2, 0)  
                counter_for_find2 = 0
        lmerA=''  
    print("sending to wire...")    
    wire_info = w.wire(str(u.u.count), str(u.u.count2))
    u.u.wire_info.append(wire_info)
    dg.draw()
    
    return 
curdir = os.path.dirname(__file__)
head, tail = os.path.split(curdir)
fd = open(head+"/kmers/dna_kmer_21455.txt", "r")
val_str = fd.readline()
fd.close()
val_lst = []

val_str = val_str.replace("[",'')
val_str = val_str.replace("]",'')
val_str = val_str.replace("'",'')
val_lst = val_str.split(', ')
print(val_str)
print(val_lst)

graph_maker(val_lst)
