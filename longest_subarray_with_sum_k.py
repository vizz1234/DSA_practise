class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        d = {}
        pS = 0
        n = len(arr)
        res = 0
        for i in range(n):
            pS += arr[i]
            if pS == k:
                res = i + 1
            if pS - k in d:
                res = max(res, i - d[pS - k])
            if pS not in d:
                d[pS] = i
        return res
obj = Solution()
print(obj.longestSubarray([1,2,3,4,5], 5))