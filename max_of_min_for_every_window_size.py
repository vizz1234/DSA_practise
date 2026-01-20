class Solution:
    def maxOfMins(self, arr):
       # code here
        n = len(arr)
        left = [-1] * n
        right = [n] * n
        stack = []
       
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)
        
        stack = []
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)
        
        ans = [0] * (n + 1)
        
        for i in range(n):
            length = right[i] - left[i] - 1
            ans[length] = max(ans[length], arr[i])
        
        for i in range(n - 1, 0, -1):
            ans[i] = max(ans[i], ans[i + 1])
        
        return ans[1:]
        
sol = Solution()       
print(sol.maxOfMins([10, 20, 30, 50, 10, 70, 30]))       
            
       
       