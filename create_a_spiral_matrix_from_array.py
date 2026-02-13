class Solution:
    def spiralFill(self, n, m, arr):
        # code here
        left, right, top, bottom, cnt = 0, m - 1, 0, n - 1, 0
        mat = [[0] * m for _ in range(n)]
        while cnt < len(arr):
            for i in range(left, right + 1):
                if cnt >= len(arr):
                    return mat
                mat[top][i] = arr[cnt]
                cnt += 1
            top += 1
            for i in range(top, bottom + 1):
                if cnt >= len(arr):
                    return mat
                mat[i][right] = arr[cnt]
                cnt += 1
            right -= 1
            
            for i in range(right, left - 1, -1):
                if cnt >= len(arr):
                    return mat
                mat[bottom][i] = arr[cnt]
                cnt += 1
            bottom -= 1
            
            for i in range(bottom, top - 1, -1):
                if cnt >= len(arr):
                    return mat
                mat[i][left] = arr[cnt]
                cnt += 1
            left += 1
        return mat
sol = Solution()
print(sol.spiralFill(3, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9]))