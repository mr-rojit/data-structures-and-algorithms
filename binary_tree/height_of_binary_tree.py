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


def find_height(root):
    if root == None:
        return 0
    left_height = find_height(root.left)
    right_height = find_height(root.right)
    return max(left_height, right_height) + 1

print(find_height(a))
