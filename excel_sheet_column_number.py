class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        num = 0
        n = len(columnTitle)

        for i in range(n):

            char = columnTitle[i]
            map_char = ord(char) - 64

            num = num * 26 + map_char
        
        return num

sol = Solution()
print(sol.titleToNumber("ZY"))