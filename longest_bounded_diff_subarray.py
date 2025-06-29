from collections import deque
class Solution:
    def longestSubarray(self, arr, x):
        #code here 
        left = 0
        incDq = deque()
        decDq = deque()
        maxWin = 0
        start = 0
        n = len(arr)
        
        for right in range(n):
            
            while incDq and arr[right] < arr[incDq[-1]]:
                incDq.pop()
            incDq.append(right)
            
            while decDq and arr[right] > arr[decDq[-1]]:
                decDq.pop()
            decDq.append(right)
            
            while arr[decDq[0]] - arr[incDq[0]] > x:
                left += 1
                if decDq[0] < left:
                    decDq.popleft()
                if incDq[0] < left:
                    incDq.popleft()
            
            if right - left + 1 > maxWin:
                maxWin = right - left + 1
                start = left
            
        return arr[start : start + maxWin]
    
sol = Solution()
print(sol.longestSubarray([8, 4, 2, 6, 7], 4))