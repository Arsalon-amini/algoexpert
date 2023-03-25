# take in a binary tree and returns a list of its branch sums ordered leftomost branch sum to rightmost branch sum
# O(n) time ~ traversing every node, only doing O(1) calculations at each node
# O(n) space ~ recursive call stack 

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None 
        
def branch_sums(root):
    sums = []
    calculate_branch_sums(root, 0, sums)
    return sums 
    
    
def calculate_branch_sums(node, running_sum, sums):
    if node is None:
        return
    
    new_running_sum = running_sum + node.value 
    
    if node.left is None and node.right is None:
        sums.append(new_running_sum)
        return
    
    calculate_branch_sums(node.left, new_running_sum, sums)
    calculate_branch_sums(node.right, new_running_sum, sums)

  