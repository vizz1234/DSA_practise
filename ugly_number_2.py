class Solution:
    # Function to find the nth ugly number.
    def uglyNumber(self, n):
        # code here
        
        dp = [0] * n
        dp[0] = 1
        
        p2, p3, p5 = 0, 0, 0
        
        for i in range(1, n):
            
            n2, n3, n5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
            dp[i] = min(n2, n3, n5)
            
            if dp[i] == n2:
                p2 += 1
            if dp[i] == n3:
                p3 += 1
            if dp[i] == n5:
                p5 += 1
        
        return dp[n - 1]

sol = Solution()
print(sol.uglyNumber(10))