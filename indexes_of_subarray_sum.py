class Solution:
    def subarraySum(self, arr, target):
        # code here
        # This is done using prefix sum, hence takes O(n) space and time, but can be done in O(1) space and O(n) time using two pointers
        pS = {}
        cS = 0
        n = len(arr)
        for i in range(n):
            cS += arr[i]
            if cS not in pS:
                pS[cS] = i
            if cS == target:
                return [1, i + 1]
            if cS - target in pS:
                return [pS[cS - target] + 2, i + 1]
        return [-1]
obj = Solution()
print(obj.subarraySum([1,2,3,4,5], 5))

#Using two pointers, we can do this in O(1) space and O(n) time
class twoPointerSolution:
    def subarraySum(self, arr, target):
        # code here
        left = 0
        right = 0
        n = len(arr)
        cS = 0
        while right < n:
            cS += arr[right]
            while cS > target:
                cS -= arr[left]
                left += 1
            right += 1
        return [-1]
obj = twoPointerSolution()
print(obj.subarraySum([1,2,3,4,5], 5))