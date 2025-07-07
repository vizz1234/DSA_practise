class Solution:
    def equalPartition(self, arr):
        # code here
        arrSum = sum(arr)
        if arrSum % 2 != 0:
            return False
        
        target = arrSum // 2
        dp = [False] * (target + 1)
        dp[0] = True
        
        for num in arr:
            for i in range(target, num - 1, -1):
                if dp[i - num]:
                    dp[i] = True
        
        return dp[target]

sol = Solution()
print(sol.equalPartition([1, 5, 11, 5]))