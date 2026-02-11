class Solution:
    def medianOf2(self, a, b):
        # code here
        if len(a) > len(b):
            a, b = b, a
        
        m = len(a)
        n = len(b)
        total = m + n
        half = total // 2
        
        left, right = 0, m
        
        while True:
            i = (left + right) // 2
            j = half - i
            
            Aleft = a[i - 1] if i > 0 else float('-inf')
            Aright = a[i] if i < m else float('inf')
            Bleft =  b[j - 1] if j > 0 else float('-inf')
            Bright = b[j] if j < n else float('inf')
            
            if Aleft <= Bright and Bleft <= Aright:
                
                if total % 2:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            
            elif Aleft > Bright:
                right = i - 1
            
            else:
                left = i + 1
sol = Solution()
print(sol.medianOf2([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))