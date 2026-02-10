class Solution:
    def minDaysBloom(self, arr, k, m):
        # Code here
        if len(arr) < k * m:
            return -1
        
        def check_valid_days(d):
            b = 0
            c = 0
            for n in arr:
                if n <= d:
                    c += 1
                else:
                    b += c // k
                    c = 0
            b += c // k
            return b >= m
        
        left, right = min(arr), max(arr)
        ans = right
        
        while left <= right:
            mid = (left + right) // 2
            if check_valid_days(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans
sol = Solution()
print(sol.minDaysBloom([1, 10, 3, 10, 2], 3, 1))