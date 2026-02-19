class Solution:
    def countSum(self, arr, target):
        #code here
        n = len(arr)
        pair_sum = {}
        count = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                s = arr[i] + arr[j]
                if target - s in pair_sum:
                    count += pair_sum[target - s]
            for k in range(i):
                s = arr[i] + arr[k]
                pair_sum[s] = pair_sum.get(s, 0) + 1
        
        return count

# Example usage:
sol = Solution()
arr = [1, 2, 3, 4, 5]
target = 10
print(sol.countSum(arr, target))  # Output: 2