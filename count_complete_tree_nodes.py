from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        def left_height(node):

            if not node:
                return 0
            
            return 1 + left_height(node.left)
        
        def right_height(node):

            if not node:
                return 0
            
            return 1 + right_height(node.right)
        
        lh = left_height(root)
        rh = right_height(root)

        if lh == rh:
            return (1 << lh) - 1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
print(sol.countNodes(root))