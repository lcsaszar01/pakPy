#!/usr/bin/env python3
import sys
sys.dont_write_bytecode = True
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
    visit_count = [] #Vertex Count for prefixes
    terminal = [] #Boolean for if the kmer-1 should be terminal for prefixes

    #For suffix
    visit_count2 = [] #Vertex Count for Suffixes
    terminal2 = [] #Boolean for is the kmer-1 should be terminal for suffixes
    
    wire_info = [] #Wire info returned from wire.py
    visit_match= [] #for both affixes, stores the combo list of each visit and match count while also allowing for duplicates. 
    
    @staticmethod
    def label(l):
        u.labels.append(l)

    @staticmethod 
    def prefix_info(p_letter, visit_count, match_count, terminal):
        u.p_letter.append(p_letter)
        u.visit_count.append(visit_count)
        u.terminal.append(terminal)
        u.visit_match.append([visit_count, match_count])
        u.node_info.update({"Type": 'Prefix' , "letter": p_letter, "visit_count:strings_matched": u.visit_match[-1], "Terminal": terminal})
 
    @staticmethod
    def suffix_info(s_letter, visit_count2, match_count2, terminal2):
        u.s_letter.append(s_letter)
        u.visit_count2.append(visit_count2)
        u.terminal2.append(terminal2)
        u.visit_match.append([visit_count2, match_count2])
        u.node_info.update({"Type": 'Suffix' , "letter": s_letter, "visit_count:match_count": u.visit_match[-1], "Terminal": terminal2})
        
    #Set the affix type
    def affix(self):
        if self.affix_type == 'prefix':
            self.affix = u.prefix_info()
        else:
            self.affix = u.suffix_info()

 
