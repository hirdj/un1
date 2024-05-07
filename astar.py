import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Distance from start node to current node
        self.h = 0  # Heuristic distance from current node to end node
        self.f = 0  # Total cost (g + h)

    def __lt__(self, other):
        return self.f < other.f

def heuristic(current, goal):
    # Manhattan distance heuristic
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

def astar(maze, start, end):
    open_list = []
    closed_list = set()

    start_node = Node(start)
    end_node = Node(end)

    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.position == end_node.position:
            path = []
            while current_node is not None:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        closed_list.add(current_node.position)

        for next_move in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            node_position = (current_node.position[0] + next_move[0], current_node.position[1] + next_move[1])

            if node_position[0] < 0 or node_position[0] >= len(maze) or \
               node_position[1] < 0 or node_position[1] >= len(maze[0]) or \
               maze[node_position[0]][node_position[1]] == 1:
                continue

            neighbor_node = Node(node_position, current_node)

            if neighbor_node.position in closed_list:
                continue

            neighbor_node.g = current_node.g + 1
            neighbor_node.h = heuristic(neighbor_node.position, end_node.position)
            neighbor_node.f = neighbor_node.g + neighbor_node.h

            if any(neighbor_node.position == node.position and neighbor_node.f >= node.f for node in open_list):
                continue

            heapq.heappush(open_list, neighbor_node)

    return None

# Example usage
maze = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0]
]
start = (0, 0)
end = (4, 4)
path = astar(maze, start, end)
print(path)