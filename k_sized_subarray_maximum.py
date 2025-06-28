from collections import deque
class Solution:
    def maxOfSubarrays(self, arr, k):
        # code here
        dq = deque()
        n = len(arr)
        output = []
        
        for i in range(n):
            if dq and dq[0] < i + 1 - k:
                dq.popleft()
            
            while dq and arr[dq[-1]] < arr[i]:
                dq.pop()
            
            dq.append(i)
            
            if i >= k - 1:
                output.append(arr[dq[0]])
        
        return output

sol = Solution()
print(sol.maxOfSubarrays([1, 2, 3, 4, 5], 3))