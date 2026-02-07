#User function Template for python3
class Solution:

    def findMaximum(self, arr):
        # code here
        n = len(arr)
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
                return arr[mid]
            elif arr[mid] > arr[mid + 1]:
                right = mid - 1
            elif arr[mid] < arr[mid + 1]:
                left = mid + 1
        return arr[n - 1]
sol = Solution()
print(sol.findMaximum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))