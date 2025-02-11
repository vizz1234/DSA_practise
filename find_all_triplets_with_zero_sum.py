class Solution:
    def findTriplets(self, arr):
        # Your code here
        output = set()
        d = {}
        n = len(arr)
        for i in range(n):
            for j in range(i+1, n):
                s = arr[i] + arr[j]
                if s not in d:
                    d[s] = []
                d[s].append([i, j])
        
        for i in range(n):
            s = -arr[i]
            if s in d:
                for idx in d[s]:
                    if idx[0] != i and idx[1] != i:
                        j = idx[0]
                        k = idx[1]
                        triplet = sorted([i, j, k])
                        output.add(tuple(triplet))
        
        output = [list(t) for t in output]
        
        return output
obj = Solution()
print(obj.findTriplets([0, -1, 2, -3, 1]))