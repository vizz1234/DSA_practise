class Solution:
    def bellmanFord(self, V, edges, src):
        #code here
        inf = 10 ** 8
        dist = [inf] * V
        dist[src] = 0
        for _ in range(V - 1):
            updated = False
            for u, v, w in edges:
                if dist[u] != inf and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    updated = True
            if not updated:
                break
        for u, v, w in edges:
            if dist[u] != inf and dist[u] + w < dist[v]:
                return [-1]
        return dist
sol = Solution()
print(sol.bellmanFord(3, [[0, 1, 5], [1, 2, -3], [2, 0, 1]], 0))