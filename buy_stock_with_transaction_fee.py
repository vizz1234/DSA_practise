class Solution:
    def maxProfit(self, arr, k):
        # Code here
        n = len(arr)
        free = 0
        hold = float('-inf')
        
        for i in range(n):
            
            prev_free = free
            prev_hold = hold
            
            free = max(prev_free, prev_hold + arr[i] - k)
            
            hold = max(prev_hold, prev_free - arr[i])
            
        return free

sol = Solution()
print(sol.maxProfit([1, 3, 7, 5, 10, 3], 3))