# write a fn that takes a BT and returns sum of its node depths
# O(n) time | o(h) where h = height of tree

# sum = 9

#    2 | d = 0
#  3   5 | d = 1
# 4 5  6 9 | d = 2

# recursive
# fn_recursive (root, depth)
# base case ~ if node is none, return
# sum_depths = depth + fn_recursive(root.left, depth + 1) + fn_recursive(root.right, dpeth + 1)

def node_depths(root, depth):
    if root is None:
        return 0
    depth_sum = depth + \
        node_depths(root.left, depth + 1) + node_depths(root.right, depth + 1)

    return depth_sum
