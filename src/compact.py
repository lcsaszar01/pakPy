#!/usr/bin/env python3

import os
import pickle as pk
import u


def generate_indep_set(node_lists,kmer_size):
    I = []
    for node in node_lists:
        key = node[0]
        max_kmer = key

        if node[1][0] == 'Prefix':
            for i in node[1][1]:
                if len(i) >= kmer_size:
                    pred_node = i[0:(kmer_size-1)] # I intepreted this as if the length of 'i' affix length is larger then the kmer_size then 'i' should have its extra charater chopped off to (k-1)mer size
                else:
                    remainder = (kmer_size-1)-len(i)
                    pred_node = i+key[0:remainder]
                if len(pred_node) > len(key):
                    max_kmer=pred_node
                    break
        else:        
            for i in node[1][2]:
                if len(i) >= (kmer_size-1):
                    succ_node = i[-(kmer_size-1):]
                else:
                    remainder = (kmer_size-1)-len(i)
                    succ_node = key[-remainder:]+i
                if len(succ_node) > key:
                    max_kmer = succ_node
                    break
        if max_kmer == key:
            I.append(node)
                
        return I
    
def iterate_and_pack(node_lists, I, kmer_size):
    pcontig_list = []
    transfer_nodeInfo = []
    
    for num in range(len(I)):
        print(u.macro_node.wire_info)
        for prefix in u.macro_node.wire_info:
            pid = prefix
            print(pid)
            if len(I[num][1][2]) > 0 and I[num][1][3]==0:
                pred_node = I[num-1]
                pred_ext = I[num][1][2]
            for suffix in u.macro_node.wire_info:
                
                sid = suffix
                visit_count = I[num][1][2][0]
            
            if(I[pid[0]]==1 and I[sid[0]]==1):
                contig = I[num][pid[0]][3] + I[num][0] + I[num][sid[0]][3] 
                pcontig_list.append(contig)
                
            else:
                succ_node = I[num-1]
                succ_ext = I[num][1][1]
                if I[num][pid][3] != 0:
                    target_proc = pred_node
                    new_ext = pred_ext + I[num][pid][sid]
                    transfer_nodeInfo[target_proc] = tuple(pred_node, pred_ext, new_ext, visit_count)
                if I[num][sid] != 0:
                    target_proc = succ_node
                    new_ext = I[num][pid] + succ_ext
                    transfer_nodeInfo[target_proc] = tuple(succ_node, succ_ext, new_ext, visit_count)
                    
    return transfer_nodeInfo, pcontig_list

'''the function below was inspired by the serialization methods of https://www.knowledgehut.com/tutorials/python-tutorial/python-object-serialization#:~:text=Python%20%2D%20Object%20Serialization-,Object%20serialization%20is%20the%20process%20of%20converting%20state%20of%20an,object%20from%20the%20byte%20stream.'''


def serialize_and_transfer(node_list, transfer_nodeInfo, kmer_size):
    serial_buffer = []
    deserial_buffer = []
    fnode = []
    rewire_nodes_list = []
    for x in len(transfer_nodeInfo):
        serial_buffer.append(pk.pickle.dumps(transfer_nodeInfo[x]))
    #deserial_buffer.append(serial_buffer)
    while(len(deserial_buffer) != 0):
        n = pk.pickle.loads(deserial_buffer)
        
        return
    '''
            if n == gnode:
                fnode = gnode
                affix = gnode[1] 
                if affix is 'suffix':
                    for o in range(len(gnode)):
                        idx = fnode.get(key).get()
                        if idx == pred_next:
                            pass
                            
                else:
                    for y in range(len(gnode)):
                        idx = fnode.get().get()
    return rewire_nodes_list
    '''                   

def compact(nodes, kmer_size):
    print('starting compact')
    
    node_threshold = 100000 #number taken from suggested value in paper.
    I = []
    num_nodes = len(nodes)
    
    begin_kmer_lst = []
    pcontig_lst = []

    while((num_nodes > node_threshold) == False):
        I  = generate_indep_set(nodes, kmer_size)
        
        '''
        For every node u that exists in I, pass u.pred_ext to u's successor and u.succ_ext to u's predecessor, and then delete u.
        Iterate_and_pack_node returns the lst of neightboring nodes to be modifided. 
        '''
        transfer_nodeInfo, pcontig_lst = iterate_and_pack(nodes, I, kmer_size)
        print(" FUNC2:", transfer_nodeInfo, pcontig_lst)
        new_size = len(nodes)-len(I)
        print(new_size)
        
        '''
        Inform all nodes that are neightbors of deleted nodes in I so that they can update their extensions.
        This was achieved in the oringal PaKman by using MPI_Alltoallv.
        Alternative:
        '''
        rewire_nodes_lst = serialize_and_transfer(transfer_nodeInfo, nodes, kmer_size)
        begin_kmer_lst.append(rewire_nodes_lst)
        '''below psudocode needed for threading'''
        #global_nodes = MPI_Allgatherv(nodes)
    print('Compact is done')  
    return pcontig_lst, begin_kmer_lst #will need global_nodes for once  the MPI or MPI alterative for python
