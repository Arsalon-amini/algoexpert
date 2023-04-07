"""
Write a f(n) that takes a Binary Tree and returns if that tree is symmetrical.
A tree is symmetrical if left and right subtress are mirror images of eachother
"""

#         1
#     2       2
#   3   4   4   3
# 5  6         6  5

# left_subtree_node.left == right_subtree_node.right
# left_subtree_node.right == right_subtree_node.left

# edge cases
# _subtree. is None

# brainstorming ideas
# could have a class tree_info:
# is_symmetrical that is passed up recursive stack


# Iterative soln

# O(n) time | where n is number of nodes in tree
# O(h) space | where h is height of tree (stored in stack)

def symm_trees(root):
    left_stack = [root.left]
    right_stack = [root.right]

    while len(left_stack) > 0:
        right_subtree_node = right_stack.pop()
        left_subtree_node = left_stack.pop()

        if left_subtree_node is None and right_subtree_node is None:
            continue
        
        if left_subtree_node is None or right_subtree_node is None or left_subtree_node.value != right_subtree_node.value:
            return False 
        
        
        right_stack.append(right_subtree_node.right)
        right_stack.append(right_subtree_node.left)
        left_stack.append(left_subtree_node.left)
        left_stack.append(left_subtree_node.right)
        
    return True

# left_stack [564] 
# right_stack [564]