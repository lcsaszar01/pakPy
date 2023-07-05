#!/usr/bin/env python3

from dataclasses import dataclass
import time

@dataclass
class macro_node():
    lmers_and_attrs = []
    type = []
    affix = []
    counts = []
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
        macro_node.temp.append(macro_node.type.pop(0))
        macro_node.temp.append(macro_node.affix.pop(0))
        macro_node.temp.append(macro_node.counts.pop(0))
        macro_node.temp.append(macro_node.terminal.pop(0))
        
        macro_node.temp2.append(macro_node.temp.copy())
        macro_node.temp.clear()
        macro_node.lmers_and_attrs.append(macro_node.temp2.copy())
        macro_node.temp2.clear()
           
    @staticmethod
    def updateNodes(lmer, type, affix, counts, terminal, wire_info):
        
        pass
    
    @staticmethod
    def clearNodes():
        macro_node.type.clear()
        macro_node.affix.clear()
        macro_node.counts.clear()
        macro_node.terminal.clear()
        macro_node.temp2.clear()
        macro_node.lmers_and_attrs.clear()
        
        
    