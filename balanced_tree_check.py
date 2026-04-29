
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None

class Solution:
    def isBalanced(self, root):
        # code here
        
        def check(node):
            
            if not node:
                return -1
            
            left_h = check(node.left)
            right_h = check(node.right)
            
            if left_h == -2 or right_h == -2:
                return -2
            
            if abs(left_h - right_h) > 1:
                return -2
            
            return 1 + max(left_h, right_h)
        
        return check(root) != -2

root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(3)

sol = Solution()
print(sol.isBalanced(root))