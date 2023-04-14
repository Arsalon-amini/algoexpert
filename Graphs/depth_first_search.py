'''
You're given a Node class that has 'name' and an optional array of 'children' nodes. When put together, nodes form an acyclic tree-like structure.

Implement depth_first_search method on the Node class, which takes in an empty arry, traverses the tree using DFS (left to right), stores nodes' names in input array
and returns the array

graph = 

         A
    B    C    D
  E   F      G  H
     I  J   K
    
'''
# DFS_output =  [A, B, E, F, I, J, C, D, G, K, H]

# O(v+e) time where e is edges and v is vertices 
class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
    
    def add_child(self, name):
        self.children.append(Node(name)) 
        return self
    
    def depth_first_search(self, array):
        array.append(self.name)
        for child in self.children:
            child.depth_first_search(array)
        return array
    
    
# test
graph = Node("A")
graph.add_child("B").add_child("C").add_child("D")
graph.children[0].add_child("E").add_child("F")
graph.children[2].add_child("G").add_child("H")
graph.children[0].children[1].add_child("I").add_child("J")
graph.children[2].children[0].add_child("K")

print(graph)