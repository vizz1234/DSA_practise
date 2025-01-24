def hIndex(citations):
    #code here
    n = len(citations)
    freq = [0] * (n + 1)
    for i in range(n):
        if citations[i] > n:
            freq[n] += 1
        else:
            freq[citations[i]] += 1
    h = freq[n]
    idx = n
    while h < idx:
        idx -= 1
        h += freq[idx]
    return idx

print(hIndex([3,0,6,1,5]))