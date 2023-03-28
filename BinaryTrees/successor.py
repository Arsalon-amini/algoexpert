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
#     1
#   2   3
#  4 5
# 6


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


# O(h) time | O(1) space where h = height of tree 
#      1
#    2    3
#  4   5
# 6
def find_successor_optimal(tree, target_node):
    if target_node.right is not None:
        return get_left_most_node(target_node.right)
    
    return get_parent(target_node) 
     
def get_left_most_node(node):
    current_node = node
    while current_node.left is not None:
        current_node = current_node.left 
        
    return current_node

def get_parent(node):
    current_node = node
    while current_node.parent is not None and current_node.parent.right == current_node:
         current_node = node.parent
    return current_node.parent
    
        


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
