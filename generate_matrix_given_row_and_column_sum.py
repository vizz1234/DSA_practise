class Solution:
    def generateMatrix(self, rowSum, colSum):
        # code here
        n = len(rowSum)
        m = len(colSum)
        
        output = [[0] * m for _ in range(n)]
        cur_row_sum = [0] * n
        cur_col_sum = [0] * m
        
        for i in range(n):
            for j in range(m):
                row_val = rowSum[i] - cur_row_sum[i]
                col_val = colSum[j] - cur_col_sum[j]
                
                output[i][j] = min(row_val, col_val)
                
                cur_row_sum[i] += output[i][j]
                cur_col_sum[j] += output[i][j]
                
        return output
sol = Solution()
print(sol.generateMatrix([1, 2, 3], [1, 2, 3]))