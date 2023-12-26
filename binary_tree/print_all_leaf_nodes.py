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

def print_leaf(root):
    stack = [root]
    while stack:
        current = stack.pop()
        if not current.left and not current.right:
            print(current.value)
        else:
            if current.left:
                stack.append(current.left)
            
            if current.right:
                stack.append(current.right)

print_leaf(a)