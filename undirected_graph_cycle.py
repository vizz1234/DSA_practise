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