#!/usr/bin/env python3
'''
An attempt to create a structure and class for the graphs 
Inspired by the class tutorials at https://stackoverflow.com/questions/40898482/defining-method-of-class-in-if-statement

'''
import os
import math as m
import wire as w


class u:
    def __init__(self, affix_type):
        self.affix_type = affix_type
     
    #For prefix 
    count = []
    terminal = []
    wire = []

    #For suffix
    count2 = []
    terminal2 = []
    wire2 = []
    
    @staticmethod 
    def prefix_info(count, terminal, wire):
        u.count.append(count)
        u.terminal.append(terminal)
        u.wire.append(wire)
                        
    @staticmethod
    def suffix_info(count2, terminal2, wire2):
        u.count2.append(count2)
        u.terminal2.append(terminal2)
        u.wire2.append(wire2)
        
    #Set the affix type
    def affix(self):
        if self.affix_type == 'prefix':
            self.affix = u.prefix_info(count, terminal, wire)
        else:
            self.affix = u.suffix_info(count, terminal, wire)
            
def graph_maker(kmer_list):
    enum = enumerate(kmer_list) #count the number of strings in the list to prep it for dictionary conversion

    kmer_dict = dict((x,y) for x,y in enum)

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
        for x in range(0,len(lmer1)):   #In theory these should be the same length of k_size
            lmerA+=lmer1[x] 
            lmerB+=lmer2[x]
 
        lmer1.clear()
        lmer2.clear()
        
        dict_str = () #takes a string from a dictonary value
        alpha_size = 0
        vertex_count = 0
        coverage = 100 #assuming 100 for the fake_dna sample that chatGPT created
        prefix_dict = {}
        suffix_dict = {}
        alpha_size2 =0
        vertex_count2=0
        found_countA = 0
        found_countB = 0
        
        label = u('prefix') 
        for d in range(len(kmer_dict)-1): #FIND EDGES FOR PREFIX
            count1 = 0
            for a in alpha:
                alpha_size +=1
                dict_str = kmer_dict.get(d)
                temp_lmer = a+lmerA
              
                if(dict_str == temp_lmer):
                    #print("FOR LETTER:", a) 
                    #print("DICTONARY VALUE", kmer_dict.get(d)) 
                    #print("ADDED LETTER:  ", temp_lmer) 
                    count1 += 1
                    vertex_count = m.ceil(count1/coverage)
                    #print("Vertex Count (vc):", vertex_count)
                    #print("In Dict\n")
                    prefix_dict.update({temp_lmer:vertex_count})
                    label.prefix_info(list(prefix_dict), [0], [0])
                    found_countA += 1     
                else:
                    pass 

        lmerA=''           
        label2 = u('suffix')
        for d2 in range(len(kmer_dict)-1): #FIND EDGES FOR SUFFIX
            count2 = 0
            for a2 in alpha:
                alpha_size2 +=1
                dict_str2 = kmer_dict.get(d2)
                temp_lmer2 = lmerB+a2
                if(dict_str2 == temp_lmer2):
                    #print("FOR LETTER:", a2) 
                    #print("DICTONARY VALUE", kmer_dict.get(d2)) 
                    #print("ADDED LETTER:  ", temp_lmer2)
                    count2 += 1
                    vertex_count2 = m.ceil(count2/coverage)
                    #print("Vertex Count (vc):", vertex_count)
                    #print("In Dict\n")
                    suffix_dict.update({temp_lmer2:vertex_count2})
                    label2.suffix_info(list(suffix_dict), [0], [0])
                    found_countB += 1
                    
                else:
                    pass
        lmerB=''  
         
    ulength = len(u.count)  
    for h in range(ulength):   
        print(u.count[h],u.terminal[h])
        print(u.count2[h],u.terminal[h])
    
'''
        LEFT TO DO:
			wire_info = wire(u)
			graph = u.wire_info.info()
    return graph
'''
 
####CALLING THE FUNCTION####
curdir = os.path.dirname(__file__)
path = os.path.join(curdir+"/fasta_files/dna_kmer.txt")
fd = open(path, 'r')
kmer_list = fd.read()
fd.close()
kmer_list = kmer_list[1:-1]
for i in kmer_list:
    kmer_list = kmer_list.replace("'", '')
    
kmer_list = list(kmer_list.split(', '))
graph_maker(kmer_list)

