class Solution:
    def isPalinSent(self, s):
        # code here
        left = 0
        right = len(s) - 1
        s = s.lower()
        numeric_set = set([48 + i for i in range(10)])
        alpha_set = set([97 + i for i in range(26)])
        
        while left < right:
            left_c = s[left]
            right_c = s[right]
            if ord(left_c) not in numeric_set and ord(left_c) not in alpha_set:
                left += 1
                continue
            if ord(right_c) not in numeric_set and ord(right_c) not in alpha_set:
                right -= 1
                continue
            if left_c != right_c:
                return False
            left += 1
            right -= 1
        return True
sol = Solution()
print(sol.isPalinSent("A man, a plan, a canal: Panama"))