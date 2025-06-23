class Solution:
    def calculateSpan(self, arr):
        #write code here
        stack = []
        output = []
        for i in range(len(arr)):
            val = arr[i]
            while stack and arr[stack[-1]] <= val:
                stack.pop()
            
            if not stack:
                span = i + 1
            else:
                span = i - stack[-1]
    
            output.append(span)
            stack.append(i)
            
        return output

s = Solution()
print(s.calculateSpan([100, 80, 60, 70, 60, 75, 85]))