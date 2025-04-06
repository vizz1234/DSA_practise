class Solution:
    def findPermutation(self, s):
        # Code here
        res = []
        sl = list(s)
        def recPer(index, s):
            if index == len(s):
                res.append(''.join(s))
                return
            for i in range(index, len(s)):
                s[index], s[i] = s[i], s[index]
                recPer(index + 1, s)
                s[index], s[i] = s[i], s[index]
        recPer(0, sl)
        return list(set(res))

# Example usage:
sol = Solution()
s = "ABC"
print(sol.findPermutation(s))
