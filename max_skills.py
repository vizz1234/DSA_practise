class Solution:
    def maxSkill(self, arr):
        # code here
        n = len(arr)
        nums = [1] + arr + [1]
        
        dp = [[0] * (n + 1) for _ in range(n + 2)]
        
        for length in range(1, n + 1):
            
            for l in range(1, n - length + 2):
                
                r = l + length - 1
                
                for k in range(l, r + 1):
                    
                    gain = nums[l - 1] * nums[k] * nums[r + 1]
                    
                    total = dp[l][k - 1] + gain + dp[k + 1][r]
                    
                    dp[l][r] = max(dp[l][r], total)
        
        return dp[1][n]

sol = Solution()
print(sol.maxSkill([3, 1, 5, 8]))