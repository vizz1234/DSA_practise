class Solution:
    def longestSubarray(self, arr, k):
        # Code Here
        n = len(arr)
        greater_than_k = [1 if num > k else -1 for num in arr]
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + greater_than_k[i]
        max_len = 0
        stack = []
        for i in range(n + 1):
            if not stack or prefix[i] < prefix[stack[-1]]:
                stack.append(i)
        for j in range(n, -1, -1):
            while stack and prefix[j] > prefix[stack[-1]]:
                max_len = max(max_len, j - stack[-1])
                stack.pop()
        return max_len
sol = Solution()
arr = [1, 2, 3, 4, 1]
k = 2
print(sol.longestSubarray(arr, k))
arr = [6, 5, 3, 4] 
k = 2
print(sol.longestSubarray(arr, k))