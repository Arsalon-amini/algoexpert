"""
Given two binary trees, merge them and return the resulting tree. If two nodes overlap, sum the values.
Solution can either mutate the existing tree or return a new tree.
"""

# Recursive soln |
# O(n) time where n = # nodes in smallest tree
# O(h) space where h is height of smaller tree (O(n) if it's a single list)


class Tree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Test solution ~
tree_one = Tree(1)
tree_one.left = Tree(3)
tree_one.left.left = Tree(7)
tree_one.left.right = Tree(4)
tree_one.right = Tree(2)

tree_two = Tree(1)
tree_two.left = Tree(5)
tree_two.left.left = Tree(2)
tree_two.right = Tree(9)
tree_two.right.left = Tree(7)
tree_two.right.right = Tree(6)

# Recursive Soln
def merge_trees(tree_one_node, tree_two_node):
    if tree_one_node is None:
        return tree_two_node
    if tree_two_node is None:
        return tree_one_node

    tree_one_node.value += tree_two_node.value

    tree_one_node.left = merge_trees(tree_one_node.left, tree_two_node.left)
    tree_one_node.right = merge_trees(tree_one_node.right, tree_two_node.right)

    return tree_one_node


result = merge_trees(tree_one, tree_two)
print(result)

# Iterative solution - depth first search using a stack 
def merge_bts(tree_one_node, tree_two_node):
    if tree_one_node is None:
        return tree_two_node
    
    stack_one = [tree_one_node]
    stack_two = [tree_two_node]
    
    while len(stack_one) > 0:
        tree_one_node = stack_one.pop() 
        tree_two_node = stack_two.pop()
        
        # accept tree_one_node as single node in merged tree
        if tree_two_node is None:
            continue 
        
        tree_one_node.value += tree_two_node.value
        
        # Case 1: Tree1 doesn't have a left, use Tree2 left as node in our merged tree
        if tree_one_node.left is None:
            tree_one_node.left = tree_two_node.left  
        else:
            stack_one.append(tree_one_node.left)
            stack_two.append(tree_two_node.left)
    
        # Case 2: Tree1 doesn't have a right, use Tree2 right as node in our merged tree
        if tree_one_node.right is None:
            tree_one_node.right = tree_two_node.right
        else:
            stack_one.append(tree_one_node.right)
            stack_two.append(tree_two_node.right)
            
    return tree_one