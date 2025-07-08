class Solution:  
    def findMaxSum(self,arr):
        # code here
        secPrev = 0
        prev = 0
        n = len(arr)
        loot = 0
        
        for i in range(n):
            loot = max(prev, secPrev + arr[i])
            secPrev = prev
            prev = loot
        
        return loot

sol = Solution()
print(sol.findMaxSum([5, 5, 10, 100, 10, 5]))