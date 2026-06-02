class Solution:
    def totHammingDist(self, arr):
        # code here
        s = 0
        n = len(arr)
        
        for i in range(32):
            ones = 0
            for j in range(n):
                if arr[j] & (1 << i):
                    ones += 1
            zeros = n - ones
            s += ones * zeros
        
        return s

sol = Solution()
print(sol.totHammingDist([4, 14, 4, 14]))