graph = {
    'a': ['b', 'c'],
    'b': ['d', 'g'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': [],
    'g': []
}

"""
    a----->c
    |      |
g<--b      e
    |
    d----->f
"""

def depth_first_iterative(graph, source):
    stack = [source]

    while stack:
        current_node = stack.pop()
        print(current_node)
        for child in graph[current_node]:
            stack.append(child)

def depth_first_recursive(graph, source):
    print(source)
    for child in graph[source]:
        depth_first_recursive(graph, child)


def breadth_first_search(graph, source):
    queue = [source]
    while queue:
        current_node = queue.pop(0)
        print(current_node)
        for child in graph[current_node]:
            queue.append(child)



def menu():
    menu_str = \
"""
choose the folloing number for:
1. DFS Iterative
2. DFS Recursive
3. BFS
"""
    print(menu_str)


def main():
    menu()
    inp = int(input('Enter your choice: '))
    match inp:
        case 1:
            depth_first_iterative(graph=graph, source='a')
        case 2:
            depth_first_recursive(graph=graph, source='a')
        case 3:
            breadth_first_search(graph=graph, source='a')
        case _:
            depth_first_iterative(graph=graph, source='a')

if __name__ == '__main__':
    main()

