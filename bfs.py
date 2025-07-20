class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    def bfs(self, adj):
        # code here
        queue = [0]
        output = []
        outputSet = set()
        n = len(adj)
        front = 0
        
        while len(output) < n:
            
            currEle = queue[front]

            if currEle not in outputSet:
                output.append(currEle)
                outputSet.add(currEle)
                
            for i in range(len(adj[currEle])):
                if adj[currEle][i] not in outputSet:
                    queue.append(adj[currEle][i])
            
            front += 1
            
        return output

sol = Solution()
print(sol.bfs([[2, 3, 1], [0], [0, 4], [0], [2]]))