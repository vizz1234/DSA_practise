class Solution:
    def lowerBound(self, arr, target):
        # code here
        n = len(arr)
        left = 0
        right = n - 1
        if arr[n - 1] < target:
            return n
        ele_idx = n - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] >= target:
                ele_idx = mid
                right = mid - 1
            else:
                left = mid + 1
        return ele_idx
sol = Solution()
print(sol.lowerBound([1, 2, 3, 4, 5], 3))