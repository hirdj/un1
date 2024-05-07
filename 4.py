# Here's a simple implementation of the Graph Coloring problem using a Backtracking algorithm in Python:
# python
def is_safe(graph, color, v, c, n):
    for i in range(n):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True

def graph_coloring(graph, m, n):
    color = [-1] * n

    def backtrack(v):
        if v == n:
            print_solution(color)
            return True

        for c in range(m):
            if is_safe(graph, color, v, c, n):
                color[v] = c
                if backtrack(v + 1):
                    return True
                color[v] = -1

        return False

    backtrack(0)

def print_solution(color):
    print("Solution found:")
    for c in color:
        print(c, end=" ")
    print()

# Example usage
graph = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
graph_coloring(graph, 3, 4)




######################################################################################################################################################
# for n queen problem
class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [-1] * n
        self.solution_count = 0

    def is_safe(self, row, col):
        for i in range(row):
            if self.board[i] == col or \
               self.board[i] - i == col - row or \
               self.board[i] + i == col + row:
                return False
        return True

    def solve_backtracking(self, row):
        if row == self.n:
            self.print_solution()
            self.solution_count += 1
            return

        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row] = col
                self.solve_backtracking(row + 1)
                self.board[row] = -1

    def solve_branch_and_bound(self, row):
        if row == self.n:
            self.print_solution()
            self.solution_count += 1
            return True

        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row] = col
                if self.solve_branch_and_bound(row + 1):
                    return True
                self.board[row] = -1
        return False

    def print_solution(self):
        print("Solution", self.solution_count)
        for row in range(self.n):
            line = ["0"] * self.n
            line[self.board[row]] = "1"
            print(" ".join(line))
        print()


# Example usage
print("Backtracking Solutions:")
nq_backtracking = NQueens(4)
nq_backtracking.solve_backtracking(0)

print("\nBranch and Bound Solutions:")
nq_branch_and_bound = NQueens(4)
nq_branch_and_bound.solve_branch_and_bound(0)
