#!/usr/bin/env python3

'''The function in this file traverses over the FASTA DNA sequence to capture sequences. 
starting at a kmer length of 32'''

import os

def window(dna_str, kmer_size):
    kmer=''
    count=0
    kmer_list=[]
    dna_list = list(dna_str)
    for x in range(0,len(dna_list)):
        for y in range(x,len(dna_list)):
            count += 1
            kmer+=dna_list[y]
            if(count == kmer_size): 
                kmer_list.append(kmer)
                kmer = ''
                count = 0
                break
    
    curdir = os.path.dirname(__file__)
    head, tail = os.path.split(curdir)
    file_ext ='/fasta_files/dna_kmer_'+str(os.urandom(1))+'.txt' 
    file_path = head+file_ext
    dna_list = str(kmer_list)
    fd = open(file_path, "w")
    fd.write(dna_list)
    fd.close()      
    return kmer_list

