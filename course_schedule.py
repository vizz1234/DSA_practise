from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        state = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for course, prerequisite in prerequisites:
            adj[prerequisite].append(course)

        def dfs(node):

            state[node] = 1

            for neighbor in adj[node]:
                if state[neighbor] == 1:
                    return True
                elif state[neighbor] == 0 and dfs(neighbor):
                    return True
            
            state[node] = 2
            return False
        
        for i in range(numCourses):

            if state[i] == 0:

                if dfs(i):
                    return False
        
        return True

sol = Solution()
print(sol.canFinish(numCourses = 2, prerequisites = [[1,0]]))
print(sol.canFinish(numCourses = 2, prerequisites = [[1,0], [0,1]]))

        