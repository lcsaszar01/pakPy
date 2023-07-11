#!/usr/bin/env python3

import pickle as pk
import u

def compact(nodes, kmer_size):
    print('starting compact')
    
    node_threshold = 100000 #number taken from suggested value in paper.
    num_nodes = len(nodes)
    
    begin_kmer_lst = []
    pcontig_lst = []
    count = 1
    
    while((num_nodes > node_threshold) == True):
        
        I  = generate_indep_set(nodes, kmer_size)
        count +=1
        '''
        For every node u that exists in I, pass u.pred_ext to u's successor and u.succ_ext to u's predecessor, and then delete u.
        Iterate_and_pack_node returns the lst of neightboring nodes to be modifided. 
        '''
        
        transfer_nodeInfo, pcontig_lst = iterate_and_pack(I, nodes, kmer_size)
        
        new_size = num_nodes-len(I)
        print('length of I',len(I),'numbers of nodes', num_nodes,"new size",new_size)
        
        '''
        Inform all nodes that are neightbors of deleted nodes in I so that they can update their extensions.
        This was achieved in the oringal PaKman by using MPI_Alltoallv.
        Alternative:
        '''
        rewire_nodes_lst = serialize_and_transfer(transfer_nodeInfo, nodes)
        begin_kmer_lst.append(rewire_nodes_lst)
        
        '''below psudocode needed for threading
        if count > 100:
            break{% load '''
        #global_nodes = MPI_Allgatherv(nodes)
    print('Compact is done')  
    return pcontig_lst, begin_kmer_lst #will need global_nodes for once  the MPI or MPI alterative for python

def generate_indep_set(node_lists,kmer_size):
    I = []
    for node in node_lists:
        key = node[0]
        max_kmer = key
        if len(node)!=0:
            i=node[1][1]
            
            if node[1][0] == 'Prefix': #For nodes are the Prefixes
                
                if len(i) >= kmer_size:
                    pred_node = i[0:(kmer_size-1)] # I intepreted this as if the length of 'i' affix length is larger then the kmer_size then 'i' should have its extra charater chopped off to (k-1)mer size
                else:
                    remainder = (kmer_size-1)-len(i)
                    pred_node = i+key[0:remainder]
                if len(pred_node) > len(key):
                    max_kmer=pred_node
                    break
            else:  #If the node is a Suffix
                
                if len(str(i)) >= (kmer_size-1):
                    succ_node = i[-(kmer_size-1):]
                else:
                    remainder = (kmer_size-1)-len(i)
                    succ_node = key[-remainder:]+i
                if len(succ_node) > len(key):
                    max_kmer = succ_node
                    break
            if max_kmer == key:
                I.append(node) 
        else:
            break          
    return I
    
def iterate_and_pack(I, nodes_list, kmer_size):
    pcontig_list = []
    transfer_nodeInfo = []
    
    for node in range(len(I)): #Controls the traversal through each node in list I
        if I[node][1][0] == 'Prefix': #looks at if the node is a prefix.
            pid = I[node][1][1] #takes the letter if node is a prefix
            if len(I[node][1][1]) > 0 and I[node][1][3]==0: #if the len of the prefix and the node is not terminal
                pred_node = I[node-1] #find the previous node in I
                pred_ext = I[node][0] #the extension to search with in the previous nodes.
            for suffix in range(len(I)):
                
                if I[suffix][1][0] == 'Suffix' and I[suffix][0]==I[node][0]:
                    sid = I[suffix][1][1]
                    
                    visit_count = I[suffix][1][4][2]
                    
            
                if(I[node][1][3]==1 and I[suffix][1][3]==1): #If the prefix node and suffix node are both terminal
                    contig = pid + I[node][0] + sid
                    #print("CONTIG with prefix, suffix, and k-1mer:",contig)
                    pcontig_list.append(contig) #append to contig list
        
            else:
                succ_node = I[node+1] #The successor node to the current node
                succ_ext = I[node+1][0] #the externsion to search with in prefixes
                
                for prefix in range(node+1,len(I)):
                    if I[prefix][1][0]=='Prefix' and I[prefix][1][1]==pid and I[prefix][1][3]!= 0:
                        target_proc = pred_node
                        new_ext = pred_ext + sid
                       
                        transfer_nodeInfo[target_proc] = tuple(pred_node, pred_ext, new_ext, visit_count)
                    if I[suffix][1][0]=='Suffix' and I[suffix][1][1]==sid and I[suffix][1][3]!= 0:
                        target_proc = succ_node
                        new_ext = pid + succ_ext
                        transfer_nodeInfo[target_proc] = [succ_node, succ_ext, new_ext, visit_count]
        
    return transfer_nodeInfo, pcontig_list

'''the function below was inspired by the serialization methods of https://www.knowledgehut.com/tutorials/python-tutorial/python-object-serialization#:~:text=Python%20%2D%20Object%20Serialization-,Object%20serialization%20is%20the%20process%20of%20converting%20state%20of%20an,object%20from%20the%20byte%20stream.'''


def serialize_and_transfer(node_list, transfer_nodeInfo):
    serial_buffer = []
    deserial_buffer = []
    fnode = []
    rewire_nodes_list = []
    for x in range(len(transfer_nodeInfo)):
        serial_buffer.append(pk.dumps(transfer_nodeInfo[x]))
    
    while(len(deserial_buffer) != 0):
        n = pk.loads(deserial_buffer)
        count = len(deserial_buffer) - 1
        for node in range(len(node_list)):
            if n == node_list[node]:
                fnode.append(node[n])
                affix = node[n][1][0] 
                if affix == 'suffix':
                    for idx in range(len(node)):
                        if fnode[idx][1][1]== n[node][1]:
                            fnode[idx][1][1]=n[node][2]
                            fnode[idx][1][2][1]=n[node][3]
                            
                else:
                    for idx in range(len(node)):
                        if fnode[idx][1][1]== n[node][1]:
                            fnode[idx][1][1]=n[node][2]
                            fnode[idx][1][2][1]=n[node][3]
                            
        if count == 100:
            break
    return rewire_nodes_list
                   
