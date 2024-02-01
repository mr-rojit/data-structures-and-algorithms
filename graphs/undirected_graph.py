graph = {
    'a': ['b', 'c'],
    'b': ['a', 'c'],
    'c': ['a', 'b', 'd', 'e'],
    'd': ['c'],
    'e': ['c'],
    'f': ['g'],
    'g': ['f']
}

"""
    a----b
    |   / 
    |  /
    | /
    c----d
    |
    |
    e

    f-----g

"""
def traverse(root, graph, visited=set()):
    for node in graph[root]:
        if not node in visited:
            print(node)
            visited.add(node)
            traverse(node, graph, visited)

# traverse('f', graph)

def has_path(graph, src, dest, visited=set()):
    if src == dest:
        return True

    for node in graph[src]:
        if node not in visited:
            visited.add(node)
            if has_path(graph, node, dest, visited):
                return True
    return False


print(has_path(graph, 'a', 'f'))

        




