class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(t)
        dp = [1] + [0] * n
        for ch in s:
            for i in range(n, 0, -1):
                if t[i - 1] == ch:
                    dp[i] += dp[i - 1]
        return dp[n]

sol = Solution()
print(sol.numDistinct("rabbbit", "rabbit"))