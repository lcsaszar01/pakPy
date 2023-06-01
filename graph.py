#!/usr/bin/env python3
'''
An attempt to create a structure and class for the graphs 
Inspired by the graph tutorials at https://www.tutorialspoint.com/python_data_structure/python_tuples_data_structure.htm
'''

class graph:
    #class attribue
    type = "De Bruijn Graph"
    
    def __init__(self,gdict_pair=None, gdict_key=None): 
        self.gdict_pair = gdict_pair
        self.gdict_key = gdict_key

# Create the dictionary with graph elements
graph_elements = { 
   "a" : ["b","c"],
   "b" : ["a", "d"],
   "c" : ["a", "d"],
   "d" : ["e"],
   "e" : ["d"]
}
g = graph(graph_elements.keys(), graph_elements.values())
print(g.gdict_pair)
print(g.gdict_key)