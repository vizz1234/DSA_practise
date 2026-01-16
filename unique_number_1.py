class Solution:
    def findUnique(self, arr):
        # code here 
        x = 0
        for i in arr:
            x ^= i
        return x
sol = Solution()
print(sol.findUnique([1,2,1,3,3,4,4,5,5]))