class Solution:
    
    #Function to rotate matrix anticlockwise by 90 degrees.
    def rotateby90(self, mat): 
        # code here
        n = len(mat)
        for i in range(n):
            for j in range(i, n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        
        for i in range(n//2):
            for j in range(n):
                mat[i][j], mat[n-1-i][j] = mat[n-1-i][j], mat[i][j]
        return mat
obj = Solution()
print(obj.rotateby90([[1,2,3],[4,5,6],[7,8,9]]))