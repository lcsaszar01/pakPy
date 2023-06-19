#!/usr/bin/env python3

class u:
    def __init__(self, affix_type):
        self.affix_type = affix_type
       
    #Info for the Nodes, will be the values() of the node dictionary
    node_info = {}
    
    #Node Dictonary for graph creation
    node = {}   
    
    #lable list
    labels = [] #kmer-1 without the letter that matches 
    
    #affixes letter of the alphabet that contribute to string matches of kmer-1    
    p_letter = []
    s_letter = []
    
    #For prefix 
    vertex_count = [] #Vertex Count for prefixes
    terminal = [] #Boolean for if the kmer-1 should be terminal for prefixes
    match_count = [] #number of matches found

    #For suffix
    vertex_count2 = [] #Vertex Count for Suffixes
    terminal2 = [] #Boolean for is the kmer-1 should be terminal for suffixes
    match_count2 = [] #number of matches found
    
    wire_info = [] #Wire info returned from wire.py
    
    @staticmethod
    def label(l):
        u.labels.append(l)

    @staticmethod 
    def prefix_info(p_letter, vertex_count, match_count, terminal):
        u.p_letter.append(p_letter)
        u.vertex_count.append(vertex_count)
        u.terminal.append(terminal)
        u.match_count.append(match_count)
        u.node_info.update({"Type": 'Prefix' , "letter": p_letter, "vertex_count":vertex_count, "strings_matched": match_count, "Terminal": terminal})
 
    @staticmethod
    def suffix_info(s_letter, vertex_count2, match_count2, terminal2):
        u.s_letter.append(s_letter)
        u.vertex_count2.append(vertex_count2)
        u.terminal2.append(terminal2)
        u.match_count2.append(match_count2)
        u.node_info.update({"Type": 'Suffix' , "letter": s_letter, "vertex_count":vertex_count2, "strings_matched": match_count2, "Terminal": terminal2})
        
    #Set the affix type
    def affix(self):
        if self.affix_type == 'prefix':
            self.affix = u.prefix_info()
        else:
            self.affix = u.suffix_info()

 
