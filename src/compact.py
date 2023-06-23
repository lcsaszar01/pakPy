#!/usr/bin/env python3

import os
import pickle, pi

def compact(graph, node_threshold):
    num_nodes = 0
    threshold = 100000 #number taken from suggested value in paper.
    I = []
    num_nodes = len(graph)
    
    while(num_nodes > node_threshold):
        I  = generate_indep_set(graph)
        '''
        For every node u that exists in I, pass u.pred_ext to u's successor and u.succ_ext to u's predecessor, and then delete u.
        Iterate_and_pack_node returns the lst of neightboring nodes to be modifided. 
        '''
        (transwer_nodeInfo, pcontig_list) = iterate_and_pack(I,graph)
        New_size = len(graph)-len(I)
        
        '''
        Inform all nodes that are neightbors of deleted nodes in I so that they can update their extensions.
        This was achieved in the oringal PaKman by using MPI_Alltoallv.
        Alternative:
        '''
        
        rewire_nodes_lst = serialize_and_transfer(transwer_nodeInfo, graph)
        
        '''below psudocode needed for threading'''
        #global_graph = MPI_Allgatherv(graph)
        
    return(pcontig_lst, begin_kmer_lst) #will need global_graph for once  the MPI or MPI alterative for python

def generate_indep_set(node_dict,kmer_size):
    I = []
    for node in u.u.node_dict:
        key = len(node)
        max_kmer = key
        for i in len(u.u.node.get(node)):
            if len(i) >- kmer_size-1:
                pred_node = i
            else :
                remainder = (kmer_size-1)-len(i)
                pred_node = i+key[0:remainder]
            if pred_node > key:
                max_kmer=pred_node
                break
            
        for u in len(u.u.node.get(node)):
            vals = u.u.node.get(node)
            if vals.get('type')=='suffix':
                if len(j) >- (kmer_size-1):
                    succ_node = j[(kmer_size-1):]
                else:
                    remainder = (kmer_size-1)-len(j)
                    succ_node = key([-remainder:]+j)
                if succ_node > key:
                    max_kmer = succ_node
                    break
        if max_kmer == key:
            I.append(node)
                
        return I
    
def iterate_and_pack(node_dict, I, kmer_size):
    for node in I:
        for prefix in len(u.u.wire_info):
            pid = prefix
            if len(node_dict) > 0 and node_dict.get('terminal') == 0:
                pass
                
    return transfer_nodeInfo, pcontig_list

'''the function below was inspired by the serialization methods of https://www.knowledgehut.com/tutorials/python-tutorial/python-object-serialization#:~:text=Python%20%2D%20Object%20Serialization-,Object%20serialization%20is%20the%20process%20of%20converting%20state%20of%20an,object%20from%20the%20byte%20stream.'''

def serialize_and_transfer(node_dict, transfer_nodeInfo, kmer_size):
    serial_buffer = []
    deserial_buffer = []
    for x in len(transfer_nodeInfo):
        serial_buffer.append(pickle.dumps(transfer_nodeInfo[x]))
    deserial_buffer.append(serial_buffer)
    while(len(deserial_buffer) != 0):
        n = pickle.loads(deserial_buffer)
        for gnode in node_dict:
            if n == gnode:
                fnode =gnode
                type = node_dict.get(gnode)
                
                affix = type.get('type')
                if affix is 'suffix':
                    for o in range(len(gnode)):
                        idx = fnode.get(key).get(s_letter)
                        if idx == pred_next:
                            pass
                            
                else:
                    for y in range(len(gnode)):
                        idx = fnode.get(key).get(p_letter)
                        