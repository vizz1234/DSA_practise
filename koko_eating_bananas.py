class Solution:
    def kokoEat(self, arr, k):
        # Code here
        def hours_needed(speed):
            total = 0
            for pile in arr:
                total += (pile + speed - 1) // speed
            return total
        
        left, right = 1, max(arr)
        ans = right
        
        while left <= right:
            mid = (left + right) // 2
            if hours_needed(mid) <= k:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans
sol = Solution()
print(sol.kokoEat([3, 6, 7, 11], 8))