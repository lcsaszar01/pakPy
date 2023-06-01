#!/usr/bin/env python3

import sys, os

curdir = os.path.dirname(__file__)
fasta_path = os.path.join(curdir+'/fasta_file')

file_name = input("Please enter the name of the file you want to analize. > ") 

fasta_path = os.path.join(fasta_path+"/"+file_name+".fasta")

if(os.path.isfile==True):
    fd = open(fasta_path, 'r')
        #Add window operations and call func
        
    fd.close()
else: print("Sorry that file does not exist in the fasta_file folder. Please try again >")

