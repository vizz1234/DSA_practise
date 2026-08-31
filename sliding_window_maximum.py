from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        q = deque([])
        output = []

        for i, num in enumerate(nums):

            if q and q[0] <= i - k:
                q.popleft()
            
            while q and num >= nums[q[-1]]:
                q.pop()
            
            q.append(i)
            
            if i >= k - 1:
                output.append(nums[q[0]])
        
        return output

sol = Solution()
print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))




        