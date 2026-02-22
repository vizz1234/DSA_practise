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