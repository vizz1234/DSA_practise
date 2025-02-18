class Solution:
    #Function to find equilibrium point in the array.
    def findEquilibrium(self, arr):
        # code here
        pS = arr[0]
        tS = sum(arr)
        n = len(arr)
        for i in range(1, n):
            cur = (tS - arr[i])
            if pS == (cur) / 2:
                return i
            pS += arr[i]
        return -1
obj = Solution()
print(obj.findEquilibrium([1,3,5,2,2]))