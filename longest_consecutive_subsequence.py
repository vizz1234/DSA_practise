class Solution:
    
    # arr[] : the input array
    
    #Function to return length of longest subsequence of consecutive integers.
    def longestConsecutive(self,arr):
        #code here
        longest = 0
        arrSet = set(arr)
        n = len(arr)
        for i in range(n):
            cur = arr[i]
            if cur - 1 not in arrSet:
                curNum = cur
                count = 1
                while curNum + 1 in arrSet:
                    count += 1
                    curNum += 1
                longest = max(longest, count)
        return longest
obj = Solution()
print(obj.longestConsecutive([1,2,2,1,3]))