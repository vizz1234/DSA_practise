from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def node_height(self, node):
        if not node or self.flag:
            return -1
        left = 1 + self.node_height(node.left)
        right = 1 + self.node_height(node.right)

        if abs(left - right) > 1:
            self.flag = 1
        
        return max(left, right)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        self.flag = 0
        lh = self.node_height(root.left)
        rh = self.node_height(root.right)

        if self.flag or abs(lh - rh) > 1:
            return False
        
        return True
        
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

sol = Solution()
print(sol.isBalanced(root))

        