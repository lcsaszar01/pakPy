#!/usr/bin/env python3

import sys, os
import reads as r
import fasta as f

flag=True
while(flag==True):
    ans = input("Do you want to create a fasta file? > ")
    if(ans=="No"):
        flag=False
    elif(ans=="Yes") : 
        f.fasta_create()
        flag=False
    elif(ans=="Quit" or ans=="q"):
        flag=False
    else: print("Not a valid input please try again")


