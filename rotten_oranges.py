from collections import deque
class Solution:
    def orangesRotting(self, mat):
        #Code here
        n = len(mat)
        m = len(mat[0])
        q = deque()
        fresh = 0
        
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 2:
                    q.append((i, j, 0))
                elif mat[i][j] == 1:
                    fresh += 1
        
        time = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while q:
            
            i, j, t = q.popleft()
            time = max(time, t)
            
            for dx, dy in directions:
                di, dj = dx + i, dy + j
                if 0 <= di < n and 0 <= dj < m and mat[di][dj] == 1:
                    mat[di][dj] = 2
                    fresh -= 1
                    q.append((di, dj, t + 1))
        
        if fresh == 0:
            return time
        else:
            return -1
