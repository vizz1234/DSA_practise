class Solution:
    #Function to count the number of possible triangles.
    def countTriangles(self, arr):
        # code here
        n = len(arr)
        arr.sort()
        res = 0
        for i in range(2, n):
            j = 0
            k = i - 1
            while j < k:
                if arr[j] + arr[k] > arr[i]:
                    res += k - j
                    k -= 1
                else:
                    j += 1
        return res
obj = Solution()
print(obj.countTriangles([1,2,3,4,5]))