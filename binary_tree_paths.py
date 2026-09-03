from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        output = []

        def recur(node, s):

            if not node:
                return
            
            if s == '':
                s = str(node.val)
            
            else:
                s = s + '->' + str(node.val)
            
            if not node.left and not node.right:
                output.append(s)
                return
            
            recur(node.left, s)
            recur(node.right, s)

        
        recur(root, '')

        return output    

sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(sol.binaryTreePaths(root))