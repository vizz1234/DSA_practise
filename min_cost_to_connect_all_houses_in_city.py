class Solution:
    def minCost(self, houses):
      # code here
        n = len(houses)
        minDist = [float('inf')] * n
        visited = [False] * n
        minDist[0] = 0
        total_cost = 0
        for _ in range(n):
            u = -1
            for i in range(n):
                if not visited[i] and (u == -1 or minDist[i] < minDist[u]):
                    u = i
            visited[u] = True
            total_cost += minDist[u]
            
            x1, y1 = houses[u]
            for v in range(n):
                if not visited[v]:
                    x2, y2 = houses[v]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    minDist[v] = min(minDist[v], dist)
        return total_cost
sol = Solution()
print(sol.minCost([[0, 0], [1, 1], [1, 0], [0, 1]]))