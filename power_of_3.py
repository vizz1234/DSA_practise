import math

class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        if n <= 0:
            return False
        
        x = round(math.log(n, 3))

        return 3 ** x == n

sol = Solution()
print(sol.isPowerOfThree(27))
print(sol.isPowerOfThree(0))