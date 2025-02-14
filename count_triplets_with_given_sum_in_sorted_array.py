class Solution:
    def countTriplets(self, arr, target):
        # code here
        n = len(arr)
        k = n - 1
        res = 0
        for i in range(n-2):
            j = i + 1
            k = n - 1
            while j < k:
                cS = arr[i] + arr[j] + arr[k]
                if cS < target:
                    j += 1
                elif cS > target:
                    k -= 1
                else:
                    e1 = arr[j]
                    e2 = arr[k]
                    c1 = 0
                    c2 = 0
                    while j <= k and arr[j] == e1:
                        j += 1
                        c1 += 1
                    while arr[k] == e2 and j <= k:
                        k -= 1
                        c2 += 1
                    if e1 == e2:
                        res += (c1 * (c1 - 1)) // 2
                    else:
                        res += c1 * c2
                    
        return res