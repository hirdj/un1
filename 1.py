# def dfs(graph, start):
#     visited = set()
#     traversal_order = []

#     def dfs_helper(node):
#         visited.add(node)
#         traversal_order.append(node)
#         for neighbor in graph[node]:
#             if neighbor not in visited:
#                 dfs_helper(neighbor)

#     dfs_helper(start)
#     return traversal_order

# # Example usage:
# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F'],
#     'D': [],
#     'E': ['F'],
#     'F': []
# }

# print("Depth-First Traversal:", dfs(graph, 'A'))



from collections import deque

def bfs(graph, start):
    visited = set()
    traversal_order = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            traversal_order.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return traversal_order

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("Breadth-First Traversal:", bfs(graph, 'A'))



# def recursive_bfs(graph, start):
#     visited = set()
#     traversal_order = []

#     def bfs_helper(node):
#         visited.add(node)
#         traversal_order.append(node)
#         for neighbor in graph[node]:
#             if neighbor not in visited:
#                 bfs_helper(neighbor)

#     bfs_helper(start)
#     return traversal_order

# # Example usage:
# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F'],
#     'D': [],
#     'E': ['F'],
#     'F': []
# }

# print("Recursive Breadth-First Traversal:", recursive_bfs(graph, 'A'))


##########################################################################################################################
switch case driven code
from collections import deque

def dfs(graph, start):
    visited = set()
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")
        for neighbor in graph[vertex] - visited:
            visited.add(neighbor)
            queue.append(neighbor)

def switch_case(choice, graph, start):
    switcher = {
        'dfs': dfs,
        'bfs': bfs
    }
    # Get the function from switcher dictionary
    func = switcher.get(choice.lower())
    # Execute the function
    if func:
        func(graph, start)
    else:
        print("Invalid choice")

# Example usage
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}
start_vertex = 'A'
choice = input("Enter 'dfs' for Depth-First Search or 'bfs' for Breadth-First Search: ")
switch_case(choice, graph, start_vertex)




