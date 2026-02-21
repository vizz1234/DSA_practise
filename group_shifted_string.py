class Solution:
    def groupShiftedString(self, arr):
        #code here
        if len(arr) == 1:
            return [arr]
        d = {}
        
        for word in arr:
            l = len(word)
            key = '0'
            num = ord(word[0])
            for i in range(1, l):
                key += str((ord(word[i]) - num) % 26)
            len_key = (l, key)
            if len_key not in d:
                d[len_key] = []
            d[len_key].append(word)
        
        output = [[] for _ in range(len(d))]
        
        i = 0
        for key, val in d.items():
            output[i][:] = val[:]
            i += 1
        
        return output
sol = Solution()
arr = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
print(sol.groupShiftedString(arr))