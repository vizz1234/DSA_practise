import heapq
from typing import List

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:

        events = []

        for l, r, h in buildings:

            events.append((l, -h, r))
            events.append((r, 0, r))
        
        events.sort()

        heap = [(0, float('inf'))]
        result = []

        for left, height, right in events:

            if height:
                heapq.heappush(heap, (height, right))
            
            while heap[0][1] <= left:
                heapq.heappop(heap)
            
            h = -heap[0][0]

            if not result or result[-1][1] != h:
                result.append([left, h])
        
        return result

sol = Solution()
print(sol.getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))
print(sol.getSkyline([[0,2,3],[2,5,3]]))