from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:

        left, right = 0, len(citations) - 1
        n = len(citations)

        while left <= right:

            mid = (left + right) // 2

            if citations[mid] >= (n - mid):
                right = mid - 1
            
            else:
                left = mid + 1
                
        
        return n - left

sol = Solution()
print(sol.hIndex([0, 1, 3, 5, 6]))
print(sol.hIndex([1, 100]))