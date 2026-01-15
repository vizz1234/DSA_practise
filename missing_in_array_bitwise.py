class Solution:
    def missingNum(self, arr):
        # code here
        n = len(arr)
        x1 = 0
        x2 = 0
        for i in arr:
            x1 ^= i
        for i in range(1, n + 2):
            x2 ^= i
        return x1 ^ x2
sol = Solution()
print(sol.missingNum([1,2,3,5]))
