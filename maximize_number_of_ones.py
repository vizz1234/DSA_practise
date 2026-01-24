class Solution:
    def maxOnes(self, arr, k):
        # code here
        l = 0
        most = 0
        zeros = 0
        
        for r in range(len(arr)):
            if arr[r] == 0:
                zeros += 1
            
            while zeros > k:
                if arr[l] == 0:
                    zeros -= 1
                l += 1
            
            most = max(most, r - l + 1)
        
        return most