class Solution:
    def nextGreater(self, arr):
        # code here
        stack = []
        n = len(arr)
        result = [-1] * n
        
        for i in range(2 * n):
            
            curr = arr[i % n]
            
            while stack and arr[stack[-1]] < curr:
                idx = stack.pop()
                result[idx] = curr
            
            if i < n:
                stack.append(i)
        
        return result

sol = Solution()
print(sol.nextGreater([1, 2, 1]))