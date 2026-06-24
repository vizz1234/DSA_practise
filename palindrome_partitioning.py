from collections import defaultdict
from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        self.memo = defaultdict(list)
        self.memo[''] = [[]]
        
        def backtrack(s):
            if s in self.memo:
                return self.memo[s]
            res = []
            for i in range(1, len(s) + 1):
                if s[:i] == s[:i][::-1]:
                    for subs in backtrack(s[i:]):
                        res.append([s[:i]] + subs)
            self.memo[s] = res
            return res
        
        return backtrack(s)

sol = Solution()
print(sol.partition("aab"))