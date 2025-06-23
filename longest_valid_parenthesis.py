class Solution:
    def maxLength(self, s):
        # code here
        stack = [-1]
        n = len(s)
        longPar = 0
        
        for i in range(n):
            
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                
                if not stack:
                    stack.append(i)
                
                else:
                    longPar = max(longPar, i - stack[-1])
        
        return longPar

s = Solution()
print(s.maxLength("(()))"))