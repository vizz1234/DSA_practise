class Solution:
    def countWays(self, s):
        # code here
        n = len(s)
        nS = (n + 1) // 2
        
        dpT = [[0] * nS for _ in range(nS)]
        dpF = [[0] * nS for _ in range(nS)]
        
        for i in range(nS):
            if s[i * 2] == 'T':
                dpT[i][i] = 1
            else:
                dpF[i][i] = 1
        
        for L in range(2, nS + 1):
            for i in range(nS - L + 1):
                
                j = i + L - 1
                
                for k in range(i, j):
                    
                    op = s[k * 2 + 1]
                    lt = dpT[i][k]
                    lf = dpF[i][k]
                    rt = dpT[k + 1][j]
                    rf = dpF[k + 1][j]
                    
                    if op == '&':
                        dpT[i][j] += lt * rt
                        dpF[i][j] += lf * rf + lf * rt + lt * rf
                    
                    if op == '|':
                        dpT[i][j] += lt * rt + lf * rt + lt * rf
                        dpF[i][j] += lf * rf
                    
                    if op == '^':
                        dpT[i][j] += lf * rt + lt * rf
                        dpF[i][j] += lt * rt + lf * rf
        
        return dpT[0][nS - 1]

sol = Solution()
print(sol.countWays("T|T&F^T"))