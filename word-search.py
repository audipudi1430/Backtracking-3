# - This backtracking approach uses DFS to explore all paths starting from each cell, checking if the target word can be formed.
# - A set is used to track visited cells during each path exploration to prevent revisiting.
# - Time Complexity: O(N * 3^L), Space Complexity: O(L) where N is number of cells and L is the length of the word.

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                word[i] != board[r][c] or
                (r, c) in visited
            ):
                return False

            visited.add((r, c))
            res = (
                dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1)
            )
            visited.remove((r, c))
            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False
