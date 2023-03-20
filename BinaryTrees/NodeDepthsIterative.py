class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def calc_node_depths_iterative(root):
    sum_of_depths = 0
    stack = [{"node": root, "depth": 0}]
    while len(stack) > 0:
        node_info = stack.pop()
        node, depth = node_info["node"], node_info["depth"]
        if node is None:
            continue
        sum_of_depths += depth
        stack.append({"node": node.left, "depth": depth + 1})
        stack.append({"node": node.left, "depth": depth + 1})
    return sum_of_depths
