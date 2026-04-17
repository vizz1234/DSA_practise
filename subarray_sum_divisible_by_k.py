class Solution:
    # Function to count the number of subarrays with a sum that is divisible by K
    def subCount(self, arr, k):
        # Your code goes here
        prefix_sum = {0: 1}
        prefix = 0
        count = 0
        for i in range(len(arr)):
            prefix += arr[i]
            rem = prefix % k
            if rem in prefix_sum:
                count += prefix_sum[rem]
                prefix_sum[rem] += 1
            else:
                prefix_sum[rem] = 1
        return count

sol = Solution()
arr = [4, 5, 0, -2, -3, 1]
k = 5
print(sol.subCount(arr, k))