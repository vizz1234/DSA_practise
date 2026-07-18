from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        if not tokens:
            return 0
        
        valid_op = {'+', '-', '*', '/'}
        stack = []

        for token in tokens:
            if token in valid_op:
                ele = stack.pop()
                if token == '+':
                    stack[-1] += ele
                elif token == '-':
                    stack[-1] -= ele
                elif token == '*':
                    stack[-1] *= ele
                else:
                    stack[-1] = int(stack[-1] / ele)
            else:
                stack.append(int(token))
        
        return stack[0]

sol = Solution()
print(sol.evalRPN(["2", "1", "+", "3", "*", "4", "+"]))
print(sol.evalRPN(["1", "2", "+", "3", "*"])) 