class Solution:
    def power(self, b: float, e: int) -> float:
        # Code Here
        if e == 0:
            return 1
        if e < 0:
            return 1 / self.power(b, -e)
        
        half = self.power(b, e//2)
        
        if e % 2 == 0:
            return half * half
        
        else:
            return b * half * half

# Example usage:
sol = Solution()
print(sol.power(2, 3))  # Output: 8
print(sol.power(2, -3)) # Output: 0.125
print(sol.power(2, 0))  # Output: 1

