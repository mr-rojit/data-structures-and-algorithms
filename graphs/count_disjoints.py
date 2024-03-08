graph = {
    'a': ['b', 'c'],
    'b': ['a', 'c'],
    'c': ['a', 'b', 'd', 'e'],
    'd': ['c'],
    'e': ['c'],
    'f': ['g'],
    'g': ['f'],
    'h': ['i'],
    'i': ['h']
}

"""
3 Disconnected graphs (undirected)

    a----b      h
    |   /       :
    |  /        :
    | /         i
    c----d
    |
    |
    e
    

    f-----g
"""

def get_count(graph):
    pass


get_count(graph)