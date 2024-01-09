graph = {
    'a': ['b', 'c'],
    'b': ['d', 'g'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': [],
    'g': [],
    'h': ['f']
}

"""
    a----->c
    |      |
g<--b      e
    |
    d----->f<----h
"""


def has_path(graph, src, dest):
    if src == dest:
        return True
    for neighbour in graph[src]:
        if has_path(graph, neighbour, dest):
            return True
    return False

print(has_path(graph, 'b', 'e'))