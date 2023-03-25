

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# O(n) time | O(h) space
def calc_node_depth_recursively(root, depth=0):
    if root is None:
        return 0

    return depth + calc_node_depth_recursively(root.left, depth + 1) + calc_node_depth_recursively(root.right, depth + 1)
