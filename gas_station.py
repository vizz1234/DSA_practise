class Solution:
    def startStation(self, gas, cost):
        # Your code here
        n = len(gas)
        start = 0
        totalRem = 0
        curBal = 0
        
        for i in range(n):
            rem = gas[i] - cost[i]
            totalRem += rem
            curBal += rem
            
            
            if curBal < 0:
                start = i + 1
                curBal = 0
        
        if totalRem < 0:
            return -1
        
        else:
            return start

sol = Solution()
print(sol.startStation([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))