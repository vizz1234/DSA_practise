class Solution:
    def mergeArrays(self, a, b):
    # Get lengths of both arrays
        m, n = len(a), len(b)
        
        # Start from the end of first array
        i = m - 1
        # Start from beginning of second array
        j = 0
        
        # Compare and swap elements while i >= 0 and j < n
        while i >= 0 and j < n:
            if a[i] > b[j]:
                # Swap elements if element in first array is greater
                a[i], b[j] = b[j], a[i]
                i -= 1
                j += 1
            else:
                # If element in first array is smaller or equal, stop
                break
        
        # Sort both arrays
        a.sort()
        b.sort()
        
        return a, b
