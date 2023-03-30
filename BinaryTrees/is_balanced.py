"""
Write a f(n) that returns "true" if a Binary Tree is height balanced and "false" if it isn't.
A BT is height balanced if each node in the tree the height diff <= 1
"""

# O(n) time where n is number of nodes in tree, O(h) space where h is height of tree on stack


class Tree_Info():
    def __init__(self, is_balanced, height):
        self.is_balanced = is_balanced
        self.height = height


def is_balanced(tree):
    return get_tree_info(tree).is_balanced


def get_tree_info(node):
    if node is None:
        return Tree_Info(True, -1)

    left_tree_info = get_tree_info(node.left)
    right_tree_info = get_tree_info(node.right)

    is_balanced = (left_tree_info.is_balanced
                   and right_tree_info.is_balanced
                   and abs(left_tree_info.height - right_tree_info.height) <= 1
                   )

    height = max(left_tree_info.height, right_tree_info.height) + 1

    return Tree_Info(is_balanced, height)
