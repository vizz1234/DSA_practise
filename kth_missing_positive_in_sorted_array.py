def kthMissing(arr, k):
    # code here
    n = len(arr)
    res = n + k
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > mid + k:
            res = mid + k
            high = mid - 1
        else:
            low = mid + 1
    return res
print(kthMissing([2, 3, 5, 6], 2))