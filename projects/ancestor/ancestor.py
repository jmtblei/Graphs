#given the dataset and id of individual in a dataset
#return the earliest known ancestor - the farthest distance from the input indiv
    #if there is more than 1 ancestor tied for earliest, return lowest number ID
    #if input individual has no parents, return -1

def earliest_ancestor(ancestors, starting_node):
    #if no parent, return -1
    known_ancestor = False
    for parent in ancestors:
        if parent[1] == starting_node:
            known_ancestor = True
            break
    if known_ancestor == False:
        return -1

    #use BFS to find the earliest known ancestor
    #create empty set to store visited pathss
    visited = set()
    #create empty queue 
    q = []
    #enqeue with path to starting node
    q.append([starting_node])
    #while the queue s not empty,
    while len(q) > 0:
        #dequeue the first path
        path = q.pop(0)
        #check if current is our target
        current = path[-1]
        #iterate our set to check for visited
        if current not in visited:
            #add them if visited
            visited.add(current)
        no_parent = False
        #add neighboring nodes (parents) to back of queue
        for parent in ancestors:
            if parent[1] == current:
                #copy the path
                copy = list(path)
                copy.append(parent[0])
                #enqueue the copy
                q.append(copy)
                no_parent = True
        #if curent has no ancestors, break
        if no_parent == False:
            q.append(list(path))
            break
    #check for the earliest known ancestor, return the lowest numerical one if tied
    earliest = []
    for path in q:
        if len(path) > len(earliest):
            earliest = list(path)
        elif len(path) == len(earliest):
            if path[-1] < earliest[-1]:
                earliest = list(path)
    #the earliest known ancestor is the furthest from input (end of the path)
    return earliest[-1]