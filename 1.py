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