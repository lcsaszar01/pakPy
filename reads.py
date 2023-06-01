#!/usr/bin/env python3

import sys, os


curdir = os.path.dirname(__file__)
fasta_path = os.path.join(curdir+'/fasta_file')

def reader():
    flag=True
    while(flag is True):
        file_name = input("Please enter the name of the file you want to analize. > ") 
        fasta_path = " "
        if(file_name != "quit" or file_name != "q"):
            fasta_path = os.path.join(fasta_path+"/"+file_name+".fasta")

            if(os.path.exists(fasta_path)==True):
                fd = open(fasta_path, 'r')
                    #Add window operations and call func
                    
                fd.close()
                flag=False
            else: 
                print("Sorry that file does not exist in the fasta_file folder. Please try again >")
                flag=False
        else: flag=False

reader()