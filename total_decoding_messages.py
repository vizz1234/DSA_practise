class Solution:
    def countWays(self, digits):
        # Code here
        if not digits or digits[0] == '0':
            return 0
        
        n = len(digits)
        prev, curr = 1, 1
        
        for i in range(1, n):
            temp = 0
            if digits[i] != '0':
                temp += curr

            twoDigit = int(digits[i-1:i+1])
            if 10 <= twoDigit <= 26:
                temp += prev
            
            prev = curr
            curr = temp
        
        return curr

sol = Solution()
print(sol.countWays("123"))