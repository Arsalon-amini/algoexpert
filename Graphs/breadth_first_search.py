'''
You're given a Node class that has a name and optional array of children nodes. 

Implement breadth_first_search on the Node class, which takes in an empty array, traverses the tree using bfs (left to right), stores nodes' names
in input array, returns it.

O(V+E) time where V is vertice (node) and E are children nodes
O(V) space 

Graph = 
        A
   B    C     D
E   F       G   H
   I  J          K
   

'''


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def add_child(self, name):
        self.children.append(Node(name))
        return self

    def breadth_first_search(self, array):
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            array.append(current.name)
            for child in current.children:
                queue.append(child)

        return array
