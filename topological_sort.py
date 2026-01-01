class Solution:
    def topoSort(self, V, edges):
        # Code here
        n = V
        indegree = [0] * n
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            indegree[v] += 1
        
        res = []
        queue = []
        
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        
        front = 0
        while front < len(queue):
            top = queue[front]
            front += 1
            res.append(top)
            for v in adj[top]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
        
        return res
sol = Solution()
print(sol.topoSort(5, [[0, 1], [0, 2], [1, 3], [1, 4], [2, 3], [2, 4]]))