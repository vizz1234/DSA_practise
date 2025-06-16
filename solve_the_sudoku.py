# class Solution:
    
#     #Function to find a solved Sudoku. 

        
#     def solveSudoku(self, mat):
        
#         # Your code here
#         box = {}
#         row = {i:set() for i in range(9)}
#         col = {i:set() for i in range(9)}
#         boxCheck = {i:set() for i in range(9)}
#         for i in range(9):
#             for j in range(9):
#                 box[(i, j)] = (i//3) * 3 + (j//3)
#                 if mat[i][j] != 0:
#                     getBox = box[(i, j)]
#                     row[i].add(mat[i][j])
#                     col[j].add(mat[i][j])
#                     boxCheck[getBox].add(mat[i][j])

        
#         def emptyRC(mat):
#             for i in range(9):
#                 for j in range(9):
#                     if mat[i][j] == 0:
#                         return i, j
#             return -1, -1
        
#         def backtrack():
#             r, c = emptyRC(mat)
#             if r == -1:
#                 return True
                
#             getBox = box[(r, c)]
            
#             for i in range(1, 10):
#                 if i in row[r] or i in col[c] or i in boxCheck[getBox]:
#                     continue
#                 mat[r][c] = i
#                 row[r].add(i)
#                 col[c].add(i)
#                 boxCheck[getBox].add(i)
                
#                 if backtrack():
#                     return True
                    
#                 mat[r][c] = 0
#                 row[r].remove(i)
#                 col[c].remove(i)
#                 boxCheck[getBox].remove(i)
            
#             return False
                
#         backtrack()
#         return mat

#User function Template for python3

class Solution:
    
    #Function to find a solved Sudoku. 
    def solveSudoku(self, mat):
        
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        box_sets = [set() for _ in range(9)]
        
        # Your code here
        for i in range(9):
            for j in range(9):
                val = mat[i][j]
                if val == 0:
                    continue
                
                row_sets[i].add(val)
                col_sets[j].add(val)
                box_num = (i // 3) * 3 + (j // 3)
                box_sets[box_num].add(val)
        
        def backtrack():
            for i in range(9):
                for j in range(9):
                    val = mat[i][j]
                    if val == 0:
                        box = (i//3) * 3 + (j//3)
                        for num in range(1, 10):
                            if (num not in row_sets[i] and
                                num not in col_sets[j] and
                                num not in box_sets[box]):
                                    mat[i][j] = num
                                    row_sets[i].add(num)
                                    col_sets[j].add(num)
                                    box_sets[box].add(num)
                                    
                                    if backtrack():
                                        return True
                                    
                                    mat[i][j] = 0
                                    row_sets[i].remove(num)
                                    col_sets[j].remove(num)
                                    box_sets[box].remove(num)
                                
                        return False
            return True
        
        backtrack()
                            
