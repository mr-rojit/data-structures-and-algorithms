"""
Given a binary tree, find if it is height balanced or not. 
A tree is height balanced if difference between heights of left and right subtrees is not more than one for all nodes of tree. 

A height balanced tree
        1
     /     \
   10      39
  /
5

An unbalanced tree
        1
     /    
   10   
  /
5
"""



class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')

a.left = b
a.right = c
b.left = d
d.left = e

#        a
#       / \
#      b   c
#     / 
#    d      
#   /
#  e


def check_balanced(root):
    if not root:
        return 0
    
    left = check_balanced(root.left)
    right = check_balanced(root.right)

    d = left


    

