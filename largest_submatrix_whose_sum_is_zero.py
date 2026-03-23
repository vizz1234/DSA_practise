class Solution:
    def zeroSumSubmat(self, mat):
        n = len(mat)
        m = len(mat[0])
        ans = 0

        for r1 in range(n):
            # colSum[c] = sum of column c from row r1 to r2
            colSum = [0] * m

            for r2 in range(r1, n):
                # Extend colSum to include row r2
                for c in range(m):
                    colSum[c] += mat[r2][c]

                # Now find the largest zero-sum subarray in colSum[]
                # using prefix sums + hashmap
                prefix_map = {0: -1}  # prefix_sum -> first index seen
                prefix = 0

                for c in range(m):
                    prefix += colSum[c]

                    if prefix in prefix_map:
                        # Zero-sum subarray found from prefix_map[prefix]+1 to c
                        width = c - prefix_map[prefix]
                        height = r2 - r1 + 1
                        ans = max(ans, height * width)
                    else:
                        prefix_map[prefix] = c

        return ans
sol = Solution()
mat = [[1, -1, -1], [1, -1, 1], [1, 1, 1]]
print(sol.zeroSumSubmat(mat))
mat = [[9, 7, 16, 5], [1, -6, -7, 3], [1, 8, 7, 9], [7, -2, 0, 10]] 
print(sol.zeroSumSubmat(mat))