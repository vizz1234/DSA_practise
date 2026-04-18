class Solution:
    def longestSubarrayDivK(self, arr, k):
        #Complete the function
        prefix_sum = {0: -1}
        prefix = 0
        max_size = 0
        for i in range(len(arr)):
            prefix += arr[i]
            rem = prefix % k
            if rem in prefix_sum:
                size = i - prefix_sum[rem]
                max_size = max(max_size, size)
            else:
                prefix_sum[rem] = i
        return max_size
sol = Solution()
arr = [2, 7, 6, 1, 4, 5]
k = 3
print(sol.longestSubarrayDivK(arr, k))