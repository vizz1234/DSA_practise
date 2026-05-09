import heapq
class Solution:
    def nearlySorted(self, arr, k):  
        #code here
        heap = []
        idx = 0
        
        for i in range(k + 1):
            heapq.heappush(heap, arr[i])
        
        for i in range(k + 1, len(arr)):
            arr[idx] = heapq.heappop(heap)
            idx += 1
            heapq.heappush(heap, arr[i])
        
        while heap:
            arr[idx] = heapq.heappop(heap)
            idx += 1
        
        return arr

sol = Solution()
print(sol.nearlySorted([6, 5, 3, 2, 8, 10, 9], 3))
