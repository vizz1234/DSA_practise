from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        output = []

        def backtrack(i, cur_arr):

            s = sum(cur_arr)
            cl = len(cur_arr)

            if s == n and cl == k:
                output.append(cur_arr)
                return
            
            if s > n or cl > k or i >= 9:
                return
            
            backtrack(i + 1, cur_arr + [i + 1])
            backtrack(i + 1, cur_arr)
        
        backtrack(0, [])
        return output
        
sol = Solution()
print(sol.combinationSum3(3, 7)) 
print(sol.combinationSum3(3, 9))     