
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None


class Solution:
    def isSymmetric(self, root):
        # code here
        if not root:
            return True
        
        def isMirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.data != right.data:
                return False
            return isMirror(left.left, right.right) and isMirror(left.right, right.left)
        
        return isMirror(root.left, root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(3)

sol = Solution()
print(sol.isSymmetric(root))