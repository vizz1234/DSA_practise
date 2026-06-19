from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')
        def inorder(node):
            if not node:
                return 0
            left = max(inorder(node.left), 0)
            right = max(inorder(node.right), 0)
            sub_path_sum = left + node.val + right
            self.max_sum = max(sub_path_sum, self.max_sum)
            return node.val + max(left, right)
        inorder(root)
        return self.max_sum

root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
sol = Solution()
print(sol.maxPathSum(root))