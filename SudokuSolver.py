class Solution:
    def solveSudoku(self, board):
        # Helper function to check if placing a number is valid
        def is_valid(num, row, col):
            # Check the row
            for i in range(9):
                if board[row][i] == num:
                    return False
            # Check the column
            for i in range(9):
                if board[i][col] == num:
                    return False
            # Check the 3x3 sub-box
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j] == num:
                        return False
            return True

        # Backtracking function to solve the Sudoku
        def solve():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for num in '123456789':
                            if is_valid(num, i, j):
                                board[i][j] = num
                                if solve():
                                    return True
                                board[i][j] = '.'  # Backtrack
                        return False  # No valid number found
            return True  # Solved

        solve()

# Example usage
board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

s = Solution()
s.solveSudoku(board)
for row in board:
    print(row)
