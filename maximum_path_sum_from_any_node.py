
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    #Function to return maximum path sum from any node in a tree.
    def recurMax(self, root):
        if not root:
            return 0
        
        l = max(0, self.recurMax(root.left))
        r = max(0, self.recurMax(root.right))
        
        self.res = max(self.res, l + r + root.data)
        
        return root.data + max(l, r)
        
    def findMaxSum(self, root): 
        #Your code here
        self.res = root.data
        
        self.recurMax(root)
        
        return self.res