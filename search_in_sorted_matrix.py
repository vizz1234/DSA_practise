class Solution:
    
    #Function to search a given number in row-column sorted matrix.
    def searchMatrix(self, mat, x): 
        # code here 
        n = len(mat)
        m = len(mat[0])
        left, right = 0, n * m - 1
        while left <= right:
            mid = (left + right) // 2
            i = mid // m
            j = mid % m
            if x > mat[i][j]:
                left = mid + 1
            elif x < mat[i][j]:
                right = mid - 1
            else:
                return True
        return False
obj = Solution()
print(obj.searchMatrix([[1,2,3],[4,5,6],[7,8,9]], 10))