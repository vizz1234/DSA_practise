# Python program to find the longest subarray where the
# absolute difference between any two elements is not
# greater than X

from collections import deque

# Functio+1n that prints the longest sub-array
# where the absolute difference between any
# two element is not greater than X
def longestSubarray(arr, x):
    
    # Monotonic Queue to store maximum and minimum elements
    minQueue = deque()
    maxQueue = deque()
    
    # Pointers to mark the range of current subarray
    n = len(arr)
    start = end = 0
    
    # Pointers to mark the range of maximum subarray
    resStart = resEnd = 0
    while end < n:
        
        # Pop the elements greater than current element
        # from min Queue
        while minQueue and arr[minQueue[-1]] > arr[end]:
            minQueue.pop()
            
        # Pop the elements smaller than current element
        # from max Queue
        while maxQueue and arr[maxQueue[-1]] < arr[end]:
            maxQueue.pop()
            
        # Push the current index to both the queues
        minQueue.append(end)
        maxQueue.append(end)
        
        # Check if the subarray has maximum difference less
        # than X
        while arr[maxQueue[0]] - arr[minQueue[0]] > x:
                   
            # Reduce the length of sliding window by moving
            # the start pointer
            if start == minQueue[0]:
                minQueue.popleft()
            if start == maxQueue[0]:
                maxQueue.popleft()
            start += 1
        
        # Maximize the subarray length
        if end - start > resEnd - resStart:
            resStart, resEnd = start, end

        end += 1

    # Return the longest sub-array
    return arr[resStart:resEnd+1]

if __name__ == "__main__":
    arr = [8, 4, 2, 6, 7]
    x = 4

    res = longestSubarray(arr, x)
    
    print(*res)