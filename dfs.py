class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfs(self, adj):
        # code here
        output = []
        outputSet = set()
        n = len(adj)
        stack = [0]
        
        while len(output) < n:
            top = stack[-1]
            if top not in outputSet:
                output.append(top)
                outputSet.add(top)
            i = 0
            while i < len(adj[top]):
                if adj[top][i] not in outputSet:
                    stack.append(adj[top][i])
                    break
                i += 1
            else:
                stack.pop()
        
        return output

sol = Solution()
print(sol.dfs([[2, 3, 1], [0], [0, 4], [0], [2]]))