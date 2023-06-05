#!/usr/bin/env python3
'''
An attempt to create a structure and class for the graphs 
Inspired by the graph tutorials at https://www.tutorialspoint.com/python_data_structure/python_tuples_data_structure.htm

'''
import os
import math as m
import wire

class u:
    def __init__subclass__(wire_info, info):
        super().__init_subclass__(info)
        wire_info.info=info
    def __init__subclass__(prefix, prefix_count, terminal):
        prefix.prefix_count = prefix_count
        prefix.terminal = terminal
    def __init__subclass__(suffix, suffix_count, terminal):
        suffix.suffix_count = suffix_count
        suffix.terminal = terminal
        
    def showA(self):
        print("THE PREFIX_COUNT:", u.prefix.prefix_counts, '\nTERMINAL?: ', u.prefix.terminal)
    def showB(self):
        print("THE PREFIX_COUNT:", u.suffix.suffix_counts, '\nTERMINAL?: ', u.suffix.terminal)

def graph_maker(kmer_list):
    enum = enumerate(kmer_list) #count the number of strings in the list to prep it for dictionary conversion

    kmer_dict = dict((x,y) for x,y in enum)
    print(kmer_dict)

    #send to a dictonary instead of a tuple because a tuple is immutable. 
    lmer1 = []
    lmer2 = []
    count = 0
    alpha = ('A','T','C','G')
     
    for i in range(0,1):
        kmer_str = kmer_dict[i]
        
        while(count != 3):  #splits total string of dna bases of the best kmer size between 32 and 42
            count +=1
            if(count == 1):
                kmer_list_temp = list(kmer_str)      
                for j in kmer_list_temp:
                    lmer1 += j      
            elif(count == 2):
                kmer_list_temp = list(kmer_str)   
                for j in kmer_list_temp:
                    lmer2 += j
            
        lmer1.pop(len(lmer1)-1)
        lmer2.pop(0) #gets the greater than symbol out of the string
   
        lmerA = ''
        lmerB = ''
        for x in range(0,len(lmer1)):   #In theory these should be the same length of k_size
            lmerA+= lmer1[x] 
            lmerB+= lmer2[x]
            
        dict_str = () #takes a string from a dictonary value
        count1 =0
        alpha_size = 0
        vertex_count = 0
        coverage = 100 #assuming 100% for the fake_dna sample that chatGPT created
        prefix_dict = {}
        suffix_dict = {}
        count2=0
        alpha_size2 =0
        vertex_count2=0
        
        print(len(kmer_dict))
        
        for d in range(len(kmer_dict)-1): #FIND EDGES FOR PREFIX
            for a in alpha:
                alpha_size +=1
                print("FOR LETTER:", a)
                dict_str = kmer_dict.get(d)
                print("DICTONARY VALUE", kmer_dict.get(d))
                temp_lmer = a+lmerA
                print("ADDED LETTER:  ", temp_lmer)
                if(dict_str == temp_lmer):
                    count1 += 1
                    vertex_count = m.ceil(count1/coverage)
                    print(vertex_count)
                    prefix_dict.update({temp_lmer:vertex_count})
                    lmer = u.prefix(prefix_dict, None)
                    lmer.showA()
                    
                else:
                    print("Not in dict\n")
                    
        print("\nSUFFIX\n")
        for d2 in range(len(kmer_dict)-1): #FIND EDGES FOR SUFFIX
            for a2 in alpha:
                alpha_size2 +=1
                print("FOR LETTER:", a2)
                dict_str2 = kmer_dict.get(d2)
                print("DICTONARY VALUE", kmer_dict.get(d2))
                temp_lmer2 = lmerB+a2
                print("ADDED LETTER:  ", temp_lmer2)
                if(dict_str2 == temp_lmer2):
                    count2 += 1
                    vertex_count2 = m.ceil(count2/coverage)
                    print("In Dict")
                    suffix_dict.update({temp_lmer2:vertex_count2})
                    lmer = u.suffix(suffix_dict, None)
                    lmer.showB()
                    
                else:
                    print("Not in dict\n")
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

