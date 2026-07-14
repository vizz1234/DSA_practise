from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
        
        stack = [root]
        result = []

        while stack:
            n = stack[-1]
            if not n.left and not n.right:
                n = stack.pop()
                result.append(n.val)
            if n.right:
                stack.append(n.right)
                n.right = None
            if n.left:
                stack.append(n.left)
                n.left = None

        return result

head = TreeNode(1)
head.left = TreeNode(2)
head.right = TreeNode(3)

sol = Solution()
print(sol.postorderTraversal(head))