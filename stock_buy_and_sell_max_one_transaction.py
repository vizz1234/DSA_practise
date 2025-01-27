class Solution:
    def maximumProfit(self, prices):
        # code here
        curMin = prices[0]
        maxProfit = 0
        for i in range(1, len(prices)):
            if prices[i] < curMin:
                curMin = prices[i]
                continue
            maxProfit = max(maxProfit, prices[i] - curMin)
        return maxProfit
obj = Solution()
print(obj.maximumProfit([7,1,5,3,6,4]))