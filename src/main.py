#!/usr/bin/env python3
import reads as r
import fasta as f
import compact as c
import walker as w
import stats as s

import gpu_check as check

ans = ''
flag=True

check.precheck()
while(flag!=False):
    #ans = input("Do you want to create a fasta file? [Yes/No] > ")
    ans = 'n'
    if(ans=="Yes" or ans=="yes" or ans=='y' or ans=='Y'): 
        f.fasta_create()
        ans2 = input("What kmer size do you want? (Must be between 32-48 char) > ")
        if(int(ans2)<=48 and int(ans2)>=32):
            r.reads(int(ans2))
            flag=False
        break
    elif(ans=="No" or ans=='no' or ans=='n' or ans=='N'):
        #ans2 = input("What kmer size do you want? (Must be between 32-48 char) > ")
        ans2 = 32
        if(int(ans2)<=48 and int(ans2)>=32):
            graph, k_size = r.reader(int(ans2))
            global_graph, pcontig_lst, begin_kmer_lst = c.compact(graph,k_size)
            contigs = w.walk_alg(global_graph, pcontig_lst, begin_kmer_lst)
            print('Output Contigs:',contigs)
            s.stopwatch()
            flag=False
        break
    elif(ans=="Quit" or ans=="q" or ans=="exit"):
        flag=False
        break
    
    else: print("Not a valid input please try again...")


