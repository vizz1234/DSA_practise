from collections import defaultdict
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        d = defaultdict(list)
        
        def level_order_traversal(node, height):
            if not node:
                return
            d[height].append(node.val)
            level_order_traversal(node.left, height + 1)
            level_order_traversal(node.right, height + 1)
        
        level_order_traversal(root, 0)
        max_height = max(list(d.keys()))
        result = [d[l] for l in range(max_height, -1, -1)]
        return result

sol = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(sol.levelOrderBottom(root))


        