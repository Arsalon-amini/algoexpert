"""
Given two binary trees, merge them and return the resulting tree. If two nodes overlap, sum the values.
Solution can either mutate the existing tree or return a new tree.
"""

# Recursive soln | 
# O(n) time where n = # nodes in smallest tree
# O(h) space where h is height of smaller tree (O(n) if it's a single list)

class Tree:
    def __init__(self, value):
        self.value = value
        self.right = Tree
        self.left = Tree 

def merge_trees(tree_one_node, tree_two_node):
    if tree_one_node is None:
        return tree_two_node
    if tree_two_node is None:
        return tree_one_node
    
    tree_one_node.value += tree_two_node.value
    
    tree_one_node.left = merge_trees(tree_one_node.left, tree_two_node.left)
    tree_one_node.right = merge_trees(tree_one_node.right, tree_two_node.right)
    