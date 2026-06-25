class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 3 or dp[i+1][j-1]):
                    dp[i][j] = True
        
        min_cuts = [float('inf')] * n

        for i in range(n):
            if dp[0][i]:
                min_cuts[i] = 0
            else:
                for j in range(1, i + 1):
                    if dp[j][i]:
                        min_cuts[i] = min(min_cuts[i], min_cuts[j-1] + 1)
        
        return min_cuts[n - 1]


sol = Solution()
print(sol.minCut("aab"))