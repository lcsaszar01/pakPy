#!/usr/bin/env python3
'''
An attempt to create a structure and class for the graphs 
Inspired by the graph tutorials at https://www.tutorialspoint.com/python_data_structure/python_tuples_data_structure.htm

'''
import os

class u:
    def __init__(self, prefix_count, terminal):
        self.prefix_count = prefix_count
        self.terminal = terminal
        
    def show(self):
        print("THE PREFIX_COUNT:", self.prefix_counts, '\nTERMINAL?: ', self.terminal)

def graph_maker(kmer_list):
    enum = enumerate(kmer_list) #count the number of strings in the list to prep it for dictionary conversion

    kmer_dict = dict((x,y) for x,y in enum)

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
        for x in range(0,len(lmer1)):   #In theory these should be the same length
            lmerA+= lmer1[x] 
            lmerB+= lmer2[x]
            
        dict_str = () #takes a string from a dictonary value
        count1 =0
        alpha_size = 0
        vertex_count = 0
        coverage = 100 #assuming 100% for the fake_dna sample that chatGPT created
        prefix_dict = dict(mute_kmer='', vertex_count_str='') 

        for d in range(len(kmer_dict)):
            for a in alpha:
                alpha_size +=1
                print("FOR LETTER:", a)
                dict_str = kmer_dict.get(d)
                print("DICTONARY VALUE", kmer_dict.get(d))
                temp_lmer = a+lmerA
                print("ADDED LETTER:  ", temp_lmer)
                if(dict_str == temp_lmer):
                    count1 += 1
                    vertex_count = ceil(count1/coverage)
                    prefix_dict(temp_lmer, vertex_count)
                    lmer = u(prefix_dict, None)
                    lmer.show()
                    
                else:
                    print("Not in dict\n")
            '''
            LEFT TO DO:
            
            do edge detection
            graph = wire()
            return graph
            '''
 
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

