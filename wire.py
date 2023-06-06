

def wire(node):
    sc=0
    pc=0
    null_side =-1
    null_pid=-1
    
    for i in node.suffix: #calculate the sum of all suffix visists of node
        sc= sc+node.prefix_count[i].vertex_counts
        
    for j in node.prefix: #calculate the sum of all prefix visits of node
        pc = pc+ node.prefix_counts[j].vc
        
    for k in node.suffix: #initialize and assign value to the null suffix
        if(node.suffixes[k].size()==0):
            null_sid = k
            node.suffice_count[k]=(1,pc-sc)
            
    for y in node.prefix: #initialize and assign value to the null prefix
        if(node.prefix[y].size()==0):
            null_pid = y
            node.prefix_count[y] = (1, sc-pc)
            
    #Deal with leftovers
    leftovers = sc+node.suffix_count[null_sid].vc
    
    '''Initialize a wiring table for the macro-node to hold info realted to every suffix connected to a given prefix'''
    
    node.wire_info = (len(node.prefix()))
            
        
    return 