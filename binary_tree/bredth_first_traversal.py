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



def bredth_first_iterative(root):
    queue = [root]
    
    while(queue):
        current = queue.pop(0)
        print(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

bredth_first_iterative(a)



