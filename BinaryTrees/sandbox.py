# write a fn, takes in a BT and returns list of branch sums leftmost to rightmost
# O(n) time | O(n) space


# fn_start (root) ~ kick off method
# init sums []
# fn(tree, currentSum, sums[]) ~ fn(root, 0, sums[])


# fn_rec (tree, currentSum, sums[])

# stop (leaf node) ~ if Node is None: return
# add to sums (parent to leaf) ~ add to sums ~ if Node.right is None and Node.left is None: sums.append(currentSum)

# recursive calls ~
# fn(tree.left, currentSum, sums[])
# fn(tree.right, currentSum, sums[])

def branch_sums(root):
    sums = []
    calc_branch_sums(root, 0, sums)
    return sums


def calc_branch_sums(node, current_running_sum, sums[]):
    if node is None:
        return

    new_current_running_sum = node.value + current_running_sum

    if node.left is None and node.right is None:
        sums.append(new_current_running_sum)
        return 

    calc_branch_sums(node.left, new_current_running_sum, sums)
    calc_branch_sums(node.right, new_current_running_sum, sums)
