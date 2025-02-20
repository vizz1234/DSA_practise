class Solution:
    def productExceptSelf(self, arr):
        #code here
        output = []
        n = len(arr)
        p = 1
        c = 0
        for i in range(n):
            if arr[i] != 0:
                p = p * arr[i]
            else:
                c += 1
                zI = i
        if c > 1:
            return [0] * n
        if c == 1:
            output[:] = [0] * n
            output[zI] = p
            return output
            
        for i in range(n):
            if arr[i] == 0:
                output.append(p)
                continue
            output.append(p//arr[i])
        return output
obj = Solution()
print(obj.productExceptSelf([1,2,3,4]))