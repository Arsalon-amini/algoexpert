'''
Given a list of edges representing an unweighted, directed graph with at least one node. 
Write a function that returns a boolean representing whether the given graph contains a cycle.
A cycle (here) is defined as a chain of at least one vertex in which the first vertex is the same as the last

edges = [
    [1, 3],
    [2, 3, 4],
    [0],
    [],
    [2, 5],
    [],
]
'''

'''
Soln #1 ~ use two aux data structures (0 = false, 1 = true)
visited = [len(graph)] ex [ False, False, False, False, False, False]
inStack = [len(graph)]

O(v + e) time 
O(v) space where v is no of vertices in graph
'''

def cycle_in_graph(edges):
    num_nodes = len(edges)
    visited = [False for _ in range(num_nodes)]
    currently_in_stack = [False for _ in range(num_nodes)]
    
    for node in range(num_nodes):
        if visited[node]: 
            continue
        
        contains_cycle = is_node_in_cycle(edges, node, visited, currently_in_stack)
        if contains_cycle:
            return True
     
    return False
        

def is_node_in_cycle(edges, node, visited, currently_in_stack):
    visited[node] = True
    currently_in_stack[node] = True
    
    neighbors = edges[node] 
    
    for neighbor in neighbors:
        if not visited[neighbor]:
            contains_cycle = is_node_in_cycle(edges, neighbor, visited, currently_in_stack)
            if contains_cycle:
                return True 
        elif currently_in_stack[neighbor]:
            return True 
        
    currently_in_stack[node] = False 
    return False 
        
        
'''
Soln #2 ~ use one aux data structure (0 = not visited, 1 = visiting, 2 = completed (no further edges))
O(v + e) time 
O(v) space where v is no of vertices in graph
'''