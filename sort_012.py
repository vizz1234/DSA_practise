def sort012(arr):
    # code here
    n = len(arr)
    zeroPointer = 0
    onePointer = 0
    twoPointer = n - 1
    while onePointer <= twoPointer:
        if arr[onePointer] == 0:
            arr[onePointer], arr[zeroPointer] = arr[zeroPointer], arr[onePointer]
            onePointer += 1
            zeroPointer += 1
        elif arr[onePointer] == 1:
            onePointer += 1
        else:
            arr[twoPointer], arr[onePointer] = arr[onePointer], arr[twoPointer]
            twoPointer -= 1
    return arr

print(sort012([0, 1, 2, 0, 1, 2]))