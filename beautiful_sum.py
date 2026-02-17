class Solution:
    def balanceSums(self, mat):
        # code here
        max_sum = -1
        n = len(mat)
        m = len(mat[0])
        total_sum = 0
        for i in range(n):
            cur_sum = sum(mat[i])
            max_sum = max(max_sum, cur_sum)
            total_sum += cur_sum
        for j in range(m):
            cur_sum = 0
            for i in range(n):
                cur_sum += mat[i][j]
            max_sum = max(max_sum, cur_sum)
        return max_sum * n - total_sum
sol = Solution()
print(sol.balanceSums([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))