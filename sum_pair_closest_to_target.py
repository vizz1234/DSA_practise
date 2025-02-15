class Solution:
    def sumClosest(self, arr, target):
        # code here
        arr.sort()
        output = []
        cS = float('inf')
        left = 0
        n = len(arr)
        right = n - 1
        while left < right:
            s = arr[left] + arr[right]
            if s == target:
                return [arr[left], arr[right]]
            if abs(s - target) < cS:
                output[:] = [arr[left], arr[right]]
                cS = abs(s - target)
            if s < target:
                left += 1
            else:
                right -= 1
        return output
obj = Solution()
print(obj.sumClosest([1,2,4,5,7], 10))