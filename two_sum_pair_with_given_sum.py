class Solution:
    def twoSum(self, arr, target):
        # code here
        d = {}
        for num in arr:
            cur = target - num
            if d.get(cur, 0) != 0:
                return True
            d[num] = 1
        return False

obj = Solution()
print(obj.twoSum([2,3,5,8,9,10,11], 17))