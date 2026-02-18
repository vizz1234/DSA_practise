class Solution:
    def countPairs(self, arr, k):
        # code here
        d = {}
        for num in arr:
            if num not in d:
                d[num] = 0
            d[num] += 1
        
        count = 0
        for num, val in d.items():
            if num + k in d:
                count += d[num] * d[num + k]
        return count
sol = Solution()
print(sol.countPairs([1, 5, 3, 4, 2], 3))