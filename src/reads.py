#!/usr/bin/env python3

import os
import window as win
import time
import graph as g
import sys
sys.dont_write_bytecode = True
def reader(k_size):
    flag=True
    curdir = os.path.dirname(__file__)
    head, tail = os.path.split(curdir)
    fasta_path = os.path.join(head+"/fasta_files")
    dna = []
    
    while(flag is True):
        file_name = input("Please enter the name of the file you want to analize. > ") 
        
        if(file_name == "quit" or file_name == "q"): #exit option
            flag == False
            break
        
        fasta_path = os.path.join(fasta_path+"/"+file_name+".fasta")

        if(os.path.exists(fasta_path)==True): #If the file exists in the folder 
            fd = open(fasta_path, 'r') #read the data from the file in the folder
            
            lines = fd.readlines()
            
            for lin in lines[0:6]: #gets rid of the info line of the file
                #number limitation is a temp fix for not allowing it to run all the data and fill up the HD
                if(lin.startswith('>')==False): #passes over info header lines
                    print(lin) 
                    dna = win.window(lin, k_size) #gets the overlapping kmer of a given k_size
                    g.graph_maker(dna)
                else:
                    continue
                    
            return dna
        
        else: #catch 22 for if the file does not exist
            print("Sorry that file does not exist in the fasta_file folder. Please try again...")
