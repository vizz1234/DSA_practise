class Solution:
    def countDistinct(self, arr, k):
        # Code here
        n = len(arr)
        d = {}
        res = []
        for i in range(k):
            d[arr[i]] = d.get(arr[i], 0) + 1
        res.append(len(d))
        for i in range(k, n):
            d[arr[i]] = d.get(arr[i], 0) + 1
            d[arr[i-k]] -= 1
            if d[arr[i-k]] == 0:
                del d[arr[i-k]]
            res.append(len(d))
        return res
obj = Solution()
print(obj.countDistinct([1,2,3,4,5], 3))