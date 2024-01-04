"""
Question : Given a Binary Tree. Return
true if, for every node X in the tree other than the leaves,
its value is equal to the sum of its left subtree's 
value and its right subtree's value. Else return false.
An empty tree is also a Sum Tree as the sum of an empty tree can
be considered to be 0. A leaf node is also considered a Sum Tree.

Input:
    3
  /   \    
 1     2

Output: 1
Explanation:
The sum of left subtree and right subtree is
1 + 2 = 3, which is the value of the root node.
Therefore,the given binary tree is a sum tree.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

a = Node(3)
b = Node(2)
c = Node(4)
d = Node(1)
e = Node(4)
f = Node(3)
g = Node(7)

#        50
#       / \
#      20  30
#     / \ 
#    10  10
