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

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
#      a
#     / \
#    b   c
#   / \   \
#  d   e   f



def depth_first_iterative(root):
    stack = [root]
    
    while(stack):
        current = stack.pop()
        print(current.value)
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)

depth_first_iterative(a)



