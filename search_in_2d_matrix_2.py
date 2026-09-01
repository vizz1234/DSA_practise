from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        nr, nc = len(matrix), len(matrix[0])
        r, c = nr - 1, 0

        while r >= 0 and c < nc:

            v = matrix[r][c]

            if v == target:
                return True
            
            if v < target:
                c += 1
            
            else:
                r -= 1
        
        return False
        
sol = Solution()
print(sol.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5))    