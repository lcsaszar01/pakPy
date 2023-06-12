#!/usr/bin/env python3
'''
An attempt to create a structure and class for the graphs 
Inspired by the class tutorials at https://stackoverflow.com/questions/40898482/defining-method-of-class-in-if-statement
'''

import os
import math as m
import wire as w 

            
def graph_maker(kmer_list):

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
        
        label = u('prefix')#Initialize the data structure for the prefix type in the class 
        for d in range(len(kmer_dict)-1): #FIND EDGES FOR PREFIX
            for a in alpha:
                dict_str = kmer_dict.get(d)
                temp_lmer = a+lmerA
                comp = dict_str == temp_lmer

                #If the string exists in the dictionary
                if(comp == True):
                    found_countA += 1
                    #Gives us the number of vertices that the string should have
                    vertex_count = m.ceil(found_countA/coverage)
                    app = {temp_lmer:vertex_count}
                    prefix_dict.update(app)
                    logic = vertex_count==1
                    temp=[]
                    temp = app.copy()
            
                    if(logic is True): #Marks a terminal node if edge is 1
                        label.prefix_info(temp, 1, 0)    
                    else:
                        label.prefix_info(temp, 0, 0)
        lmerA=''
                 
        label2 = u('suffix') #Initialize the data structure for the suffix type in the class
        for d2 in range(len(kmer_dict)-1): #FIND EDGES FOR SUFFIX
            for a2 in alpha:
                dict_str2 = kmer_dict.get(d2)
                temp_lmer2 = lmerB+a2
                if(dict_str2 == temp_lmer2):
                    found_countB += 1
                    #Gives us the number of vertices that the string should have
                    vertex_count2 = m.ceil(found_countB/coverage)          
                    app2 = {temp_lmer2:vertex_count2}
                    suffix_dict.update(app2)
                    logic2 = vertex_count2==1
                    temp2=[]
                    temp2 = app2.copy()
            
                    if(logic2 is True): #Marks a terminal node if edge is 1
                        label2.suffix_info(temp2, 1, 0)
                    else:
                        label2.suffix_info(temp2, 0, 0)             
        lmerB=''  
        
    #appends the values into suffixes since its hard to do so in a python class    
    ulength = len(u.count) 
    for h in range(ulength):  
        val = ''
        val2 = ''
        val =  u.count[h]
        val2 = u.count2[h]
        u.prefixes.append(val)
        u.suffixes.append(val2)
        
    #save data to files for each affix type
    curdir = os.path.dirname(__file__)
    file_path1 = curdir+'/fasta_files/gd_prefix.txt'
    file_path2 = curdir+'/fasta_files/gd_suffix.txt' 
    
    fd = open(file_path1, "w")
    fd.write(str(u.prefixes))
    fd.close()
    
    fd = open(file_path2, "w")
    fd.write(str(u.suffixes))
    fd.close()

    wire_info = w.wire(str(u.prefixes), str(u.suffixes))
    graph = u.wire_info.append(wire_info)
    print(graph)
    return graph

class u:
    def __init__(self, affix_type):
        self.affix_type = affix_type
    
    #affixes    
    prefixes = []
    suffixes = []
    
    #For prefix 
    count = []
    terminal = []
    wire = []

    #For suffix
    count2 = []
    terminal2 = []
    wire2 = []
    
    wire_info = []
   
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
            self.affix = u.prefix_info()
        else:
            self.affix = u.suffix_info()

 
'''    CALLING THE FUNCTION    
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

'''