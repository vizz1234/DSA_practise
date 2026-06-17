from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        output = [1]
        for i in range(1, rowIndex + 1):
            cur_output = output + [1] 
            for j in range(1, len(output)):
                cur_output[j] = output[j-1] + output[j]
            output = cur_output
        return output

sol = Solution()
print(sol.getRow(3))