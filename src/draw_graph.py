#!/usr/bin/env python3
import os
import networkx as netx
import matplotlib.pyplot as plt
import u
import random
import numpy as np
import counter as c

def draw():
    g = netx.MultiDiGraph()
    
    for key in u.u.node:
        vals = u.u.node.get(key)
        g.add_node(key, info = vals)
    
    lst = list(g.nodes(data=True))
    for t in range(len(lst)):
        print(lst[t],'\n')

    
        
    #for i in u.u.node.values():
        #print(i['letter'])
        #g.add_edges_from(tuple(i['letter']))
            

    
    plt.figure(figsize=(40,40.5))
    netx.draw_networkx(g, node_color="blue",node_shape="o",node_size=400, edgecolors="red", label="fake_dna_graph")
    
    #save graph as an image
    curdir = os.path.dirname(__file__)
    head, tail = os.path.split(curdir)
    c.count_clear()
    intg = c.globe_count()
    path = os.path.join(head+"/graph_images/graph_output"+str(intg)+".png")
    plt.savefig(path)
    
    
    print("Graph drawing is complete.")
    
    return