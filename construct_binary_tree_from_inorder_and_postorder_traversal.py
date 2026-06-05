from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_idx = {val:i for i, val in enumerate(inorder)}
        def recur(left_idx, right_idx):
            if left_idx > right_idx:
                return None

            root_ele = postorder.pop()
            root = TreeNode(root_ele)
            mid = inorder_idx[root_ele]
            root.right = recur(mid + 1, right_idx)
            root.left = recur(left_idx, mid - 1)

            return root
        
        return recur(0, len(inorder) - 1)

sol = Solution()
print(sol.buildTree([9,3,15,20,7], [9,15,7,20,3]))
