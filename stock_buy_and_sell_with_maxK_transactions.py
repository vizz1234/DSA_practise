import heapq
class Solution:
    def maxProfit(self, prices, k):
        # code here
        if not prices or k == 0:
            return 0
        
        n = len(prices)
        
        if k > n // 2:
            profit = 0
            for i in range(n - 1):
                if prices[i + 1] > prices[i]:
                    profit += prices[i + 1] - prices[i]
            
            return profit
        
        dp = [[0] * n for _ in range(k + 1)]
        
        for t in range(1, k + 1):
            max_diff = -prices[0]
            for d in range(1, n):
                dp[t][d] = max(dp[t][d - 1], prices[d] + max_diff)
                max_diff = max(max_diff, dp[t - 1][d] - prices[d])
        
        return dp[k][n - 1]

sol = Solution()
print(sol.maxProfit([10, 22, 5, 75, 65, 80], 2))