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


middle = get_middle_node(head)
print(middle)
