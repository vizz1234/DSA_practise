class Solution:
    def numIslands(self, grid):
        # code here
        if not grid:
            return 0
        
        def dfs(row, col):
            visited[row][col] = 1
            for dx, dy in actions:
                rowX, colY = row + dx, col + dy
                if 0 <= rowX < n and 0 <= colY < m:
                    if not visited[rowX][colY] and grid[rowX][colY] == 'L':
                        dfs(rowX, colY)
        
        n, m = len(grid), len(grid[0])
        visited = [[False] * m for _ in range(n)]
        nIslands = 0
        actions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
        
        for i in range(n):
            for j in range(m):
                
                if not visited[i][j] and grid[i][j] == 'L':
                    dfs(i, j)
                    nIslands += 1
        
        return nIslands
sol = Solution()
print(sol.numIslands([['L', 'L', 'L'], ['L', 'L', 'L'], ['L', 'L', 'L']]))