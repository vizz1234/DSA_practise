def lisEndingAtIdx(arr, idx, memo):
  
    # Base case
    if idx == 0:
        return 1

    # Check if the result is already computed
    if memo[idx] != -1:
        return memo[idx]

    # Consider all elements on left of i,
    # recursively compute LISs ending with 
    # them and consider the largest
    mx = 1
    for prev in range(idx):
        if arr[prev] < arr[idx]:
            mx = max(mx, lisEndingAtIdx(arr, prev, memo) + 1)

    # Store the result in the memo array
    memo[idx] = mx
    return memo[idx]

def lis(arr):
    n = len(arr)

    memo = [-1] * n
  
    res = 1
    for idx in range(1, n):
        res = max(res, lisEndingAtIdx(arr, idx, memo))
    return res

if __name__ == "__main__":
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    print(lis(arr))