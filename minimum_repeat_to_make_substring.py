class Solution:
    def minRepeats(self, s1, s2):
        # code here 
        s = s1
        count = 1
        while len(s) < len(s2):
            s += s1
            count += 1
        
        if s2 in s:
            return count
        
        s += s1
        if s2 in s:
            return count + 1
        return -1