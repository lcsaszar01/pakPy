#!/usr/bin/env python3

def list_prune(list_a, list_b):
    update_list_a = []
    update_list_a.extend(list_a.copy())
    for x in range(len(list_a)):
        for y in range(len(list_b)):
            print("A:", list_a[x])
            print("B:", list_b[y])
            
            if list_a[x][0] == list_b[y][0]:
                affix = list_a[x][1][0] == list_b[y][1][0] 
                if affix == True:
                    if affix == 'Suffix':
                        val = (list_b[y][1][1])
                        node_to_update = update_list_a[x][1]
                        node_to_update.extend(val)
                        
                    else: 
                        val = list_b[y][1][1]
                        node_to_update = update_list_a[x][1]
                        node_to_update.insert(1,val)
                else:
                    temp = []
                    temp.append(list_b[y][1][0])
                    temp.append(list_b[y][1][1])
                    node_to_update = update_list_a[x][1]
                    node_to_update.insert(1,temp) 
                    
    return update_list_a
                    

            

    