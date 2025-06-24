class Solution:
    def getMaxArea(self,arr):
        #code here
        stack = []
        n = len(arr)
        maxArea = 0
        
        for i in range(n):
            while stack and arr[i] < arr[stack[-1]]:
                top = stack.pop()
                width = i if not stack else i - stack[-1] - 1
                area = arr[top] * width
                maxArea = max(area, maxArea)
            stack.append(i)
        
        i = n
        
        while stack:
            top = stack.pop()
            width = i if not stack else i - stack[-1] - 1
            area = arr[top] * width
            maxArea = max(area, maxArea)
        
        return maxArea

s = Solution()
print(s.getMaxArea([6, 2, 5, 4, 5, 1, 6]))