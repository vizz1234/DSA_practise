class Solution:
    def minRemovals(self, arr, k):
        # code here
        total = sum(arr)
        n = len(arr)
        if total == k:
            return n
        if k == 0:
            return 0
        target = total - k
        left = 0
        maxLen = -1
        curSum = 0
        for right in range(n):
            curSum += arr[right]
            while left < right and curSum > target:
                curSum -= arr[left]
                left += 1
            if curSum == target:
                maxLen = max(maxLen, right - left + 1)
        return n - maxLen if maxLen != -1 else -1
sol = Solution()
arr = [1, 2, 3, 4, 5]
k = 10
print(sol.minRemovals(arr, k))