class Solution:
    ##Complete this function
    def pairInSortedRotated(self,arr, target):
        #Your code here
        n = len(arr)
        pivot = n - 1
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                pivot = i
                break
        l = (pivot + 1) % n
        r = pivot
        while l != r:
            s = arr[l] + arr[r]
            if s == target:
                return True
            if s < target:
                l = (l + 1) % n
            else:
                r = (r - 1) % n
        return False
sol = Solution()
arr = [1, 2, 3, 4, 5]
target = 10
print(sol.pairInSortedRotated(arr, target))
arr = [7, 9, 1, 3, 5]
target = 6
print(sol.pairInSortedRotated(arr, target))
arr[] = [2, 3, 4, 1]
target = 3
print(sol.pairInSortedRotated(arr, target))
arr[] = [10, 7, 4, 1]
target = 9
print(sol.pairInSortedRotated(arr, target))
