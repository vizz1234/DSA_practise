
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def recurPath(self, root, curSum, prefixSum):
        if not root:
            return 0
        
        curSum += root.data
        countPath = 0
        
        if curSum == self.k:
            countPath += 1
        
        if curSum - self.k in prefixSum:
            countPath += prefixSum[curSum - self.k]
        prefixSum[curSum] = prefixSum.get(curSum, 0) + 1
        
        countPath += self.recurPath(root.left, curSum, prefixSum)
        countPath += self.recurPath(root.right, curSum, prefixSum)
        
        prefixSum[curSum] -= 1
        
        return countPath
            
    def sumK(self,root,k):
        # code here
        self.k = k
        return self.recurPath(root, 0, {})