class Solution:
    def articulationPoints(self, V, edges):
        # Build adjacency list
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        tin = [-1] * V
        low = [-1] * V
        visited = [False] * V
        isAP = [False] * V
        timer = 0
        
        def dfs(u, parent):
            nonlocal timer
            visited[u] = True
            tin[u] = low[u] = timer
            timer += 1
            
            children = 0  # DFS children count
            
            for v in adj[u]:
                if v == parent:
                    continue
                
                if not visited[v]:
                    dfs(v, u)
                    low[u] = min(low[u], low[v])
                    
                    # Case 1: non-root
                    if parent != -1 and low[v] >= tin[u]:
                        isAP[u] = True
                    
                    children += 1
                else:
                    # Back edge
                    low[u] = min(low[u], tin[v])
            
            # Case 2: root
            if parent == -1 and children > 1:
                isAP[u] = True
        
        # Graph may be disconnected
        for i in range(V):
            if not visited[i]:
                dfs(i, -1)
        
        result = [i for i in range(V) if isAP[i]]
        return result if result else [-1]
sol = Solution()
print(sol.articulationPoints(5, [[0, 1], [0, 2], [1, 3], [1, 4], [2, 3], [2, 4]]))