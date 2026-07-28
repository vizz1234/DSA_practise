from functools import cmp_to_key
from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        strs = [str(num) for num in nums]

        def compare(a, b):

            if a + b > b + a:
                return -1
            
            elif b + a > a + b:
                return 1
            
            else:
                return 0
        
        strs.sort(key = cmp_to_key(compare))
        res = ''.join(strs)
        return res if res[0] != '0' else '0'

sol = Solution()
print(sol.largestNumber([10, 2]))
