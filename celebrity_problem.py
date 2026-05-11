class Solution:
    def celebrity(self, mat):
        # code here
        n = len(mat)
        stack = list(range(n))
        
        while len(stack) > 1:
            
            a = stack.pop()
            b = stack.pop()
            
            if mat[a][b] == 1:
                stack.append(b)
            else:
                stack.append(a)
        
        candidate = stack[0]
        
        for i in range(n):
            if i == candidate:
                continue
            if mat[i][candidate] == 0 or mat[candidate][i] == 1:
                return -1
        
        return candidate

mat = [[1, 1, 0],
        [0, 1, 0],
        [0, 1, 1]]
sol = Solution()
print(sol.celebrity(mat))