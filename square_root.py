class Solution:
    def floorSqrt(self, n): 
        # code here
        left, right = 0, n
        while left <= right:
            mid = (left + right) // 2
            sq = mid * mid
            if sq == n:
                return mid
            elif sq < n:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
sol = Solution()
print(sol.floorSqrt(10))