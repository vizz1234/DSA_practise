class Solution:
    def subsets(self, arr):
        n = len(arr)
        res = []
        for mask in range(1 << n):        # 0 to 2^n - 1
            cur = []
            for i in range(n):
                if mask & (1 << i):       # if i-th bit is set
                    cur.append(arr[i])
            res.append(cur)
        return res

sol = Solution()
print(sol.subsets([1, 2, 3]))
