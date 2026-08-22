from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        r, c = len(matrix), len(matrix[0])
        dp = [[0] * (c + 1) for _ in range(r + 1)]
        max_count = 0

        for i in range(1, r + 1):
            for j in range(1, c + 1):

                if matrix[i - 1][j - 1] == "1":

                    dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])
                    max_count = max(max_count, dp[i][j])
        
        return max_count ** 2

sol = Solution()
print(sol.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
print(sol.maximalSquare([["0","1"],["1","0"]]))
print(sol.maximalSquare([["0"]]))