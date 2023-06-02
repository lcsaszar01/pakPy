#!/usr/bin/env python3
'''
An attempt to create a structure and class for the graphs 
Inspired by the graph tutorials at https://www.tutorialspoint.com/python_data_structure/python_tuples_data_structure.htm


class graph:
    #class attribue
    type = "De Bruijn Graph"
    
    def __init__(self,gdict_pair=None, gdict_key=None): 
        self.gdict_pair = gdict_pair
        self.gdict_key = gdict_key

# Create the dictionary with graph elements
graph_elements = { 
   "a" : ["b","c"],
   "b" : ["a", "d"],
   "c" : ["a", "d"],
   "d" : ["e"],
   "e" : ["d"]
}
g = graph(graph_elements.keys(), graph_elements.values())
print(g.gdict_pair)
print(g.gdict_key)
'''

import os

def graph_maker(kmer_list):
    enum = enumerate(kmer_list)

    kmer_dict = dict((x,y) for x,y in enum)

    #send to a dictonary instead of a tuple because a tuple is immutable. 
    lmer1 = []
    lmer2 = []
    count = 0
    
    for i in range(0,1):
        kmer_str = kmer_dict[i]
        
        while(count != 3):
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
        lmer2.pop(0)
   
        lmerA = ''
        lmerB = ''
        for x in range(0,len(lmer1)):   #In theory these should be the same length
            lmerA+= lmer1[x] 
            lmerB+= lmer2[x]
            
        print(kmer_str, "--og kmer")
        print(lmerA)
        print(lmerB)
        
        ####START THE LETTER MATCHING TO THE DICT, SEE WHITEBOARD PHOTOS
        
####CALLING THE FUNCTION####
curdir = os.path.dirname(__file__)
path = os.path.join(curdir+"/fasta_files/kmer_data2.txt")
fd = open(path, 'r')
kmer_list = fd.read()
fd.close()
kmer_list = kmer_list[1:-1]
for i in kmer_list:
    kmer_list = kmer_list.replace("'", '')
    
kmer_list = list(kmer_list.split(', '))
graph_maker(kmer_list)

