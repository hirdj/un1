# Selection Sort:
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Example usage:
arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)



#Minimum Spanning Tree (Prim's Algorithm):
import heapq

def prim_mst(graph):
    mst = []
    visited = set()
    start_node = list(graph.keys())[0]  # Choosing any starting node
    visited.add(start_node)
    edges = [(cost, start_node, to) for to, cost in graph[start_node]]
    heapq.heapify(edges)

    while edges:
        cost, from_node, to_node = heapq.heappop(edges)
        if to_node not in visited:
            visited.add(to_node)
            mst.append((from_node, to_node, cost))
            for to, cost in graph[to_node]:
                if to not in visited:
                    heapq.heappush(edges, (cost, to_node, to))
    
    return mst

# Example usage:
graph = {
    'A': [('B', 10), ('C', 5)],
    'B': [('A', 10), ('C', 2), ('D', 4)],
    'C': [('A', 5), ('B', 2), ('D', 3)],
    'D': [('B', 4), ('C', 3)]
}
minimum_spanning_tree = prim_mst(graph)
print("Minimum Spanning Tree:", minimum_spanning_tree)

# Job Scheduling Problem:
def job_scheduling(jobs):
    jobs.sort(key=lambda x: x[1])  # Sort jobs by finish time
    schedule = []
    last_finish_time = 0
    for job in jobs:
        start_time, finish_time = job
        if start_time >= last_finish_time:
            schedule.append(job)
            last_finish_time = finish_time
    return schedule

# Example usage:
jobs = [(1, 3), (2, 5), (3, 6), (4, 7)]
schedule = job_scheduling(jobs)
print("Job Schedule:", schedule)

# Kruskal's Minimal Spanning Tree Algorithm:
class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)

def kruskal_mst(graph):
    mst = []
    edges = [(cost, from_node, to_node) for from_node, to_edges in graph.items() for to_node, cost in to_edges]
    edges.sort()

    disjoint_set = DisjointSet(len(graph))

    for cost, from_node, to_node in edges:
        if disjoint_set.find(from_node) != disjoint_set.find(to_node):
            mst.append((from_node, to_node, cost))
            disjoint_set.union(from_node, to_node)
    
    return mst

# Example usage:
graph = {
    'A': [('B', 10), ('C', 5)],
    'B': [('A', 10), ('C', 2), ('D', 4)],
    'C': [('A', 5), ('B', 2), ('D', 3)],
    'D': [('B', 4), ('C', 3)]
}
minimum_spanning_tree_kruskal = kruskal_mst(graph)
print("Minimum Spanning Tree (Kruskal):", minimum_spanning_tree_kruskal)
