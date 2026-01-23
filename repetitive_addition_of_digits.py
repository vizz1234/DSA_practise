class Solution:
    def singleDigit(self, n):
        #code here 
        if n == 0:
            return 0
        return 1 + (n - 1) % 9
sol = Solution()
print(sol.singleDigit(123456789))