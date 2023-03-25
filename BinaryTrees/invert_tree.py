# invert tree ~ iterative approach ~ breadth first search using queue
#     3
#   4    5
# 2  3  6  7

# queue = []
# [3]
# while queue > 0 (not empty):
# pop element (first)
# swap_helper_fn ()
# add node.left, node.right to queue

# example
# [3] add to queue
# swap children
# [5, 4] added to queue
# pop off [5]
# swap children
# add 5.left, 5.right to queue [4, 7, 6]
# pop off 4
# swap children
# add 4.left, 5.right to queue [7, 6, 3, 2]

# Big O - O(n) time, O(n) space storing nodes = n on queue

def invert(tree):
    queue = []
    queue.append(tree)

    while len(queue):
        queue.pop(0)
        if tree is None:
            continue

        swap_left_right_subtrees(tree)
        queue.append(tree.left)
        queue.append(tree.right)


def swap_left_right_subtrees(node):
    temp = node.left
    node.left = node.right
    node.right = temp


# Recursive solution
# write a function that takes a BT and inverts it. f(n) should swap every left node in tree for corresponding right
# O(n) time | O(h) space where h is height of deepest branch

#      3
#   2     4
# 4  5   4  6

# Recursive approach - depth first traversal
# fn_recursive (tree)
    # base case - if node is None: return
    # swap_left_right_subtrees(tree)
    # fn_recursive(tree.left)
    # fn_recursive(tree.right)


# helper fn - swap_left_right_subtrees (tree): return tree

def invert_tree(root):
    if root is None:
        return
    swap_left_right_subtrees(root)
    invert_tree(root.left)
    invert_tree(root.right)


def swap_left_right_subtrees(node):
    temp = node.left
    node.left = node.right
    node.right = temp
