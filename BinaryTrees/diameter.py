# write a fn that takes a BT and returns its diameter.
# Diameter is length of longest path, even if that path doesn't pass through root of tree.
# length of a path is number of edges between path first node and last node
# O(n) time | O(n) space

def get_diameter(tree):
    return calc_tree_info(tree).diameter


def calc_tree_info(node):
    if node is None:
        return NodeInfo(0, 0)

    left_subtree_info = calc_tree_info(node.left)
    right_subtree_info = calc_tree_info(node.right)

    diameter = max(left_subtree_info.diameter, right_subtree_info.diameter,
                   (left_subtree_info.height + right_subtree_info.height))

    height = 1 + max(left_subtree_info.height, right_subtree_info.height)

    return NodeInfo(diameter, height)


class NodeInfo:
    def __init__(self, diameter, height):
        self.diameter = diameter
        self.height = height


# Write a f(n) that takes in a BT and returns the diameter. D is length of longest path, even if it doesn't pass the root

#          1
#      3      2
#    7    4
#  8        5
# 9           6

# current_diameter - left_sub_tree_height + right_sub_tree_height

def get_diameter(tree):
    return calc_tree_info(tree).diameter


def calc_tree_info(node):
    if node is None:
        return Node_Info(0, 0)

    left_subtree_info = calc_tree_info(node.left)
    right_subtree_info = calc_tree_info(node.right)

    longest_path_through_node = left_subtree_info.height + right_subtree_info.height
    current_max_diameter = max(
        left_subtree_info.diameter, right_subtree_info.diameter)

    current_diameter = max(longest_path_through_node, current_max_diameter)
    current_height = 1 + max(left_subtree_info.height,
                             right_subtree_info.height)

    return Node_Info(current_diameter, current_height)


class Node_Info:
    def __init__(self, height, diameter):
        self.diameter = diameter
        self.height = height
