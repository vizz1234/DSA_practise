from collections import defaultdict
class Solution:
    def getComponents(self, V, edges):
        # code here
        adj_list = defaultdict(list)
        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)
        
        
        visited = set()
        not_visited = set([i for i in range(V)])
        result = []
        
        def dfs(node, cur_res):
            if node in visited:
                return
            visited.add(node)
            not_visited.remove(node)
            cur_res.append(node)
            
            for n in adj_list[node]:
                dfs(n, cur_res)
            
            return cur_res
                
        
        while len(visited) < V:
            v = next(iter(not_visited))
            result.append(dfs(v, []))
        
        return result

sol = Solution()
print(sol.getComponents(5, [[0,1],[1,2],[3,4]]))
