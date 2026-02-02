class Solution:
    def minSum(self, arr):
        # code here
        if len(arr) == 0:
            return "0"
        if len(arr) == 1:
            return str(arr[0])
        arr.sort()
        s1 = []
        s2 = []
        for i in range(len(arr)):
            if i % 2 == 0:
                s1.append(arr[i])
            else:
                s2.append(arr[i])
        # print(s1, s2)
        res = []
        carry = 0
        i = len(s1) - 1
        j = len(s2) - 1
        while i >= 0 or j >= 0 or carry > 0:
            c1 = s1[i] if i >= 0 else 0
            c2 = s2[j] if j >= 0 else 0
            s = c1 + c2 + carry
            # print(c1, c2, s, s % 10)
            carry = s // 10
            res.append(str(s % 10))
            i -= 1
            j -= 1
            
        
        return ''.join(res[::-1]).lstrip("0")
sol = Solution()
print(sol.minSum([1, 2, 3, 4, 5]))