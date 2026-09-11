from typing import List

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        res = []

        def backtrack(index, expr, curr_val, prev_operand):
            if index == n:
                if curr_val == target:
                    res.append(expr)
                return
            for i in range(index, n):
                if i > index and num[index] == '0':   # no leading zeros
                    break
                operand_str = num[index:i + 1]
                operand = int(operand_str)
                if index == 0:
                    backtrack(i + 1, operand_str, operand, operand)
                else:
                    backtrack(i + 1, expr + '+' + operand_str, curr_val + operand, operand)
                    backtrack(i + 1, expr + '-' + operand_str, curr_val - operand, -operand)
                    backtrack(i + 1, expr + '*' + operand_str,
                              curr_val - prev_operand + prev_operand * operand,
                              prev_operand * operand)

        backtrack(0, "", 0, 0)
        return res

sol = Solution()
print(sol.addOperators("123", 6))