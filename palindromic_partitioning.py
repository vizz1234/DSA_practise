
class Solution:
    def palPartition(self, s):
        # code here
        n = len(s)
        pal = [[False] * n for _ in range(n)]
        
        for i in range(n):
            pal[i][i] = True
        
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2:
                        pal[i][j] = True
                    else:
                        pal[i][j] = pal[i + 1][j - 1]
        
        dp = [0] * (n + 1)
        
        for i in range(n - 1, -1, -1):
            if pal[i][n - 1]:
                dp[i] = 0
                continue
        
            ans = float('inf')
            
            for j in range(i, n):
                if pal[i][j]:
                    ans = min(ans, 1 + dp[j + 1])
            
            dp[i] = ans
        
        return dp[0]

sol = Solution()
print(sol.palPartition("aab"))  
