class Solution:
    def decodedString(self, s):
        # code here
        curS = ''
        curNum = 0
        stack = []
        
        for char in s:
            if char.isdigit():
                curNum = 10 * curNum + int(char)
            
            elif char == '[':
                stack.append((curNum, curS))
                curNum = 0
                curS = ''
            
            elif char == ']':
                mulNum, mulStr = stack.pop()
                curS = mulStr + curS * mulNum
                
            else:
                curS += char
        
        return curS

s = Solution()
print(s.decodedString("3[a2[c]]"))