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
Soln #2 ~ use one aux data structure 
WHITE: 0 = not visited
GREY: 1 = visiting (inStack)
BLACK: 2 = completed (no further edges, not in stack)

O(v + e) time 
O(v) space where v is no of vertices in graph
'''

WHITE, GREY, BLACK = 0, 1, 2

def colored_cycle_in_graph(edges):
    num_nodes = len(edges)
    
    colors = [False for _ in range(num_nodes)]
    
    for node in range(num_nodes):
        if colors[node] != WHITE:
            continue
        
        contains_cycle = traverse_and_color_nodes(node, edges, colors)
        if contains_cycle:
            return True
        
    return False

def traverse_and_color_nodes(node, edges, colors): 
    colors[node] = GREY
    
    neighbors = edges[node]
    for neighbor in neighbors:
        neighbor_color = colors[neighbor]
        
        if neighbor_color == GREY:
            return True 
        if neighbor_color == BLACK:
            continue
        
        contains_cycle = traverse_and_color_nodes(neighbor, edges, colors)
        
        if contains_cycle:
            return True
    
    colors[node] = BLACK
    return False 

### Practice (quiz-recall)
edges = [
    [1, 3],
    [2, 3, 4],
    [0],
    [],
    [2, 5],
    [],
]

# O(V + E) time where v is vertices (represented by indexes in edges) and E are neighbors (sublists, edges)
# O(V) space for colors 

# PLAYGROUND (PRACTICE)

WHITE, GREY, BLACK = 0, 1, 2

def cycle_in_graph(edges):
    colors = [WHITE for _ in range(len(edges)) ]
    for node in edges:
        if colors[node] == BLACK:
            continue
        
        has_cycle = dfs_and_color(edges, node, colors)
        if has_cycle:
            return True
        return False 
  
    
    
def dfs_and_color(edges, node, colors):
    colors[node] = GREY
    node_neighbors = edges[node]
    for neighbor in node_neighbors:
        neighbor_color = colors[neighbor]
        
        if neighbor_color == BLACK:
            continue 
        if neighbor_color == GREY:
            return True
        
        has_cycle = dfs_and_color(edges, neighbor, colors)
        if has_cycle:
            return True 
        
    return False 

'''
colors = [1, 1, 0, 1, 1, 0]
edges = [
    [1, 2],
    [3],
    []
    [4, 2],
    []
]

tree = 
   0 
 1 
3
4

'''