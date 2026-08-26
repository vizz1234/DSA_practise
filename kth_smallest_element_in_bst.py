from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        ordered_tree_list = []

        def inorder(node):

            if not node or len(ordered_tree_list) == k:
                return
            
            inorder(node.left)
            ordered_tree_list.append(node.val)
            inorder(node.right)
        
        inorder(root)
        return ordered_tree_list[k-1]

sol = Solution()
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.right = TreeNode(2)
print(sol.kthSmallest(root, 1))
            




        


        