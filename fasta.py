#!/usr/bin/env python3
'''
Creates gene data set files in the .fasta format
'''

import os 

def fasta_create():
    file_name = input("Please enter the file name > ")
    file_name += ".fasta"
    head = '> '
    head += input("Please enter header info for the fasta file. > ")
    data = input("Please enter the amino acid sequence. > ")
    
    curdir = os.path.dirname(__file__)
    file_path = curdir+'/fasta_files/'+ file_name
    
    fd = open(file_path, "w")
    fd.write(head +'\n'+ data)
    fd.close()

fasta_create()
