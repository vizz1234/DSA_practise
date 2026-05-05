from collections import Counter
import heapq

class Solution:
    def topKFreq(self, arr, k):
        # Code here
        freq = Counter(arr)
        heap = []
        
        for num, f in freq.items():
            heapq.heappush(heap, (-f, -num))
        
        result = []
        
        for _ in range(k):
            f, num = heapq.heappop(heap)
            result.append(-num)
        
        return result
        
sol = Solution()
print(sol.topKFreq([1,1,1,2,2,3], 2))      
print(sol.topKFreq([1,1,1,2,2,3], 1))      