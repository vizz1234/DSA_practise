class Solution:
    def zeroSumSubmat(self, mat):
        # code here
        n = len(mat)
        m = len(mat[0])
        max_size = 0
        
        for r1 in range(n):
            col_sum = [0] * m
            
            for r2 in range(r1, n):
                
                for c1 in range(m):
                    col_sum[c1] += mat[r2][c1]
                
                prefix_sum = {0: -1}
                prefix = 0
                
                for c1 in range(m):
                    prefix += col_sum[c1]
                    if prefix in prefix_sum:
                        size = (r2 - r1 + 1) * (c1 - prefix_sum[prefix])
                        max_size = max(max_size, size)
                    else:
                        prefix_sum[prefix] = c1
        
        return max_size

sol = Solution()
mat = [[1, -1, -1], [1, -1, 1], [1, 1, 1]]
print(sol.zeroSumSubmat(mat))
mat = [[9, 7, 16, 5], [1, -6, -7, 3], [1, 8, 7, 9], [7, -2, 0, 10]]
print(sol.zeroSumSubmat(mat))
mat = [[1, 2, 3], [-3, -2, -1], [1, 7, 5]]
print(sol.zeroSumSubmat(mat))