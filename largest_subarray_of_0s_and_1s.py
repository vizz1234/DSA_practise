class Solution:
    def maxLen(self, arr):
        # code here
        d = {}
        res = 0
        pS = 0
        n = len(arr)
        for i in range(n):
            pS += 1 if arr[i] == 1 else -1
            if pS == 0:
                res = i + 1
            if pS in d:
                res = max(res, i - d[pS])
            else:
                d[pS] = i
        return res
obj = Solution()
print(obj.maxLen([1,0,1,1,1,0,0]))