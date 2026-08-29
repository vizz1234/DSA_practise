

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        cur = root

        while cur:

            if p.val < cur.val and q.val < cur.val:
                cur = cur.left

            elif p.val > cur.val and q.val > cur.val:
                cur = cur.right

            else:
                return cur 

root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)

sol = Solution()
p = TreeNode(2)
q = TreeNode(8)
print(sol.lowestCommonAncestor(root, p, q).val)
p = TreeNode(2)
q = TreeNode(4)
print(sol.lowestCommonAncestor(root, p, q).val)