#!/usr/bin/env python3

'''The function in this file traverses over the FASTA DNA sequence to capture sequences. 
starting at a kmer length of 32'''

import os
import counter as c
import stats

def window(dna_str, kmer_size):
    kmer=''
    count=0
    kmer_list=[]
    dna_list = list(dna_str)
    counter= 0

    for x in range(0,((len(dna_list)-1)-kmer_size)):
        counter += 1
        for y in range(x,len(dna_list)-1):
            count += 1
            kmer+=dna_list[y]
            if(count == kmer_size):
                
                kmer_list.append(kmer)
                kmer = ''
                count = 0
                break       
    stats.loop_stat(counter, "window (kmer-creation)")
    
    curdir = os.path.dirname(__file__)
    head, tail = os.path.split(curdir)
    fd = open(head+'/kmers/dna_kmer_'+str(c.globe_count())+'.txt',  "w+")
    fd.write(str(kmer_list))
    fd.close()
      
    return kmer_list

