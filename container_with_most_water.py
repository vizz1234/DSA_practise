class Solution:
    def maxWater(self, arr):
        # code here
        n = len(arr)
        left = 0
        right = n - 1
        res = 0
        while left < right:
            l = min(arr[left], arr[right])
            res = max(res, l * (right - left))
            if arr[left] < arr[right]:
                left += 1
            else:
                right -= 1
        return res
obj = Solution()
print(obj.maxWater([1,5,4,3]))