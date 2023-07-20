#!/usr/bin/env python3

from dataclasses import dataclass


@dataclass
class macro_node():
    lmers_and_attrs = []
    type = []
    affix = []
    prefixes = []
    suffixes = []
    prefix_terminal = []
    suffix_terminal = []
    counts = []
    precount = []
    sufcount=[]
    terminal = []
    temp = []
    temp2 = []
    wire_info=[]

    @staticmethod
    def createNodes(lmer, type, affix, counts, terminal):
        macro_node.type.append(type)
        macro_node.affix.append(affix)
        macro_node.counts.append(counts)
        macro_node.terminal.append(terminal)
        macro_node.temp2.append(lmer)
        macro_node.affix_sort(type, affix, terminal)
        
        macro_node.temp.append(macro_node.type.pop(0))
        macro_node.temp.append(macro_node.affix.pop(0))
        macro_node.temp.append(macro_node.counts.pop(0))
        macro_node.temp.append(macro_node.terminal.pop(0))
        
        
        macro_node.temp2.append(macro_node.temp.copy())
        macro_node.temp.clear()
        macro_node.lmers_and_attrs.append(macro_node.temp2.copy())
        macro_node.temp2.clear()
           
    @staticmethod
    def updateNode(info_to_update):
        for i in range(len(macro_node.lmers_and_attrs)):
            macro_node.lmers_and_attrs[i][1].extend(info_to_update[0])
        
    
    @staticmethod
    def clearNodes():
        macro_node.type.clear()
        macro_node.affix.clear()
        macro_node.counts.clear()
        macro_node.terminal.clear()
        macro_node.temp2.clear()
        macro_node.lmers_and_attrs.clear()
        
    def affix_sort(affix, value, terminal):

        if affix == "Prefix":
            macro_node.precount.append(1)
            macro_node.prefixes.append(value)
            macro_node.prefix_terminal.append(terminal)
        elif affix == "Suffix":
            macro_node.suffixes.append(value)
            macro_node.suffix_terminal.append(terminal)
            macro_node.sufcount.append(1)
            
        return len(macro_node.sufcount), len(macro_node.precount)
        
        
    