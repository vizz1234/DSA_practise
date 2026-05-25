class Solution:
    def catchThieves(self, arr, k):
        #code here
        n = len(arr)
        pl = [i for i in range(n) if arr[i] == 'P']
        tl = [i for i in range(n) if arr[i] == 'T']
        p = t = count = 0
        
        while p < len(pl) and t < len(tl):
            if abs(pl[p] - tl[t]) <= k:
                count += 1
                p += 1
                t += 1
            
            elif tl[t] < pl[p] - k:
                t += 1
            
            elif pl[p] < tl[t] - k:
                p += 1
        
        return count


sol = Solution()
print(sol.catchThieves(["P", "T", "T", "P", "T", "P"], 2))
