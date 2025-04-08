class Solution:
	def isWordExist(self, mat, word):
		#Code here
		if not word:
			return False
        
		word_len = len(word)
		m, n = len(mat), len(mat[0])
        
		directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
		def backtrack(r, c, idx):
			if idx == word_len:
				return True
            
			if r < 0 or r >= m or c < 0 or c >= n or mat[r][c] != word[idx]:
				return False
            
			temp = mat[r][c]
			mat[r][c] = '$'
            
			for direction in directions:
				dr, dc = direction[0], direction[1]
				if backtrack(r + dr, c + dc, idx + 1):
					return True
            
			mat[r][c] = temp
			return False

		for i in range(m):
			for j in range(n):
				if mat[i][j] == word[0]:
					if backtrack(i, j, 0):
						return True
		return False
                    