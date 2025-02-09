class Solution:
    
    #Function to search a given number in row-column sorted matrix.
    def searchRowMatrix(self, mat, x): 
        # code here 
        n = len(mat)
        m = len(mat[0])
        for i in range(n):
            left = 0
            right = m - 1
            while left <= right:
                mid = (left + right) // 2
                if mat[i][mid] == x:
                    return True
                elif x > mat[i][mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False
obj = Solution()
print(obj.searchRowMatrix([[1,2,3],[4,5,6],[7,8,9]], 10))