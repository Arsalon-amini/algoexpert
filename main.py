from LinkedLists import *


sixth_node = LinkedList(5)
fifth_node = LinkedList(4)
fourth_node = LinkedList(4)
third_node = LinkedList(3)
second_node = LinkedList(1)
head = LinkedList(1)

head.next = second_node
second_node.next = third_node
third_node.next = fourth_node
fourth_node.next = fifth_node
fifth_node.next = sixth_node


new_head = remove_duplicates(head)
print(new_head)
