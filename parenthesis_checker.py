class Solution:
    def isBalanced(self, s):
        # code here
        stack = [-1]
        for i in s:
            if i in ('(', '{', '['):
                stack.append(i)
            else:
                top = stack[-1]
                if i == ')' and top == '(':
                    stack.pop()
                elif i == '}' and top == '{':
                    stack.pop()
                elif i == ']' and top == '[':
                    stack.pop()
                else:
                    return False
        top = stack[-1]
        if top == -1:
            return True
        return False