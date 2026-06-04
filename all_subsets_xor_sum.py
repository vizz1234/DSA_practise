class Solution:
    def subsetXORSum(self, arr):
        # code here
        n = len(arr)
        or_all = 0
        
        for num in arr:
            or_all |= num
        
        return or_all * (1 << (n - 1))

sol = Solution()
print(sol.subsetXORSum([1, 3, 5]))