# N-Queens Problem

n = int(input("Enter the value of N: "))

board = [["." for _ in range(n)] for _ in range(n)]
solutions = 0


def is_safe(row, col):
    # Check column
    for i in range(row):
        if board[i][col] == "Q":
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1

    return True


def solve(row):
    global solutions

    # All queens are placed
    if row == n:
        solutions += 1

        print("\nSolution", solutions)

        for r in board:
            print(" ".join(r))

        return

    # Try every column
    for col in range(n):

        if is_safe(row, col):
            board[row][col] = "Q"

            solve(row + 1)

            # Backtracking
            board[row][col] = "."


# Start solving
solve(0)

print("\nTotal number of possible solutions:", solutions)