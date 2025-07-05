class Solution:
    def minJumps(self, arr):
        # code here
        n = len(arr)
        dp = [float('inf')] * n
        dp[0] = 0
        for i in range(1, n):
            for j in range(i):
                if j + arr[j] >= i:
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[-1] if dp[-1] != float('inf') else -1

sol = Solution()
print(sol.minJumps([2, 3, 1, 1, 4]))