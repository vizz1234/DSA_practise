# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
class Solution:
    def findTarget(self, root, target): 
        # your code here.
        self.hashEle = {}
        self.target = target
        def recur(root):
            if not root:
                return False
            if self.target - root.data in self.hashEle:
                return True
            self.hashEle[root.data] = 1
            l = recur(root.left)
            r = recur(root.right)
            if l or r:
                return True
            return False
        return recur(root)
