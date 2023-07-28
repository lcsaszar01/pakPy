#!/usr/bin/env python3

import pickle as pk
import counter as cnt
import stats as stat
import u
import fnode 
import time

def compact(nodes, kmer_size):
    print('starting compact')
    
    node_threshold = 100000 #number taken from suggested value in paper.
    begin_kmer_lst = []
    pcontig_lst = []
    global_graph = []
    
    
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
        while len(nodes) != new_size:
        
            for o in range(len(I)):
                for s in range(1):
                    for n in nodes:
                        if n==I[o][s]:
                            nodes.pop()
                    
        rewire_nodes_lst = serialize_and_transfer(transfer_nodeInfo, nodes)
        begin_kmer_lst.append(rewire_nodes_lst)
        
        cnt.loop_count()
        
        global_graph.append(nodes)
    print('Compact is done')  
    stat.loop_stat(cnt.loop_total(), "while len(nodes) > node_threshold")
    
    return global_graph, pcontig_lst, begin_kmer_lst #will need global_nodes for MPI alterative in python

def generate_indep_set(node_lists,kmer_size):
    I = []
    pred_node = []
    succ_node = []
    count = 0 
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
            
        count += 1
    stat.loop_stat(count, 'generate_indep_set')
                
    return I #Returns the list
    
def iterate_and_pack(I, nodes_list, kmer_size):
    pcontig_list = []
    transfer_nodeInfo = []
    count = 0
   
    for n in range(len(I)):
        count += 1
        for i in range(len(u.macro_node.prefixes)):
            
            pid = i 
            if len(u.macro_node.prefixes[i]) > 0 and u.macro_node.prefix_terminal[i]==0:  
                pred_node = I[n-1]
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
    stat.loop_stat(count,"iterate_and_pack")
    return transfer_nodeInfo, pcontig_list

'''the function below was inspired by the serialization methods of https://www.knowledgehut.com/tutorials/python-tutorial/python-object-serialization#:~:text=Python%20%2D%20Object%20Serialization-,Object%20serialization%20is%20the%20process%20of%20converting%20state%20of%20an,object%20from%20the%20byte%20stream.

and https://www.geeksforgeeks.org/how-to-use-pickle-to-save-and-load-variables-in-python/
'''

#this function has several bugs in it relating to fnode but the pickling (pk) should be all ok.
def serialize_and_transfer(transfer_nodeInfo, node_list):
    serial_buffer = []
    deserial_buffer = []
    rewire_nodes_list = []
    
    #passing the transfer_nodeInfo list to serialize it
    for i in range(len(transfer_nodeInfo)):
        serial_buffer.append(pk.dumps(transfer_nodeInfo[i]))
    
    print(serial_buffer)
    
    #deserializing the info
    while(len(serial_buffer) != 0):
        for i in range(len(serial_buffer)):
            deserial_buffer.append(pk.loads(serial_buffer[i]))
            serial_buffer.pop(i)
        
        for n in deserial_buffer:
            count = len(deserial_buffer) - 1
            for j in range(len(node_list)):
                if n == node_list[j]:
                    fnode.lmers_and_attrs.append(n[j])
                    
                    if fnode.lmers_and_attrs[1][0]=='Suffix':
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
                   
