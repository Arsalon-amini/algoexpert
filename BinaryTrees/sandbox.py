# given two binary trees, merge them, if two nodes overlap sum the values

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

# Iterative Solution ~
# DFS - use a stack for visiting nodes in tree


def merge_bts(tree_one, tree_two):
    if tree_one is None:
        return tree_two

    stack_one = [tree_one]
    stack_two = [tree_two]

    while len(stack_one) > 0:
        tree_one_node = stack_one.pop()
        tree_two_node = stack_two.pop()

        # handle edge cases ~
        if tree_two_node is None:
            continue

        tree_one_node.value += tree_two_node.value

        if tree_one_node.left is None:
            tree_one_node.left = tree_two_node.left
        else:
            stack_one.append(tree_one_node.left)
            stack_two.append(tree_two_node.left)

        if tree_one_node.right is None:
            tree_one_node.right = tree_two_node.right
        else:
            stack_one.append(tree_one_node.right)
            stack_two.append(tree_two_node.right)

    return tree_one

# tree_one =
#      1
#   3     2
#  7  4

# tree_two =
#     1
#   5    9
# 2     7  6

# stack_one = [ ]
# stack_two = [ ]


# merged_tree =
#    2
#  8     11
# 9  4  7  6
