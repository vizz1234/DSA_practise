class Solution:
    def reverseArray(self, arr):
        # code here
        n = len(arr)
        for i in range(n//2):
            arr[i], arr[n-1-i] = arr[n-1-i], arr[i]
        return arr
obj = Solution()
print(obj.reverseArray([1,2,3,4,5]))