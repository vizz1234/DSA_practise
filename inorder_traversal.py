class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def inOrder(self,root):
        # code here
        res = []
        curr = root
        
        while curr:
            if curr.left:
                prev = curr.left
                while prev.right and prev.right != curr:
                    prev = prev.right
                
                if not prev.right:
                    prev.right = curr
                    curr = curr.left
                
                else:
                    prev.right = None
                    res.append(curr.data)
                    curr = curr.right
            
            else:
                res.append(curr.data)
                curr = curr.right
        
        return res