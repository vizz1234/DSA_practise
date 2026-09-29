from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:

        if n == 1:
            return [0]

        adj_list = [[] * n for _ in range(n)]
        degree = [0] * n

        for u, v in edges:

            adj_list[u].append(v)
            adj_list[v].append(u)
            
            degree[u] += 1
            degree[v] += 1
        
        leaves = deque([i for i in range(n) if degree[i] == 1])
        rem = n

        while rem > 2:

            rem -= len(leaves)

            for _ in range(len(leaves)):

                n = leaves.popleft()

                for neighbor in adj_list[n]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        leaves.append(neighbor)
        
        return list(leaves)

sol = Solution()
print(sol.findMinHeightTrees(4, [[1,0],[1,2],[1,3]]))
print(sol.findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]]))
print(sol.findMinHeightTrees(1, []))
