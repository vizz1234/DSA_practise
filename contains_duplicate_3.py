from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:

        window = valueDiff + 1
        buckets = {}

        for i, num in enumerate(nums):

            if i > indexDiff:
                old_num = nums[i - indexDiff - 1]
                old_bucket = old_num // window
                del buckets[old_bucket]
            
            bucket = num // window
            if bucket in buckets:
                return True
            buckets[bucket] = num

            if bucket - 1 in buckets:
                if abs(num - buckets[bucket - 1]) <= valueDiff:
                    return True
            
            if bucket + 1 in buckets:
                if abs(num - buckets[bucket + 1]) <= valueDiff:
                    return True
            
        return False

sol = Solution()
print(sol.containsNearbyAlmostDuplicate([1,2,3,1], 3, 0))      