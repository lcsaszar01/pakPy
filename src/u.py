#!/usr/bin/env python3

class node:
    def __init__(self, lmer, type, affix, counts, terminal):
        self.lmer = lmer
        self.type = type
        self.affix = affix
        self.counts = counts
        self.terminal = terminal
    
    def __str__(self):
        return f"{self.lmer}','{self.type}','{self.affix}','{self.counts}','{self.terminal}'\n'"  
    
    
    