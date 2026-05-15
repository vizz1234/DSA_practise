from collections import deque
class Solution:
    def getScore(self, arr, k):
        if not arr:
            return 0
        # code here
        s = arr[0]
        n = len(arr)
        q = deque([0])
        dp = [float('-inf')] * n
        dp[0] = arr[0]
        
        for i in range(1, n):
            
            if q[0] < i - k:
                q.popleft()
            
            dp[i] = dp[q[0]] + arr[i]
            
            while q and dp[q[-1]] <= dp[i]:
                q.pop()
            
            q.append(i)
        
        return dp[n - 1]
    
sol = Solution()
print(sol.getScore([1, -1, -20, 4, -2, 3], 2))