from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        curMax = curMin = result = nums[0]

        for i in range(1, len(nums)):

            if nums[i] < 0:

                curMin, curMax = curMax, curMin

            curMin = min(nums[i], curMin * nums[i])
            curMax = max(nums[i], curMax * nums[i])
            result = max(result, curMax)
        
        return result

sol = Solution()
print(sol.maxProduct([2,3,-2,4]))