class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        return True if n > 0 and (n & (n - 1) == 0) else False 

sol = Solution()
print(sol.isPowerOfTwo(7))
print(sol.isPowerOfTwo(128))