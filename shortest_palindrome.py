class Solution:
    def shortestPalindrome(self, s: str) -> str:

        rev = s[::-1]
        combined = s + '#' + rev
        n = len(combined)

        lps = [0] * n
        length = 0

        for i in range(1, n):
            while length > 0 and combined[i] != combined[length]:
                length = lps[length - 1]
            
            if combined[i] == combined[length]:
                length += 1
                lps[i] = length
        
        longest_pal_prefix = lps[-1]

        return rev[:len(s) - longest_pal_prefix] + s

sol = Solution()
print(sol.shortestPalindrome("aacecaaa"))
print(sol.shortestPalindrome("abcd"))