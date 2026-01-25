class Solution:
    def getLastMoment(self, n, left, right):
        # code here
        tl = max(left) if left else 0
        tr = n - min(right) if right else 0
        return max(tl, tr)
sol = Solution()
print(sol.getLastMoment(10, [2, 4, 6], [1, 3, 5]))