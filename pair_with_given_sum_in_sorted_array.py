class Solution:
    def countPairs (self, arr, target) : 
        #Complete the function
        res = 0
        n = len(arr)
        left, right = 0, n - 1
        while left < right:
            s = arr[left] + arr[right]
            if s == target:
                e1 = arr[left]
                e2 = arr[right]
                c1 = 0
                c2 = 0
                while left <= right and arr[left] == e1:
                    c1 += 1
                    left += 1
                while left <= right and arr[right] == e2:
                    c2 += 1
                    right -= 1
                if e1 == e2:
                    res += (c1 * (c1 - 1)) // 2
                else:
                    res += c1 * c2
            elif s < target:
                left += 1
            else:
                right -= 1
        return res
obj = Solution()
print(obj.countPairs([1,2,3,4,5], 5))