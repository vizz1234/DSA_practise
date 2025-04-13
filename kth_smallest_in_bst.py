

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    # Return the kth smallest element in the given BST 
    def kthSmallest(self, root, k): 
        #code here.
        minCnt = 0
        curr = root
        while curr:
            if not curr.left:
                minCnt += 1
                if minCnt == k:
                    return curr.data
                curr = curr.right
            else:
                pre = curr.left
                while pre.right and pre.right != curr:
                    pre = pre.right
                if not pre.right:
                    pre.right = curr
                    curr = curr.left
                else:
                    pre.right = None
                    minCnt += 1
                    if minCnt == k:
                        return curr.data
                    curr = curr.right
        return -1
