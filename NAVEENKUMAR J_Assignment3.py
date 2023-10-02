#Assignment 3

#Done by NAVEENKUMAR J

'''You are tasked with solving the N-Queens problem using a backtracking algorithm.
The N-Queens problem is to place N chess queens on an N×N chessboard so that no two queens threaten each other.
Thus, a solution requires that no two queens share the same row, column, or diagonal.
Your goal is to implement the algorithm, find all possible solutions for a given N,
and analyze its time complexity.'''

def solve_N_queens(n):
    def is_safe(board, row, col):
        # Check if there is a queen in the same column
        for i in range(row):
            if board[i][col] == 'Q':
                return False

        # Check upper-left diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False

        # Check upper-right diagonal
        for i, j in zip(range(row, -1, -1), range(col, n)):
            if board[i][j] == 'Q':
                return False

        return True

    def solve(row):
        if row == n:
            solutions.append(["".join(row) for row in board])
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                solve(row + 1)
                board[row][col] = '.'

    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []
    solve(0)

    return solutions

def print_solutions_as_chessboards(solutions):
    for i, solution in enumerate(solutions):
        print(f"Solution {i + 1}:")
        for row in solution:
            print(row)
        print()

# Example usage with N = 16
N = 16
solutions = solve_N_queens(N)
