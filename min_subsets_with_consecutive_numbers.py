class Solution:
    def numOfSubset(self, arr):
        # Your code goes here
        if len(arr) == 0:
            return 0
        arr.sort()
        cur_num = arr[0]
        count = 1
        for i in range(1, len(arr)):
            if arr[i] != cur_num + 1:
                count += 1
            cur_num = arr[i]
        return count

# Example usage:
sol = Solution()
arr = [1, 2, 3, 4, 5]
print(sol.numOfSubset(arr))  # Output: 1