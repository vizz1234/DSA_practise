class Solution:
	def matSearch(self, mat, x):
		# Complete this function
		r = len(mat)
		c = len(mat[0])
		i, j = 0, c - 1
		while i < r and j >= 0:
			if x > mat[i][j]:
				i += 1
			elif x < mat[i][j]:
				j -= 1
			else:
				return True
		return False
obj = Solution()
print(obj.matSearch([[1,2,3],[4,5,6],[7,8,9]], 10))