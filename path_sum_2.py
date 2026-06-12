from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        cur_arr = []
        def recur(node, cur_sum):
            if not node:
                return
            
            cur_arr.append(node.val)
            cur_sum += node.val

            if not node.left and not node.right:
                if cur_sum == targetSum:
                    result.append(cur_arr[:])
            
            recur(node.left, cur_sum)
            recur(node.right, cur_sum)

            cur_arr.pop()

        recur(root, 0)
        return result

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)

sol = Solution()
print(sol.pathSum(root, 22))


        