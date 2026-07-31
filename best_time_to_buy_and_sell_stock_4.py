from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        buy = [float('-inf')] * (k + 1)
        sell = [0] * (k + 1)

        for price in prices:
            for k in range(1, k + 1):
                buy[k] = max(buy[k], sell[k-1] - price)
                sell[k] = max(sell[k], buy[k] + price)
        
        return sell[k]

sol = Solution()
print(sol.maxProfit(k = 2, prices = [3,2,6,5,0,3]))