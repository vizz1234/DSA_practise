class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def getCount(self, root, l, h):
        # Your code here
        self.count = 0
        def pre_order(node):
            
            if not node:
                return
            
            if node.data <= h and node.data >= l:
                self.count += 1
                pre_order(node.left)
                pre_order(node.right)
            
            elif node.data < l:
                pre_order(node.right)
            
            elif node.data > h:
                pre_order(node.left)
        
        pre_order(root)
        
        return self.count

root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.right = Node(18)

sol = Solution()
print(sol.getCount(root, 7, 15))