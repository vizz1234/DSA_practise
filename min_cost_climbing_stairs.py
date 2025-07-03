
class Solution:
    def minCostClimbingStairs(self, cost):
        #Write your code here
        n = len(cost)
        if n == 0 or n == 1:
            return 0
    
        dp = [1000] * (n + 1)
        
        dp[0] = cost[0]
        dp[1] = cost[1]
        cost.append(0)
        
        for i in range(2, n + 1):
            curCost = cost[i]
            dp[i] = min(dp[i - 1] + curCost, dp[i - 2] + curCost)
        
        return dp[n]

sol = Solution()
print(sol.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))