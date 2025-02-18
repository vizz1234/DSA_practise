class Solution:
    def maxWater(self, arr):
        # code here
        if len(arr) < 3:
            return 0
        n = len(arr)
        lMax = arr[0]
        rMax = arr[-1]
        left = 1
        right = n - 2
        res = 0
        while left <= right:
            if lMax < rMax:
                if arr[left] < lMax:
                    res += lMax - arr[left]
                else:
                    lMax = arr[left]
                left += 1
            else:
                if arr[right] < rMax:
                    res += rMax - arr[right]
                else:
                    rMax = arr[right]
                right -= 1
        return res
obj = Solution()
print(obj.maxWater([0,1,0,2,1,0,1,3,2,1,2,1]))