# given two binary trees, merge them, if two nodes overlap sum the values
"""
Result: took 25 minutes, I needed help on edge cases (if nodes are null), in end, I am still confused on what happens
on call stack when tree_one is None and we "return tree_two" 
how does that get appended (mutate) tree_one so that when we return tree_one the node is linked
ANSWER: I thought about it and realized we're setting tree_one.left = recursivefn(tree_one.left, tree_two.left) 
so if we return tree_two it will get assigned as the tree_one.left = tree_two_node on that line
"""

# tree_one =
#      1
#   3     2
#  7  4

# tree_two =
#     1
#   5     9
# 2     7  6

# merged_tree =
#    2
#  8     11
# 9  4  7  6

# Recursive Algorithm
# DFS
# at each level in stack
# a) both tree_one & tree_two have nodes -> sum them (assign to tree_one - mutated new tree)
# b) tree_one is not None & tree_two = None -> continue (tree_one value is value)
# c) tree_one = None & tree_two is not None -> tree_two.value is value at none
# O(n) time where n is the # of nodes in shortest tree | O(h) space where h is height (stack of nodes)


def merge_trees(tree_one, tree_two):
    if tree_one is None and tree_two is None:
        return

    if tree_one is None:
        return tree_two

    if tree_two is None:
        return tree_one

    tree_one.value += tree_two.value
    tree_one.left = merge_trees(tree_one.left, tree_two.left)
    tree_one.right = merge_trees(tree_one.right, tree_two.right)
    return tree_one
