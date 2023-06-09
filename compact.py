#!/usr/bin/env python3

import os

def cmpact(graph, node_threshold):
    num_nodes = 0
    I = []
    num_nodes = len(graph)
    
    while(num_nodes > node_threshold):
        I  = gen_independ_set(graph)
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