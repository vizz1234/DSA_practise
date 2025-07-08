class Solution:
    def maxValue(self, arr):
        # code here
        prev, prev2 = 0, 0
        secPrev, secPrev2 = 0, 0
        loot1, loot2 = 0, 0
        n = len(arr)
        
        for i in range(n - 1):
            
            loot1 = max(prev, secPrev + arr[i])
            secPrev = prev
            prev = loot1
            
            loot2 = max(prev2, secPrev2 + arr[i + 1])
            secPrev2 = prev2
            prev2 = loot2
        
        return max(loot1, loot2)

sol = Solution()
print(sol.maxValue([5, 5, 10, 100, 10, 5]))