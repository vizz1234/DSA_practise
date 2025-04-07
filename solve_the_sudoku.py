class Solution:
    
    #Function to find a solved Sudoku. 

        
    def solveSudoku(self, mat):
        
        # Your code here
        box = {}
        row = {i:set() for i in range(9)}
        col = {i:set() for i in range(9)}
        boxCheck = {i:set() for i in range(9)}
        for i in range(9):
            for j in range(9):
                box[(i, j)] = (i//3) * 3 + (j//3)
                if mat[i][j] != 0:
                    getBox = box[(i, j)]
                    row[i].add(mat[i][j])
                    col[j].add(mat[i][j])
                    boxCheck[getBox].add(mat[i][j])

        
        def emptyRC(mat):
            for i in range(9):
                for j in range(9):
                    if mat[i][j] == 0:
                        return i, j
            return -1, -1
        
        def backtrack():
            r, c = emptyRC(mat)
            if r == -1:
                return True
                
            getBox = box[(r, c)]
            
            for i in range(1, 10):
                if i in row[r] or i in col[c] or i in boxCheck[getBox]:
                    continue
                mat[r][c] = i
                row[r].add(i)
                col[c].add(i)
                boxCheck[getBox].add(i)
                
                if backtrack():
                    return True
                    
                mat[r][c] = 0
                row[r].remove(i)
                col[c].remove(i)
                boxCheck[getBox].remove(i)
            
            return False
                
        backtrack()
        return mat