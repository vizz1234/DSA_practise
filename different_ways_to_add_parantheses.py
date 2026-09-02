from functools import lru_cache
from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:

        @lru_cache(maxsize = None)
        def solve(expr):

            if expr.isdigit():
                return [int(expr)]
            
            results = []

            for i, ch in enumerate(expr):

                if ch in '+-*':

                    left = solve(expr[:i])
                    right = solve(expr[i+1:])

                    for l in left:
                        for r in right:

                            if ch == '+':
                                results.append(l + r)
                            
                            elif ch == '-':
                                results.append(l - r)
                            
                            elif ch == '*':
                                results.append(l * r)
            
            return results
        
        return solve(expression)

sol = Solution()
print(sol.diffWaysToCompute("2-1-1"))