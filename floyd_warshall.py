
class Solution:
    def floydWarshall(self, dist):
        #Code here
        n = len(dist)
        inf = 10 ** 8
        for k in range(n):
            for i in range(n):
                if dist[i][k] == inf:
                    continue
                for j in range(n):
                    if dist[k][j] == inf:
                        continue
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

sol = Solution()
dist = [[0, 5, float('inf'), 10], [float('inf'), 0, 3, float('inf')], [float('inf'), float('inf'), 0, 1], [float('inf'), float('inf'), float('inf'), 0]]
sol.floydWarshall(dist)
print(dist[0][3])