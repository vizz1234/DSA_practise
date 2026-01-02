class Solution:
    def isCyclic(self, V, edges):
        # code here
        front = 0
        adj = [[] for _ in range(V)]
        indegree = [0] * V
        res = []
        queue = []
        
        for u, v in edges:
            adj[u].append(v)
            indegree[v] += 1
        
        for i in range(V):
            if indegree[i] == 0:
                queue.append(i)
        
        while front < len(queue):
            top = queue[front]
            front += 1
            for v in adj[top]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
        
        return front != V