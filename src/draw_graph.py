#!/usr/bin/env python3
import os
import networkx as netx
import matplotlib.pyplot as plt
import u
import random
import numpy as np

def draw():
    g = netx.MultiDiGraph()
    
    g.add_nodes_from(u.u.labels)
    edge_comp = []
    edge_tup = []
    edge_comp.extend(u.u.count) #prefixes edge info
    edge_comp.extend(u.u.count2) #suffixes edge info
    
    edge_str = ''
    edge_str = str(edge_comp)
    edge_str = edge_str.replace("{",'(')
    edge_str = edge_str.replace("}",')')
    edge_str = edge_str.replace("}",')') 
    edge_str = edge_str.replace(", ",'-')
    edge_str = edge_str.replace(":",',')
    edge_str = edge_str.replace("[",'')
    edge_str = edge_str.replace("]",'')
    edge_comp.clear()
    edge_comp = list(edge_str.split('-'))
    
    for r in range(len(edge_comp)):
        istr = edge_comp[r]
        tup = tuple(map(str, istr.split(', ')))
        edge_tup.append(tup)
        
    g.add_edges_from(edge_tup)

    plt.figure(figsize=(60,60.5))
    netx.draw_networkx(g, node_color="blue",node_shape="o",node_size=400, edgecolors="red", label="fake_dna_graph")
    
    #save graph as an image
    curdir = os.path.dirname(__file__)
    head, tail = os.path.split(curdir)
    intg = random.randint(0,100)
    path = os.path.join(head+"/graph_images/graph_output"+str(intg)+".png")
    plt.savefig(path)
    print("Graph drawing is complete.")
    return