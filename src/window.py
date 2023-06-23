#!/usr/bin/env python3

'''The function in this file traverses over the FASTA DNA sequence to capture sequences. 
starting at a kmer length of 32'''

import os, time
import counter as c

def window(dna_str, kmer_size):
    kmer=''
    count=0
    kmer_list=[]
    dna_list = list(dna_str)
    cnt = 1

    for x in range(0,((len(dna_list)-1)-kmer_size)):
        for y in range(x,len(dna_list)-1):
            count += 1
            kmer+=dna_list[y]
            if(count == kmer_size):
                
                kmer_list.append(kmer)
                kmer = ''
                count = 0
                break       
 
    curdir = os.path.dirname(__file__)
    head, tail = os.path.split(curdir)

    file_ext ='/kmers/dna_kmer_'+str(c.globe_count())+'.txt' #Globe_count increses the number linearly.
    file_path = head+file_ext
    mers = str(kmer_list)
    fd = open(file_path, "w+")
    fd.write(mers)
    fd.close()
      
    return kmer_list

