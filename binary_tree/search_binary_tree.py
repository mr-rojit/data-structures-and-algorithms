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

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
d.left = g
#        a
#       / \
#      b   c
#     / \   \
#    d   e   f
#   /
#  g


def search(root, target):
    stack = [root]
    
    while(stack):
        current = stack.pop()
        if current.value == target:
            return True
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
    return False

print(search(a, 'e'))
print(search(a, 'z'))
