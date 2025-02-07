class Solution:
    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, mat):
        # code here
        n, m = len(mat), len(mat[0])
        output = []
        left, right, top, bottom, count = 0, m - 1, 0, n - 1, 0
        mn = m * n
        while count < mn:
            for i in range(left, right + 1):
                output.append(mat[top][i])
                count += 1
            top += 1
            
            for i in range(top, bottom + 1):
                output.append(mat[i][right])
                count += 1
            right -= 1
            
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    output.append(mat[bottom][i])
                    count += 1
                bottom -= 1
            
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    output.append(mat[i][left])
                    count += 1
                left += 1
        return output
obj = Solution()
print(obj.spirallyTraverse([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))