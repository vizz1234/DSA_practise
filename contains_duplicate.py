from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        num_set = set(nums)

        return False if len(num_set) == len(nums) else True

sol = Solution()
print(sol.containsDuplicate([1,2,3,1]))
print(sol.containsDuplicate([1,2,3,4]))
print(sol.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))