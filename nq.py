class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [[0] * n for _ in range(n)]
        self.solution_count = 0

    def is_safe(self, row, col):
        for i in range(col):
            if self.board[row][i] == 1:
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False
        for i, j in zip(range(row, self.n, 1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False
        return True

    def solve_backtracking(self, col):
        if col >= self.n:
            self.print_solution()
            self.solution_count += 1
            return True

        for i in range(self.n):
            if self.is_safe(i, col):
                self.board[i][col] = 1
                self.solve_backtracking(col + 1)
                self.board[i][col] = 0
        return False

    def solve_branch_and_bound(self, col):
        if col >= self.n:
            self.print_solution()
            self.solution_count += 1
            return True

        for i in range(self.n):
            if self.is_safe(i, col):
                self.board[i][col] = 1
                if self.solve_branch_and_bound(col + 1):
                    return True
                self.board[i][col] = 0
        return False

    def print_solution(self):
        print("Solution", self.solution_count)
        for i in range(self.n):
            for j in range(self.n):
                print(self.board[i][j], end=" ")
            print()
        print()


print("Backtracking Solutions:")
nq_backtracking = NQueens(4)
nq_backtracking.solve_backtracking(0)

print("\nBranch and Bound Solutions:")
nq_branch_and_bound = NQueens(4)
nq_branch_and_bound.solve_branch_and_bound(0)