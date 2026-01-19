class Solution:
    def inversionCount(self, arr):
        # Code Here
        n = len(arr)
        if n < 2:
            return 0
        temp = [0] * n
        
        def merge_sort(l, r):
            if l >= r:
                return 0
            m = (l + r) // 2
            inv = merge_sort(l, m)
            inv += merge_sort(m + 1, r)
            inv += merge(l, m, r)
            return inv
        
        def merge(l, m, r):
            i, j, k = l, m + 1, l
            inv = 0
            while i <= m and j <= r:
                if arr[i] <= arr[j]:
                    temp[k] = arr[i]
                    i += 1
                else:
                    temp[k] = arr[j]
                    j += 1
                    inv += (m - i + 1)
                k += 1
            while i <= m:
                temp[k] = arr[i]
                i += 1
                k += 1
            while j <= r:
                temp[k] = arr[j]
                j += 1
                k += 1
            for idx in range(l, r + 1):
                arr[idx] = temp[idx]
            return inv
        return merge_sort(0, n - 1)
sol = Solution()
print(sol.inversionCount([1,2,3,4,5,6,7,8,9,10]))