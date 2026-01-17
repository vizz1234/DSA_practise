class Solution:
    def singleNum(self, arr):
        # Code here
        x = 0
        for num in arr:
            x ^= num
        mask = x & -x
        a, b = 0, 0
        for num in arr:
            if num & mask:
                a ^= num
            else:
                b ^= num
        if a < b:
            return [a, b]
        return [b, a]
sol = Solution()
print(sol.singleNum([1,2,3,4,2,3]))
