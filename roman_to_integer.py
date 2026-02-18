class Solution:
    def romanToDecimal(self, s): 
        # code here
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        n = len(s)
        num = d[s[n - 1]]
        for i in range(n - 2, -1, -1):
            if d[s[i]] < d[s[i + 1]]:
                num -= d[s[i]]
            else:
                num += d[s[i]]
        return num
sol = Solution()
print(sol.romanToDecimal("MCMXCIV"))