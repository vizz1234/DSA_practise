from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:

        def is_valid(cdt_s):

            stack = [0]

            for i in range(len(cdt_s)):
                
                if cdt_s[i] == '(':
                    stack.append('(')
                
                if cdt_s[i] == ')':
                    if stack[-1] != '(':
                        return 1
                    else:
                        stack.pop()
            
            return 3 if stack[-1] == 0 else 2
        
        cdt_output = []
        n = len(s)
        self.max_len = 0
        memo = set()

        def recur(chk_s, idx):

            if idx == n:

                if is_valid(chk_s) == 3:
                    cdt_output.append(chk_s)
                    self.max_len = max(self.max_len, len(chk_s))

                return
            
            if is_valid(chk_s) == 1:
                return
            
            if idx - len(chk_s) > n - self.max_len:
                return
            
            if (chk_s, idx) in memo:
                return
            else:
                memo.add((chk_s, idx))

            recur(chk_s + s[idx], idx + 1)
            recur(chk_s, idx + 1)
        
        recur('', 0)

        return list(set([cdt for cdt in cdt_output if len(cdt) == self.max_len]))

sol = Solution()
print(sol.removeInvalidParentheses("(a)())())"))