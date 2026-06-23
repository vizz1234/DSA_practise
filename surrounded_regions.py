from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        if not board or not board[0]:
            return
        
        m, n = len(board), len(board[0])

        def dfs(r, c):

            if r < 0 or r >= m or c < 0 or c >= n:
                return

            if board[r][c] != 'O':
                return
            
            board[r][c] = 'S'
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
            
        for i in (0, m - 1):
            for j in range(n):
                if board[i][j] == 'O':
                    dfs(i, j)
        
        for i in range(m):
            for j in (0, n - 1):
                if board[i][j] == 'O':
                    dfs(i, j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'S':
                    board[i][j] = 'O'
        
        return board

sol = Solution()
print(sol.solve([['X','X','X','X'],['X','O','O','X'],['X','X','O','X'],['X','O','X','X']]))
