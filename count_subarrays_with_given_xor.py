class Solution:
    def subarrayXor(self, arr, k):
        # code here
        d = {}
        cV = 0
        res = 0
        n = len(arr)
        for i in range(n):
            cV = cV ^ arr[i]
            if cV == k:
                res += 1
            if d.get(cV ^ k, 0) != 0:
                res += d[cV ^ k]
            d[cV] = d.get(cV, 0) + 1
        return res
obj = Solution()
print(obj.subarrayXor([4,2,2,6,4], 6))