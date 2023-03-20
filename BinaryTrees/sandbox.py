
# Iterative

def calc_depth(root):
    stack = [{"node": root, "depth": 0}]
    sum_of_depths = 0

    while len(stack) > 0:
        current_node = stack.pop()

        node, depth = current_node["node"], current_node["depth"]

        if node is None:
            continue

        sum_of_depths += depth
        stack.append({"node": node.left, "depth": depth + 1})
        stack.append({"node":  node.right, "depth": depth + 1})

    return sum_of_depths
