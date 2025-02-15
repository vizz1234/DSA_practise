class Solution:
    #Complete the below function
    def countPairs(self, arr, target):
        #Your code here
        arr.sort()
        left = 0
        n = len(arr)
        right = n - 1
        res = 0
        while left < right:
            s = arr[left] + arr[right]
            if s < target:
                res += right - left
                left += 1
            else:
                right -= 1
        return res
obj = Solution()
print(obj.countPairs([1,2,3,4,5], 5))