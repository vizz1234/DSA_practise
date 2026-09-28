class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        hold = float('-inf')
        sold = float('-inf')
        rest = 0

        for price in prices:

            prev_hold = hold
            prev_sold = sold
            prev_rest = rest

            hold = max(prev_hold, prev_rest - price)
            sold = prev_hold + price
            rest = max(prev_rest, prev_sold)
        
        return max(sold, rest)

sol = Solution()
print(sol.maxProfit([1,2,3,0,2]))
print(sol.maxProfit([1]))
