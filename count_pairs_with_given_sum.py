class Solution:
    #Complete the below function
    def countPairs(self,arr, target):
        #Your code here
        d = {}
        count = 0
        for num in arr:
            cur = target - num
            count += d.get(cur, 0)
            d[num] = d.get(num, 0) + 1
        return count
obj = Solution()
print(obj.countPairs([1,2,3,4,5,6,7,8,9,10], 10))