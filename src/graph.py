#!/usr/bin/env python3
'''
An attempt to create a structure and class for the graphs 
Inspired by the class tutorials at https://stackoverflow.com/questions/40898482/defining-method-of-class-in-if-statement
'''

import math as m
import wire as w 
import u as u
import draw_graph as dg


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
            for a in alpha:
                dict_str = kmer_dict.get(d)
                temp_lmer = a+lmerB
                comp = dict_str == temp_lmer
                u.u.label(temp_lmer)
                #If the string exists in the dictionary
                if(comp == True):
                    found_countA += 1
                    u.u.prefixes.append(a) 
                    #Gives us the number of vertices that the string should have
                    vertex_count = m.ceil(found_countA/coverage)
                    app = {found_countA:vertex_count}
                    prefix_dict.update(app)
                    logic = vertex_count==1
                    temp=[]
                    temp = app.copy()
            
                    if(logic is True): #Marks a terminal node if edge is 1
                        affix.prefix_info(temp, 1)    
                    else:
                        affix.prefix_info(temp, 0)
        lmerB=''
                 
        affix2 = u.u('suffix') #Initialize the data structure for the suffix type in the class
        for d2 in range(len(kmer_dict)-1): #FIND EDGES FOR SUFFIX
            for a2 in alpha:
                dict_str2 = kmer_dict.get(d2)
                temp_lmer2 = lmerA+a2
                u.u.label(temp_lmer2)
                if(dict_str2 == temp_lmer2):
                    found_countB += 1
                    u.u.suffixes.append(a2) #appends the letter which makes the string match to the list
                    #Gives us the number of vertices that the string should have
                    vertex_count2 = m.ceil(found_countB/coverage)          
                    app2 = {found_countB:vertex_count2}
                    suffix_dict.update(app2)
                    logic2 = vertex_count2==1
                    temp2=[]
                    temp2 = app2.copy()
            
                    if(logic2 is True): #Marks a terminal node if edge is 1
                        affix2.suffix_info(temp2, 1)
                    else:
                        affix2.suffix_info(temp2, 0)             
        lmerA=''  
        
    wire_info = w.wire(str(u.u.count), str(u.u.count2))
    u.u.wire_info.append(wire_info)
    dg.draw()

    return 
