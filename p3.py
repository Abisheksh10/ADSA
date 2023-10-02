def solve_n_queens(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i][col] == 'Q':
                return False

        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False

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


n = int(input("Enter the row or column size of theess board:"))
solutions = solve_n_queens(n)
print("Various Solutions Possible:")
i=1
for solution in solutions:
    print("Solution {}:".format(i))
    i+=1
    for row in solution:
        print(" ".join(row))
    print()
print("""
Backtracking Approach for N-Queens:

The backtracking approach for solving the N-Queens problem involves trying out different possibilities 
      and, when a conflict is encountered, backtracking to explore alternative choices. Here's how it
       works:

- Solution Generation: The goal is to place N queens on an NXN chessboard in such a way that no two queens
       threaten each other. The algorithm generates solutions incrementally by placing queens one by one in
       different rows while ensuring that they do not conflict with each other.

- Validation (is_safe function): Before placing a queen in a particular cell, we need to validate whether
       it's safe to do so. The `is_safe` function checks three conditions:
  1. No queen in the same column as the current cell.
  2. No queen in the upper-left diagonal.
  3. No queen in the upper-right diagonal.

- Conflict Resolution: If it's safe to place a queen in a cell, we mark that cell as 'Q' and move on to 
      the next row. If at any point we find that it's not possible to place a queen in any cell of the 
      current row without violating the safety conditions, we backtrack. Backtracking means going back to 
      the previous row and exploring a different column to place the queen.

Time Complexity and Performance:

- In the worst case, where all possible solutions are generated, the time complexity is exponential, 
      approximately O(N!).
- On average, the backtracking algorithm prunes many possibilities early on, reducing the search space. 
      In such cases, the time complexity can be closer to O(N^N).

The performance for larger N values deteriorates rapidly due to the exponential nature of the problem. 
      For small N (e.g., N = 8 or N = 10), the algorithm can find solutions relatively quickly. However,
       as N increases, the time it takes to find solutions grows significantly.

""")
