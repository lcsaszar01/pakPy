#!/usr/bin/env python3 

import os, sys
import u

def walk_alg(compact_graph, begin_kmer_list):
    mn = []
    contigs = []
    
    for b in range(len(begin_kmer_list)):
        for j in range(len(compact_graph)):
            comp = compact_graph[b][0] == begin_kmer_list[j][0]
            if comp == True:
                mn.append(comp)
                print(comp)
                
    for i in range(len(mn)):
        if mn[i][1][3] == 0: #if the node is terminal
            prefix_id = mn[i][1][1]
            freq = mn[i][1][2][1]
            c = []
            c.append(mn[i][1][1])
            c.append(mn[i][0])
            
            contigs.append(walk(c,freq,0,mn,prefix_id))
                
                #for i in range(len(compact_graph)):
    return contigs    

def walk(c,freq,offset_in_prefix, mn, pid):
    partial_contig_size = len(c)
    list_of_contigs = []
    freq_remain = freq
    internal_off = 0 #this keeps track of which entry within len of the the nodes wire_info[pid] to continue walking from
    for i in range(len(u.macro_node.wire_info)):
        sid = u.macro_node.wire_info[i][0]
        sz = u.macro_node.wire_info[i][2]
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
    return list_of_contigs