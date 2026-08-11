from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        if n <= 3:
            return max(nums)
        
        dp1_second_prev = nums[0]
        dp1_prev = max(nums[0], nums[1])
        dp2_second_prev = nums[1]
        dp2_prev = max(nums[1], nums[2])

        for i in range(2, n - 1):
            dp1 = max(dp1_prev, nums[i] + dp1_second_prev)
            dp1_second_prev = dp1_prev
            dp1_prev = dp1
       
        for i in range(3, n):
            dp2 = max(dp2_prev, nums[i] + dp2_second_prev)
            dp2_second_prev = dp2_prev
            dp2_prev = dp2
        
        return max(dp1_prev, dp2_prev)

sol = Solution()
print(sol.rob([2,3,2]))
print(sol.rob([1,2,3,1]))
        