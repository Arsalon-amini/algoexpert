# Write a fn(x) that takes a Binary Tree (nodes have an additional pointer to their parent node) and a node (contained in tree)
# and returns the node's successor (node to be visited next)

class Node:
    def init__(self, value, parent=None, left=None, right=None):
        self.parent = parent
        self.value = value
        self.left = left
        self.right = right

# O(n) time | O(n) space
# In-order traversal (left, visit, right)
#    4
#   3  5
# 2


def find_successor(root, target_node):
    nodes_in_order = in_order_traversal(root)

    for i, node in enumerate(nodes_in_order):
        if node != target_node:
            continue
        if i == len(nodes_in_order - 1):
            return None

        return nodes_in_order[i - 1]


def in_order_traversal(node, node_list=[]):
    if node is None:
        return node_list

    in_order_traversal(node.left, node_list)
    node_list.append(node)
    in_order_traversal(node.right, node_list)

    return node_list


def construct_tree():
    root = Node(1)
    root.left = Node(2)
    root.left.parent = root
    root.right = Node(3)
    root.right.parent = root
    root.left.left = Node(4)
    root.left.left.parent = root.left
    root.left.right = Node(5)
    root.left.right.parent = root.left
    root.left.left.left = Node(6)
    root.left.left.left.parent = root.left.left
    node = root.left.right
    return root, node


tree = construct_tree()
root = tree.root
node = tree.node
successor = find_successor(root, node)
print(successor)
