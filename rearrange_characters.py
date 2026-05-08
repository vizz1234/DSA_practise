import heapq
from collections import Counter

class Solution :
    def rearrangeString(self, s):
        #code here
        freq = Counter(s)
        
        heap = [(-count, char) for char, count in freq.items()]
        heapq.heapify(heap)
        
        while len(heap) >= 2:
            
            count1, char1 = heapq.heappop(heap)
            count2, char2 = heapq.heappop(heap)
            
            if count1 + 1 < 0:
                heapq.heappush(heap, (count1 + 1, char1))
            
            if count2 + 1 < 0:
                heapq.heappush(heap, (count2 + 1, char2))
            
        if heap:
            count, char = heapq.heappop(heap)
            if count + 1 < 0:
                return 0
        
        return 1

sol = Solution()
print(sol.rearrangeString("aaabbc"))      
print(sol.rearrangeString("aab"))  
