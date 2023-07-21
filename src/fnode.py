#!/usr/bin/env python3

from dataclasses import dataclass


@dataclass
class fnode():
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
        fnode.type.append(type)
        fnode.affix.append(affix)
        fnode.counts.append(counts)
        fnode.terminal.append(terminal)
        fnode.temp2.append(lmer)
        fnode.affix_sort(type, affix, terminal)
        
        fnode.temp.append(fnode.type.pop(0))
        fnode.temp.append(fnode.affix.pop(0))
        fnode.temp.append(fnode.counts.pop(0))
        fnode.temp.append(fnode.terminal.pop(0))
        
        
        fnode.temp2.append(fnode.temp.copy())
        fnode.temp.clear()
        fnode.lmers_and_attrs.append(fnode.temp2.copy())
        fnode.temp2.clear()
           
    @staticmethod
    def updateNode(info_to_update):
        for i in range(len(fnode.lmers_and_attrs)):
            fnode.lmers_and_attrs[i][1].extend(info_to_update[0])
        
    
    @staticmethod
    def clearNodes():
        fnode.type.clear()
        fnode.affix.clear()
        fnode.counts.clear()
        fnode.terminal.clear()
        fnode.temp2.clear()
        fnode.lmers_and_attrs.clear()
        
    def affix_sort(affix, value, terminal):

        if affix == "Prefix":
            fnode.precount.append(1)
            fnode.prefixes.append(value)
            fnode.prefix_terminal.append(terminal)
        elif affix == "Suffix":
            fnode.suffixes.append(value)
            fnode.suffix_terminal.append(terminal)
            fnode.sufcount.append(1)
            
        return len(fnode.sufcount), len(fnode.precount)
        
        
    