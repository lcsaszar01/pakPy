#!/usr/bin/env python3

import os, sys 
import functions.py as func

def lmer_Freq_gen():
    lmer_freq['']  #buffer for lmer_frequency 
    
    for r in reads:
        for i in r :
            lmer_freq.append(i)
            
    return r, lmer_freq

func.lmer_glob_count()

def min_lmers(k):
    min_lmer=0
    min_lmers_count=0
    r, lmer_freq = lmer_Freq_gen()
    for k in r:
        for j in k:
            if(lmer_freq < min_lmers_count):
                min_lmer = j
                min_lmers_count = lmer_freq[j]
        target_id = func.min_lmer_id()
        



def kmer_count(proc_id, k, num_kmers):
    
    
    return k_update