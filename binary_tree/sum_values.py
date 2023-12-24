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

def find_sum(node):
    
    if node == None:
        return 0
    
    left_value = find_sum(node.left)
    
    right_value = find_sum(node.right)

    sum = left_value + right_value + node.value
    return sum

print(find_sum(a)) 
