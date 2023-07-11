#!/usr/bin/env python3

import os
import window as win
import graph as g
import compact as c
import walker as w


def reader(k_size):
    flag=True
    curdir = os.path.dirname(__file__)
    head, tail = os.path.split(curdir)
    fasta_path = os.path.join(head+"/fasta_files")
    dna = []
    
    while(flag == True):
        #file_name = input("Please enter the name of the file you want to analize. > ") 
        file_name = 'ecoli'
        if(file_name == "quit" or file_name == "q"): #exit option
            flag == False
            break
        
        fasta_path = os.path.join(fasta_path+"/"+file_name+".fasta")
        if(os.path.exists(fasta_path)==True):
            flag=False
        
            if(os.path.exists(fasta_path)==True): #If the file exists in the folder 
                
                fd = open(fasta_path, 'r') #read the data from the file in the folder
                
                lines = fd.readlines()
                
                for lin in lines[0:2]: #gets rid of the info line of the file
                    #number limitation is a temp fix for not allowing it to run all the data and fill up the HD
                    if(lin.startswith('>')==False): #passes over info header lines
                        print(lin) 
                        dna = win.window(lin, k_size) #gets the overlapping kmer of a given k_size
                        graph = g.graph_maker(dna)
                        pcontig_lst, begin_kmer_lst = c.compact(graph,k_size)
                        print('pcontig list:', pcontig_lst) 
                        print('Begin kmer list:', begin_kmer_lst)
                        contigs = w.walk_alg(graph,begin_kmer_lst)
                        print('Contigs',contigs)
                        
                    else:
                        continue  
        
        else: #catch 22 for if the file does not exist
            print("Sorry that file does not exist in the fasta_file folder. Please try again...")
