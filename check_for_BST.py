class Solution:
    #Function to check whether a Binary Tree is BST or not.
    def isBST(self, root):
        #code here
        def recurBST(root, minVal, maxVal):
            if not root:
                return True
            
            if root.data < minVal or root.data > maxVal:
                return False
            
            return recurBST(root.left, minVal, root.data - 1) and recurBST(root.right, root.data + 1, maxVal)
            
        return recurBST(root, float('-inf'), float('inf'))