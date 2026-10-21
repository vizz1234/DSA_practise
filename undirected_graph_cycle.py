class Solution:
    def isCycle(self, V, edges):
        #Code here
        parent = {i:i for i in range(V)}
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent[x] = y
        
        for u, v in edges:
            rootU = find(u)
            rootV = find(v)
            if rootU == rootV:
                return True
            union(rootU, rootV)
        
        return False

sol = Solution()
print(sol.isCycle(5, [[0,1],[1,2],[2,3],[3,4],[4,0],[0,4]]))
print(sol.isCycle(3, [[0,1],[1,2],[2,0]]))
print(sol.isCycle(3, [[0,1],[1,2]]))
print(sol.isCycle(3, [[0,1],[1,2],[2,1]]))
print(sol.isCycle(1, []))
print(sol.isCycle(4, [[0,1],[1,2],[2,3]]))