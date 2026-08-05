class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:

        while right > left:
            right = right & (right - 1)

        return right 

sol = Solution()
print(sol.rangeBitwiseAnd(5, 7))
