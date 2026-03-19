#User function Template for python3
class Solution:
    def touchedXaxis(self, arr):
        # code here
        if len(arr) == 0:
            return 0
        count = 0
        s = arr[0]
        n = len(arr)
        for i in range(1, n):
            cur_s = s + arr[i]
            if (s < 0 and cur_s >= 0) or (s > 0 and cur_s <= 0):
                count += 1
            s = cur_s
        return count
arr = [2, 5, -9, 4]
obj = Solution()
print(obj.touchedXaxis(arr))
arr = [4, -6, 2, 8, -2, 3, -12]
print(obj.touchedXaxis(arr))
arr = [1, 3, 5]
print(obj.touchedXaxis(arr)) #expected 0
