class Solution:
    def closest3Sum(self, arr, target):
        # code here
        min_target_gap = float('inf')
        close_sum = float('-inf')
        n = len(arr)
        arr.sort()
        for i in range(n - 2):
            l = i + 1
            r = n - 1
            num = arr[i]
            while l < r:
                s = num + arr[l] + arr[r]
                cur_target_gap = abs(s - target)
                if cur_target_gap < min_target_gap:
                    min_target_gap = cur_target_gap
                    close_sum = s
                elif cur_target_gap == min_target_gap:
                    close_sum = max(s, close_sum)
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    return s
        return close_sum
sol = Solution()
arr = [1, 2, 3, 4, 5]
target = 10
print(sol.closest3Sum(arr, target))
arr = [-1, 2, 2, 4]
target = 4
print(sol.closest3Sum(arr, target))
