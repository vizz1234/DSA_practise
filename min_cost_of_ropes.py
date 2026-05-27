import heapq
class Solution:
   def minCost(self, arr):
    # code here
    total_cost = 0
    heapq.heapify(arr)
    
    while len(arr) > 1:
        f = heapq.heappop(arr)
        s = heapq.heappop(arr)
        m = f + s
        total_cost += m
        heapq.heappush(arr, m)
    
    return total_cost

sol = Solution()
print(sol.minCost([4, 2, 7, 6, 9]))