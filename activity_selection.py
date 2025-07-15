class Solution:
    def activitySelection(self, start, finish):
        #code here
        fSZip = list(zip(finish, start))
        fSZip = sorted(fSZip, key = lambda x : x[0])
        
        count = 1
        n = len(start)
        lastFinish = fSZip[0][0]
        
        for i in range(1, n):
            if fSZip[i][1] > lastFinish:
                count += 1
                lastFinish = fSZip[i][0]
        
        return count

sol = Solution()
print(sol.activitySelection([1, 3, 2, 5], [2, 4, 3, 6]))