#!/usr/bin/env python3

class u:
    def __init__(self, affix_type):
        self.affix_type = affix_type
        
    #lable list
    labels = []
    
    #affixes    
    prefixes = []
    suffixes = []
    
    #For prefix 
    count = []
    terminal = []
    #wire = []

    #For suffix
    count2 = []
    terminal2 = []
    #wire2 = []
    
    wire_info = []
    
    @staticmethod
    def label(l):
        u.labels.append(l)

    @staticmethod 
    def prefix_info(count, terminal):
        u.count.append(count)
        u.terminal.append(terminal)
        #u.wire.append(wire)
                        
    @staticmethod
    def suffix_info(count2, terminal2):
        u.count2.append(count2)
        u.terminal2.append(terminal2)
        #u.wire2.append(wire2)
        
    #Set the affix type
    def affix(self):
        if self.affix_type == 'prefix':
            self.affix = u.prefix_info()
        else:
            self.affix = u.suffix_info()

 
