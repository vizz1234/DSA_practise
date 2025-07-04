class Solution:
    def minCoins(self, coins, sum):
        dp = [float('inf')] * (sum + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, sum + 1):
                if dp[i - coin] != float('inf'):
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        if dp[sum] == float('inf'):
            return -1

        return dp[sum]


sol = Solution()
print(sol.minCoins([1, 2, 3], 4))