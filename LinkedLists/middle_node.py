'''
You're given a linked list with at least one node. 
Write a fn that returns the middle node of the LL, if there are two middle nodes (return the second)
Node (def) - value, next (none if tail)

Sol 1
two pointers (slow + fast) 
slow - iterate to end of list

iterate list leaving a pointer behind, each step forward, ensure pointer is in middle of current list, if not, update it
O(n) time
O(1) space
'''

def get_middle_node(linkedList):
    count = 0
    current_node = linkedList
    
    while current_node is not None:
        count += 1
        current_node = current_node.next
        
        middle_node = linkedList
        for _ in range(count // 2):
            middle_node = middle_node.next 
        
    return middle_node
        
        