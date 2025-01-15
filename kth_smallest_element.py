def kthElement(a, b, k):
    n = len(a)
    m = len(b)
    if n > m:
        return kthElement(b, a, k)
    
    low, high = max(0, k-m), min(k, n)
    while low <= high:
        leftPartitionIndex = (low + high) // 2
        rightPartitionIndex = k - leftPartitionIndex
        aLeft = a[leftPartitionIndex - 1] if leftPartitionIndex > 0 else float('-inf')
        aRight = a[leftPartitionIndex] if leftPartitionIndex < n else float('inf')
        bLeft = b[rightPartitionIndex - 1] if rightPartitionIndex > 0 else float('-inf')
        bRight = b[rightPartitionIndex] if rightPartitionIndex < m else float('inf')
        
        if aLeft <= bRight and bLeft <= aRight:
            return max(aLeft, bLeft)
        
        elif aLeft > bRight:
            high = leftPartitionIndex - 1
        
        else:
            low = leftPartitionIndex + 1

a = [4, 5, 6, 6, 13]
b = [4, 4, 5, 6, 6, 7, 8, 9, 9, 11, 12, 13]
k = 9
print(kthElement(a, b, k))