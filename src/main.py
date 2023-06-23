#!/usr/bin/env python3
import reads as r
import fasta as f
import graph as g
import timer as t
#import compact as pact

ans = ''
flag=True

while(flag!=False):
    ans = input("Do you want to create a fasta file? [Yes/No] > ")
    
    if(ans=="Yes" or ans=="yes" or ans=='y' or ans=='Y'): 
        f.fasta_create()
        ans2 = input("What kmer size do you want? (Must be between 32-48 char) > ")
        if(int(ans2)<=48 and int(ans2)>=32):
            r.reads(int(ans2))
            flag=False
        break
    elif(ans=="No" or ans=='no' or ans=='n' or ans=='N'):
        ans2 = input("What kmer size do you want? (Must be between 32-48 char) > ")
        if(int(ans2)<=48 and int(ans2)>=32):
            t.start()
            dna = r.reader(int(ans2))
            #pact.compact(dna, 100000, ans2)
            t.stop()
            t.stopwatch()
            flag=False
        break
    elif(ans=="Quit" or ans=="q"):
        flag=False
        break
    
    else: print("Not a valid input please try again...")


