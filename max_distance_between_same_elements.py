class Solution:
    # Your task is to Complete this function
    # functtion should return an integer
    def maxDistance(self, arr):
        # Code here
        d = {}
        max_dist = 0
        for i, num in enumerate(arr):
            if num not in d:
                d[num] = i
            else:
                dist = i - d[num]
                max_dist = max(dist, max_dist)
        return max_dist
sol = Solution()
print(sol.maxDistance([1, 1, 2, 2, 2, 1]))