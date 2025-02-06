class Solution:
    def minRemoval(self, intervals):
        intervals.sort()
        i = 1
        n = len(intervals)
        count = 0
        start, end = intervals[0][0], intervals[0][1]
        while i < n:
            if intervals[i][0] >= end:
                start, end = intervals[i][0], intervals[i][1]
                i += 1
            else:
                start = max(start, intervals[i][0])
                end = min(end, intervals[i][1])
                count += 1
                i += 1
        return count
obj = Solution()
print(obj.minRemoval([[1,2],[2,3],[3,4],[1,3]]))