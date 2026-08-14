import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap = []

        for num in nums:

            top = None

            if len(heap) >= k:
                top = heap[0]

                if num > top:
                    heapq.heappushpop(heap, num)
            
            else:
                heapq.heappush(heap, num)
        
        return heap[0]

sol = Solution()
print(sol.findKthLargest([3,2,1,5,6,4], 2))