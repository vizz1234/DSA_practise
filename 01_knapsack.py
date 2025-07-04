class Solution:
    def knapsack(self, W, val, wt):
        # code here
        n = len(wt)
        dp = [[0] * (W + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, W + 1):
                v = 0
                if wt[i - 1] <= j:
                    v = val[i - 1] + dp[i - 1][j - wt[i - 1]]

                dp[i][j] = max(dp[i - 1][j], v)
        
        return dp[n][W]

sol = Solution()
print(sol.knapsack(5, [1, 2, 3], [4, 5, 1]))