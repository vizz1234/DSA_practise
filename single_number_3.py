from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:

        x = 0

        for num in nums:
            x ^= num
        
        bit = x & -x
        a = 0
        b = 0

        for num in nums:
            if num & bit:
                a ^= num
            else:
                b ^= num
        
        return [a, b]

sol = Solution()
print(sol.singleNumber([1,2,1,3,2,5]))
        