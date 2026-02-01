class Solution:
    def canAttend(self, arr):
        # Code Here
        if len(arr) < 2:
            return True
        arr.sort(key = lambda x: x[1])
        prev_end = arr[0][1]
        for i in range(1, len(arr)):
            start_time = arr[i][0]
            end_time = arr[i][1]
            if start_time >= prev_end:
                prev_end = end_time
            else:
                return False
        return True
sol = Solution()
print(sol.canAttend([[0, 30], [5, 10], [15, 20]]))