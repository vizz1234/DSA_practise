
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None


class Solution:
    def distCandy(self, root):
        # code here
        self.moves = 0
        
        def post_order_traversal(node):
            
            if not node:
                return 0
            
            left = post_order_traversal(node.left)
            right = post_order_traversal(node.right)
            
            self.moves += abs(left) + abs(right)
            
            return node.data + left + right - 1
        
        post_order_traversal(root)
        
        return self.moves

root = Node(2)
root.left = Node(0)
root.right = Node(0)
root.right.left = Node(3)
root.right.right = Node(0)


sol = Solution()
print(sol.distCandy(root))
