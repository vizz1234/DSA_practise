class Solution:
    def convertToTitle(self, columnNumber: int) -> str:

        sheet = ''

        while columnNumber > 0:

            columnNumber -= 1
            sheet = chr(ord('A') + columnNumber % 26) + sheet
            columnNumber = columnNumber // 26
        
        return sheet

sol = Solution()
print(sol.convertToTitle(1))
print(sol.convertToTitle(28))
print(sol.convertToTitle(701))