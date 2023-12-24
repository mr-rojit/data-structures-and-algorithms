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

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
d.left = g
#        3
#       / \
#      2   4
#     / \   \
#    1   4   3
#   /
#  7


def find_min_value(node):
    if node == None:
        return 999999 # treating it as max value, we can use sth like max_int
    left_value = find_min_value(node.left)
    right_value = find_min_value(node.right)

    return min(left_value, node.value, right_value)

print(find_min_value(a))
