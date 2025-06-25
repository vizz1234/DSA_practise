def maxOfMin(arr):
    n = len(arr)
    
    # Arrays to store previous and next smaller elements
    prev_smaller = [-1] * n
    next_smaller = [n] * n
    
    stack = []
    
    # Find previous smaller elements
    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            prev_smaller[i] = stack[-1]
        stack.append(i)
    
    # Clear stack for next use
    stack.clear()
    
    # Find next smaller elements
    for i in range(n-1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            next_smaller[i] = stack[-1]
        stack.append(i)
    
    # Initialize result array with 0s
    res = [0] * (n + 1)
    
    # Fill res[]: For each element, find length of window
    for i in range(n):
        length = next_smaller[i] - prev_smaller[i] - 1
        res[length] = max(res[length], arr[i])
    
    # Fill remaining entries by back-propagation
    for i in range(n - 1, 0, -1):
        res[i] = max(res[i], res[i + 1])
    
    # Final result (ignore res[0])
    return res[1:]

# Example usage
if __name__ == '__main__':
    arr = [10, 20, 30, 50, 10, 70, 30]
    result = maxOfMin(arr)
    print(' '.join(map(str, result)))
