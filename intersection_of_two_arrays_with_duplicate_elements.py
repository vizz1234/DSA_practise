class Solution:
    def intersectionWithDuplicates(self, a, b):
        # code here
        d = {}
        n = len(a)
        m = len(b)
        output = set()
        for i in range(n):
            d[a[i]] = 1
        for j in range(m):
            if d.get(b[j], 0) != 0:
                output.add(b[j])
        return list(output)
obj = Solution()
print(obj.intersectionWithDuplicates([1,2,2,1,3], [2,2,3]))