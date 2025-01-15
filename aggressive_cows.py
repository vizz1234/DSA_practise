class Solution:
    
    def check(self, stalls, k, d):
        cnt = 1
        prev = stalls[0]
        n = len(stalls)
        for i in range(1, n):
            if stalls[i] - prev >= d:
                prev = stalls[i]
                cnt += 1
        return cnt >= k

    def aggressiveCows(self, stalls, k):
        stalls.sort()
        low = 1
        high = stalls[-1] - stalls[0]
        res = 0
        while low <= high:
            mid = (high + low) // 2
            if self.check(stalls, k, mid):
                res = mid
                low = mid + 1
            else:
                high = mid - 1
        return res
obj = Solution()
stalls = [6, 7, 9, 11, 13, 15]
obj.aggressiveCows(stalls, 4)