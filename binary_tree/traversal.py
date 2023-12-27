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

def inorder_traversal(root):
    """
    Left, Node, Right
    """
    if not root:
        return
    
    inorder_traversal(root.left)
    print(root.value)
    inorder_traversal(root.right)

def preorder_traversal(root):
    """
    Node, Left, Right
    """
    if not root:
        return
    
    print(root.value)
    preorder_traversal(root.left)
    preorder_traversal(root.right)


def postorder_traversal(root):
    """
    Left, Right, Node
    """
    if not root:
        return
    
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.value)

print("POST ORDER")
postorder_traversal(a)
