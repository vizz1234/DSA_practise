class Solution:
    def isBridge(self, V, edges, c, d):
        # code here 
        def bfs(start):
            queue = [start]
            front = 0
            tv = 0
            visited = [False] * V
            visited[start] = True
            while front < len(queue):
                top = queue[front]
                front += 1
                tv += 1
                for v in adj[top]:
                    if visited[v] == False:
                        queue.append(v)
                        visited[v] = True
            return tv
    
        adj = [[] for _ in range(V)]
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        tv1 = bfs(c)
        adj[c].remove(d)
        adj[d].remove(c)
        tv2 = bfs(c)

        

        
        return tv1 != tv2

sol = Solution()
print(sol.isBridge(4, [[0, 1], [1, 2], [2, 3]], 0, 1))