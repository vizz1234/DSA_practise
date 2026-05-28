from collections import defaultdict, deque
class Solution:
    def findOrder(self, n, prerequisites):
        # code here 
        adj_list = defaultdict(list)
        indegree = [0] * n
        
        for x, y in prerequisites:
            adj_list[y].append(x)
            indegree[x] += 1
        
        queue = deque()
        
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        
        result = []
        while queue:
            e = queue.popleft()
            result.append(e)
            
            for i in adj_list[e]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
        
        return result if len(result) == n else []

sol = Solution()
print(sol.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))