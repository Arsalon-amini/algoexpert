# breadth-first search iteratively using a queue
# O(n) time, O(h) space 

#iterative solution 

def invert_tree(root):
    queue = [root]
    while len(queue):
        current = queue.pop(0)

        if current is None:
            continue

        swap_nodes(current)
        queue.append(current.left)
        queue.append(current.right)


def swap_nodes(node):
    temp = node.left
    node.left = node.right
    node.right = temp


# Recursive solution 
def invert_binary_tree(node):
    if node is None:
        return
    swap_nodes(node)
    invert_binary_tree(node.left)
    invert_binary_tree(node.right) 