from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        if len(s) < 11:
            return []
        
        d = {}
        output = []

        for i in range(10, len(s) + 1):
            seq = s[i-10:i]
            if seq in d:
                d[seq] += 1
                if d[seq] == 2:
                    output.append(seq)
            else:
                d[seq] = 1
        
        return output

sol = Solution()
print(sol.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))