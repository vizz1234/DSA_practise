from collections import deque, defaultdict
class Solution:
    def isBipartite(self, V, edges):
        # code here
        adj_list = defaultdict(list)
        
        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)
        
        visited = set()
        color = [-1] * V
        
        for i in range(V):
            if color[i] != -1:
                continue
            queue = deque([i])
            color[i] = 0
            while queue:
                n = queue.popleft()
                for v in adj_list[n]:
                    if color[v] == -1:
                        color[v] = 1 - color[n]
                        queue.append(v)
                    elif color[v] == color[n]:
                        return False
        return True
sol = Solution()
print(sol.isBipartite(4, [[0,1],[1,2],[2,3],[3,0]]))
