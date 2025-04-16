import heapq

class Solution:
    def kLargest(self, arr, k):
        # Your code here
        maxK = arr[:k]
        heapq.heapify(maxK)
        
        for i in arr[k:]:
            if i > maxK[0]:
                heapq.heapreplace(maxK, i)
        
        output = []
        while maxK:
            output.append(heapq.heappop(maxK))
        
        return output[::-1]
