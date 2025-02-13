class Solution:
    def countSubarrays(self, arr, k):
        # code here
        d = {}
        cS = 0
        n = len(arr)
        res = 0
        for i in range(n):
            cS += arr[i]
            d[cS] = d.get(cS, 0) + 1
            if cS == k:
                res += 1
            if cS - k in d:
                res += d[cS - k]
        return res
obj = Solution()
print(obj.countSubarrays([1,2,3,4,5], 5))