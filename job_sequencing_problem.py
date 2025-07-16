class Solution:
    def jobSequencing(self, deadline, profit):
        # code here
        dpZip = list(zip(deadline, profit))
        dpZip = sorted(dpZip, key = lambda x : -x[1])
        n = len(deadline)
        mD = max(deadline)
        parent = {i:i for i in range(mD + 1)}
        maxProfit = 0
        nJobs = 0
        
        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent[x] = y
            
        for i in range(n):
            timeUnit = find(dpZip[i][0])
            if timeUnit > 0:
                maxProfit += dpZip[i][1]
                union(timeUnit, timeUnit - 1)
                nJobs += 1
        
        return [nJobs, maxProfit]

sol = Solution()
print(sol.jobSequencing([11, 2, 5, 8, 11, 10, 1, 6, 3, 8, 10], [321, 62, 456, 394, 424, 22, 393, 87, 118, 384, 83]))