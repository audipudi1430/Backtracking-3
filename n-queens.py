# - This solution uses backtracking to place queens row by row, validating each position to avoid conflicts along columns and diagonals.
# - A boolean board is used to track queen placement, and a helper function builds the board representation for valid configurations.
# - Time Complexity: O(N!), Space Complexity: O(N^2) for the board and recursion stack (where N is the size of the board).

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [[False for _ in range(n)] for _ in range(n)]

        def isValid(board, i, j, n):
            r = i
            c = j

            # Check vertical column
            while r >= 0:
                if board[r][c]:
                    return False
                r -= 1

            # Check left diagonal
            r = i
            c = j
            while r >= 0 and c >= 0:
                if board[r][c]:
                    return False
                r -= 1
                c -= 1

            # Check right diagonal
            r = i
            c = j
            while r >= 0 and c < n:
                if board[r][c]:
                    return False
                r -= 1
                c += 1

            return True

        def helper(board, row, n):
            if row == n:
                solution = []
                for i in range(n):
                    temp = ''
                    for j in range(n):
                        temp += 'Q' if board[i][j] else '.'
                    solution.append(temp)
                result.append(solution)
                return

            for j in range(n):
                if isValid(board, row, j, n):
                    board[row][j] = True
                    helper(board, row + 1, n)
                    board[row][j] = False

        helper(board, 0, n)
        return result
