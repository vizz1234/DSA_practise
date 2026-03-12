class Solution:
    def hasTripletSum(self, arr, target):
        # Code Here
        n = len(arr)
        arr.sort()
        for i in range(n - 2):
            s = target - arr[i]
            l = i + 1
            r = n - 1
            while l < r:
                if arr[l] + arr[r] == s:
                    return True
                elif arr[l] + arr[r] < s:
                    l += 1
                else:
                    r -= 1
        return False
sol = Solution()
arr = [1, 2, 3, 4, 5]
target = 10
print(sol.hasTripletSum(arr, target))
arr[] = [1, 2, 4, 3, 6, 7]
target = 10
print(sol.hasTripletSum(arr, target))
[40, 20, 10, 3, 6, 7]
target = 24
print(sol.hasTripletSum(arr, target))
arr[] = [1, 4, 45, 6, 10, 8]
target = 13
print(sol.hasTripletSum(arr, target))
