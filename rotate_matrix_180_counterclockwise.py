class Solution:
    def rotateMatrix(self, mat):
        # Code here
        n = len(mat)
        
        for i in range(n // 2):
            for j in range(n):
                mat[i][j], mat[n - 1 - i][n - 1 - j] = mat[n - 1 - i][n - 1 - j], mat[i][j]
        
        if n % 2 == 1:

            mid = n // 2
            for j in range(n // 2):
                mat[mid][j], mat[mid][n - 1 - j] = mat[mid][n - 1 - j], mat[mid][j]
        return mat
sol = Solution()
print(sol.rotateMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))