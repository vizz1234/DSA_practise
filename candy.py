# class Solution:
#     def minCandy(self, arr):
#         # Code here
#         n = len(arr)
#         candies = [1] * n
        
#         for i in range(1, n):
#             if arr[i] > arr[i - 1]:
#                 candies[i] = candies[i - 1] + 1
        
#         for i in range(n - 2, -1, -1):
#             if arr[i] > arr[i + 1]:
#                 candies[i] = max(candies[i], candies[i + 1] + 1)
        
#         return sum(candies)

# sol = Solution()
# print(sol.minCandy([1, 3, 2, 1]))

#candy optimised with O(1) space

from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n <= 1:
            return n
        
        total = 1      # first child always gets 1
        up = 0         # length of current increasing run
        down = 0       # length of current decreasing run
        peak = 0       # up-run length that produced the most recent peak
        
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                up += 1
                down = 0
                peak = up
                total += 1 + up        # this child's candy count, added directly
            elif ratings[i] == ratings[i - 1]:
                up = down = peak = 0
                total += 1             # flat spot, resets everything
            else:
                up = 0
                down += 1
                total += down          # triangular-number trick
                if down > peak:
                    total += 1         # bump the peak retroactively
        
        return total

sol = Solution()
print(sol.candy([1, 3, 2, 1]))