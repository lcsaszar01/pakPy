#!/usr/bin/env python3

import networkx as netx
import matplotlib.pyplot as plt

def draw(local_graph_info, afix_node):
    
    netx.draw_shell(local_graph_info, nlist=afix_node, with_labels=True, font_weight='bold')
    
    return 