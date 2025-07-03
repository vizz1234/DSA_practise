class Solution:
    def longestPalindrome(self, s):
        # code here
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        
        start = 0
        maxLen = 1
        curLen = 1
        
        for i in range(n - 1):
            dp[i][i] = True
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                curLen = 2
                if curLen > maxLen:
                    start = i
                    maxLen = curLen
        dp[n - 1][n - 1] = True
        
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    curLen = length
                    if curLen > maxLen:
                        start = i
                        maxLen = curLen
        
        return s[start : start + maxLen]

sol = Solution()
print(sol.longestPalindrome("babad"))