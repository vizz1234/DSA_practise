class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def findUnion(self, a, b):
        # code here
        d = set()
        n, m = len(a), len(b)
        for i in range(n):
            d.add(a[i])
        for i in range(m):
            d.add(b[i])
        return len(d)
obj = Solution()
print(obj.findUnion([1,2,2,1,3], [2,2,3]))