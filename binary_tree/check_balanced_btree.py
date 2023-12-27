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
f = Node('f')
g = Node('g')
h = Node('h')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
d.left = g
d.right = h
#        a
#       / \
#      b   c
#     / \   \
#    d   e   f
#   / \
#  g   h


def check_balanced(root):
    pass

