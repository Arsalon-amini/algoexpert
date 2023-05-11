'''
Given the head of a singly linked list whose nodes are in sorted order with respect to their values.
Write a fn that returns a modified version of the LL that doesn't contain any duplicate nodes. Modify in place

Input: 1 -> 1 -> 3 -> 4 -> 4 -> 5 -> 6 -> 6
Output: 1 -> 3 -> 4 -> 5 -> 6

O(n) time | O(1) space

'''


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# Input: 1 -> 1 -> 3 -> 4 -> 4 -> 5 -> 6 -> 6
# CN                     ^
# NDN                              ^^
# current_node = ^
# next_distinct_node = ^^


def remove_duplicates(head):
    current_node = head

    while current_node is not None:
        next_distinct_node = current_node.next
        while next_distinct_node is not None and next_distinct_node.value == current_node.value:
            next_distinct_node = next_distinct_node.next

        current_node.next = next_distinct_node
        current_node = next_distinct_node

    return head


'''
TESTING 

ARRANGE: 
sixth_node = LinkedList(5, None)
fifth_node = LinkedList(4, sixth_node)
fourth_node = LinkedList(4, fifth_node)
third_node = LinkedList(3, fourth_node)
second_node = LinkedList(1, third_node)
head = LinkedList(1, second_node)


ASSERT:



EXPECT: 

'''
