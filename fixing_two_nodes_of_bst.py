
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def correctBST(self, root):
        # your code here
        self.inorder = []
        def inorderTraversal(root):
            if not root:
                return None
            inorderTraversal(root.left)
            self.inorder.append(root)
            inorderTraversal(root.right)
        inorderTraversal(root)
        first = None
        middle = None
        last = None
        for i in range(1, len(self.inorder)):
            data = self.inorder[i].data
            prev_data = self.inorder[i-1].data
            if data < prev_data:
                if not first:
                    first = self.inorder[i-1]
                    middle = self.inorder[i]
                else:
                    last = self.inorder[i]
        if not last:
            last = middle
        first.data, last.data = last.data, first.data