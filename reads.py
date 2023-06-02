#!/usr/bin/env python3

import os

def reader():
    flag=True
    curdir = os.path.dirname(__file__)
    fasta_path = os.path.join(curdir+'/fasta_files') #Read in the file from the fasta folder
    while(flag is True):
        file_name = input("Please enter the name of the file you want to analize. > ") 
        
        if(file_name == "quit" or file_name == "q"): #exit option
            flag == False
            break
        
        fasta_path = os.path.join(fasta_path+"/"+file_name+".fasta")

        if(os.path.exists(fasta_path)==True): #If the file exists in the folder 
            k_size=32
            fd = open(fasta_path, 'r') #read the data from the file in the folder
            
            lines = fd.readlines() 
            fd.close()
            for lin in lines:
                print(lin)
                print(type(lin))
            
            while(flag!=False):
                size_of_acids = len(lin)
                if(size_of_acids%k_size==0): #if the number of acids can be perfectly divided into str of 32 acids or a size before 48
                    count = 0
                    kmer = ''
                    kmer_list = []
                    for y in range(0,len(lin)): 
                        lin_list = list(lin)
                        kmer+=lin_list[y]
                        count += 1
                        if(count == k_size): 
                            kmer_list.append(kmer)
                            kmer = ''
                            count = 0
            
                elif(k_size==48): #if you have to use the max length
                    k_size=47
                    count = 0
                    kmer = ''
                    kmer_list = []
                    for y in range(0,len(lin)): 
                        lin_list = list(lin)
                        kmer+=lin_list[y]
                        count += 1
                        if(count == k_size):
                            kmer_list.append(kmer)
                            kmer = ''
                            count = 0
                    
                else: k_size += 1 
                  
            #save to a file for helpful troubleshooting
            #can be removed in the final version
            curdir = os.path.dirname(__file__)
            file_path = curdir+'/fasta_files/kmer_data2.txt'
            kmer_list = str(kmer_list)
            fd = open(file_path, "w")
            fd.write(kmer_list)
            fd.close()
            return kmer_list
            
        else: #catch 22 for if the file does not exist
            print("Sorry that file does not exist in the fasta_file folder. Please try again...")
