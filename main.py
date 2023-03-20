from BinaryTrees import *

root = BinaryTree(1)
root.left = BinaryTree(2)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)
root.left.left.left = BinaryTree(8)
root.left.left.right = BinaryTree(9)

root.right = BinaryTree(3)
root.right.left = BinaryTree(6)
root.right.right = BinaryTree(7)

print(calc_depth(root))
