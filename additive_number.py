class Solution:
    def isAdditiveNumber(self, num: str) -> bool:

        n = len(num)
        self.bool = False

        if n < 3:
            return False

        def recur(idx, cur_seq):

            # print(cur_seq)

            if idx == n:
                if len(cur_seq) > 2 and int(cur_seq[-1]) == int(cur_seq[-2]) + int(cur_seq[-3]):
                    self.bool = True
                else:
                    return False
            
            if self.bool:
                return True
            
            if len(cur_seq) > 2:

                if int(cur_seq[-1]) == int(cur_seq[-2]) + int(cur_seq[-3]):
                    recur(idx + 1, cur_seq + [num[idx]])
                    
                if cur_seq[-1] != '0':
                    recur(idx + 1, cur_seq[:-1] + [cur_seq[-1] + num[idx]])
            
            else:

                recur(idx + 1, cur_seq + [num[idx]])

                if cur_seq and cur_seq[-1] != '0':
                    recur(idx + 1, cur_seq[:-1] + [cur_seq[-1] + num[idx]])
        
        recur(0, [])
        return self.bool 

sol = Solution()
print(sol.isAdditiveNumber("112358"))