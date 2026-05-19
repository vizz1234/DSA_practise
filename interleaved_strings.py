class Solution:
    def isInterleave(self, s1, s2, s3):
        # code here
        
        s1l, s2l, s3l = len(s1), len(s2), len(s3)
        
        if s1l + s2l != s3l:
            return False
        
        dp = [[False] * (s2l + 1) for _ in range(s1l + 1)]
        dp[0][0] = True
        
        for i in range(s1l + 1):
            for j in range(s2l + 1):
                
                if i > 0:
                    dp[i][j] |= dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                if j > 0:
                    dp[i][j] |= dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]

        return dp[s1l][s2l]

sol = Solution()
print(sol.isInterleave("aab", "axy", "aaxaby"))
