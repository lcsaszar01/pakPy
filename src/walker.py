#!/usr/bin/env python3 

import u
import stats

def walk_alg(global_graph, pcontig_list, begin_kmer_list):
    mn = []
    contigs = []
    count = 0
    partial_contig_size = len(pcontig_list)
    print("Begin Kmer:", begin_kmer_list)
    print("global_graph:", global_graph)
    for b in range(len(begin_kmer_list)):
        for o in range(len(global_graph)):
            if(begin_kmer_list[b]==global_graph[o]):
                mn.append(begin_kmer_list[b])
       
    for k in range(len(mn)):
        print('Node MN:',mn[k])
        count += 1
        if len(mn[k])==0:
          pass
        else:  
            if mn[k][1][3] == 0: #if the node is terminal
                prefix_id = mn[k][1][1]
                freq = mn[k][1][4][2]
                
                contigs.append(prefix_id)
                contigs.append(mn[k][0])
                
                walk(contigs,freq,0,mn,prefix_id)
    
    stats.loop_stat(count, "walk_alg")    
        
    return  

def walk(c,freq,offset_in_prefix, mn, pid):
    partial_contig_size = len(c)
    list_of_contigs = []
    freq_remain = freq
    internal_off = 0 #this keeps track of which entry within len of the the nodes wire_info[pid] to continue walking from
    count = 0
    
    print("THIS IS THE PID", pid)
    for i in range(len(u.macro_node.wire_info[pid])):
        count += 1
        sid = u.macro_node.wire_info[pid][i]
        sz = u.macro_node.wire_info[pid][i]
        offset_in_suffix = u.macro_node.wire_info[i][1]
        if internal_off == len(u.macro_node.wire_info):
            continue
        elif offset_in_prefix > internal_off:
            off_in_wire = offset_in_prefix-internal_off
            
        next_off = offset_in_suffix + off_in_wire
        freq_in_wire = min(freq_remain, (sz-off_in_wire))
        list_of_contigs.append(sid)
        for j in range(len(mn)):
            if mn[j][1][3] == 0:
                print(list_of_contigs)
            else:
                next_node = mn[j+1]
                next_prefix_id = mn[j+1][1][1]
                walk(list_of_contigs,freq_in_wire,next_off,next_node,next_prefix_id)
            freq_remain -= freq_in_wire
            list_of_contigs.clear() 
            list_of_contigs.insert(list_of_contigs,0)
            internal_off = u.macro_node.wire_info[j][2]
            
        stats.loop_stat(count, "walk")
    return list_of_contigs