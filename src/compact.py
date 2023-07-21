#!/usr/bin/env python3

import pickle as pk
import counter as cnt
import stats as stat
import u
import fnode
import time
import os 
def compact(nodes, kmer_size):
    print('starting compact')
    
    node_threshold = 100 #number taken from suggested value in paper.
    begin_kmer_lst = []
    pcontig_lst = []

    while((len(nodes) > node_threshold) == True):
        
        I  = generate_indep_set(nodes, kmer_size)
        
        '''
        For every node u that exists in I, pass u.pred_ext to u's successor and u.succ_ext to u's predecessor, and then delete u.
        Iterate_and_pack_node returns the lst of neightboring nodes to be modifided. 
        '''
        
        
        transfer_nodeInfo, pcontig_lst = iterate_and_pack(I, nodes, kmer_size)
        #print("Transfer node info:",transfer_nodeInfo, "pcontig", pcontig_lst)
        new_size = len(nodes)-len(I)
        
        '''Resize graph to new_size after deleting all macro_nodes ithat exitst in I
        This was achieved in the oringal PaKman by using MPI_Alltoallv.
        Alternative:'''
        while len(nodes) != new_size+1:
            for i in range(len(nodes)):
                for o in range(len(I)):
                    for k in range(len(I[o])-1):
                        if nodes[i]==I[o][k]:
                            nodes.pop(i) 
 
        rewire_nodes_lst = serialize_and_transfer(transfer_nodeInfo, nodes)
        begin_kmer_lst.append(rewire_nodes_lst)
        
        cnt.loop_count()
        #global_nodes = MPI_Allgatherv(nodes)
    print('Compact is done')  
    print(cnt.loop_total())
    a,b,c = stat.loop_stat(cnt.loop_total())
    print("Loop - 'while number of nodes > node_threshold", "numbers of loops:", a, "time in loop:", b, "Loops per sec:", c)
    return pcontig_lst, begin_kmer_lst #will need global_nodes for MPI alterative in python

def generate_indep_set(node_lists,kmer_size):
    I = []
    pred_node = []
    succ_node = []
    for n in range(len(node_lists)): #For each nodes in the list of nodes passed to the function
        key = node_lists[n][0] # the key is the k-1mer of the node
        max_kmer = key #same for max_kmer
        
        for i in u.macro_node.prefixes:
            if len(i) >= kmer_size-1:
                pred_node = i[0:kmer_size-1]
            else:
                remainder=(kmer_size-1)-len(i)
            if len(pred_node) > len(key):
                max_kmer = pred_node
                break
            
        for j in u.macro_node.suffixes:
            if len(j) >= (kmer_size-1):
                succ_node = j[-(kmer_size-1):0]
            else:
                remainder = (kmer_size-1)-len(i)
                succ_node = key[-remainder:0]+j
            if len(succ_node) > len(key):
                max_kmer = succ_node
                break
  
        #appending node
        if max_kmer == key:
            I.append(node_lists) 
                
    return I #Returns the list
    
def iterate_and_pack(I, nodes_list, kmer_size):
    pcontig_list = []
    transfer_nodeInfo = []
   
    for n in range(len(I)):
        for i in range(len(u.macro_node.wire_info)-1):
            pid = i 
            if len(u.macro_node.prefixes[i]) > 0 and u.macro_node.prefix_terminal[i]==0:  
                pred_node = I[n][0]
                pred_ext = I[n][0]
                
            for j in range(len(u.macro_node.wire_info[pid])):
                sid = j 
                visit_count = u.macro_node.wire_info[i][0]
    
                if(u.macro_node.prefix_terminal[pid]==0 and u.macro_node.suffix_terminal[sid]==0):
                    contig = str(u.macro_node.prefixes[pid]+u.macro_node.lmers_and_attrs[n][0]+u.macro_node.suffixes[sid])
                    pcontig_list.append(contig)
                else:
                    if(n < len(I)-1):
                        succ_node = I[n+1]
                        succ_ext = I[n][0]
                   
                    if u.macro_node.prefix_terminal[pid]!=0:
                        target_proc = pred_node
                        new_ext = pred_ext + u.macro_node.suffixes[sid]
                        transfer_nodeInfo.insert(target_proc, tuple(pred_node, pred_ext, new_ext, visit_count))
                    
                    if u.macro_node.suffix_terminal[sid]!=0:
                        target_proc = succ_node
                        new_ext = u.macro_node.prefixes[pid]+succ_ext
                        transfer_nodeInfo.insert(target_proc.tuple(succ_node,succ_ext,new_ext, visit_count))

    return transfer_nodeInfo, pcontig_list

'''the function below was inspired by the serialization methods of https://www.knowledgehut.com/tutorials/python-tutorial/python-object-serialization#:~:text=Python%20%2D%20Object%20Serialization-,Object%20serialization%20is%20the%20process%20of%20converting%20state%20of%20an,object%20from%20the%20byte%20stream.'''


def serialize_and_transfer(transfer_nodeInfo, node_list):
    serial_buffer = []
    deserial_buffer = []
    rewire_nodes_list = []
    
    for i in range(len(transfer_nodeInfo)):
        serial_buffer.append(pk.dumps(transfer_nodeInfo[i]))
    
    while(len(deserial_buffer) != 0):
        n = pk.loads(deserial_buffer)
        print("NODE FROM DESERIALIZE", n)
        count = len(deserial_buffer) - 1
        for j in range(len(node_list)):
            if n == node_list[j]:
                fnode=j[n]
                print('FNODE',fnode)
                if fnode[1][0]=='Suffix':
                    for idx in range(len(u.macro_node.suffixes)):
                        if u.macro_node.suffixes[idx] == n[idx][1]:
                            fnode.suffixes[idx]=n[j][1]
                            fnode.suffixes[idx]=n[j][2]
                            
                if fnode[1][0]=='Prefix':
                    for idx in range(len(u.macro_node.suffixes)):
                        if u.macro_node.prefix_terminal[idx]==n[idx][0]:
                            fnode[idx]=n[j][1]
                            fnode[idx]=n[j][2]
                rewire_nodes_list.append(fnode)           
        
    return rewire_nodes_list
                   
