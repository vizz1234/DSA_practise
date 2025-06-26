class Solution:
    def evaluate(self, arr):
        # code here
        stack = []
        n = len(arr)
        for i in range(n):
            if arr[i] in ('+', '-', '*', '/'):
                e1 = stack[-1]
                e2 = stack[-2]
                if arr[i] == '+':
                    res = e1 + e2
                elif arr[i] == '-':
                    res = e2 - e1
                elif arr[i] == '*':
                    res = e1 * e2
                else:
                    res = int(e2 / e1)
                stack.pop()
                stack[-1] = res
            else:
                stack.append(int(arr[i]))
            
        return stack[-1]

s = Solution()
print(s.evaluate(["1", "2", "+", "3", "4", "+", "*"]))