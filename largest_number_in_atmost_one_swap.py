class Solution:
    def largestSwap(self, s):
        #code here
        n = len(s)
        s = list(s)
        
        for i in range(n):
            max_char = s[i]
            for j in range(i+1, n):
                if s[j] >= max_char:
                    idx = j
                    max_char = s[j]
            
            if max_char > s[i]:
                s[i], s[idx] = s[idx], s[i]
                break
        
        return ''.join(s)

sol = Solution()
print(sol.largestSwap("25461"))
print(sol.largestSwap("12345"))
