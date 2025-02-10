class Solution:
    def setMatrixZeroes(self, mat):
        c0 = 0
        n, m = len(mat), len(mat[0])
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    if j == 0:
                        c0 = 1
                    else:
                        mat[0][j] = 0
                    mat[i][0] = 0
        
        for i in range(1, n):
            for j in range(1, m):
                if mat[i][0] == 0 or mat[0][j] == 0:
                    mat[i][j] = 0
        
        if mat[0][0] == 0:
            mat[0] = [0] * m
        
        if c0 == 1:
            for i in range(n):
                mat[i][0] = 0
        return mat
obj = Solution()
print(obj.setMatrixZeroes([[1,2,3],[4,0,6],[7,8,9]]))