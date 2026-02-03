class Solution:
    def minIncrements(self, arr): 
        # Code here
        if len(arr) < 2:
            return 0
        arr.sort()
        count = 0
        for i in range(1, len(arr)):
            if arr[i] <= arr[i - 1]:
                count += arr[i - 1] + 1 - arr[i]
                arr[i] = arr[i - 1] + 1
        return count
sol = Solution()
print(sol.minIncrements([1, 2, 2, 3, 3, 3]))