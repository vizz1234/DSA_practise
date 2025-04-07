class Solution:
    def nQueen(self, n):
        # code here
        col = set()
        majorDiag = set() # r + c
        minorDiag = set() # r - c
        res = []
        board = []
        def backtrack(r):
            if r == n:
                res.append(board[:])
                return
            for c in range(n):
                if c in col or r + c in majorDiag or r - c in minorDiag:
                    continue
                col.add(c)
                majorDiag.add(r + c)
                minorDiag.add(r - c)
                board.append(c + 1)
                
                backtrack(r + 1)
                
                col.remove(c)
                majorDiag.remove(r + c)
                minorDiag.remove(r - c)
                board.pop()
        
        backtrack(0)
        return res

# Example usage:
sol = Solution()
n = 4
print(sol.nQueen(n))
