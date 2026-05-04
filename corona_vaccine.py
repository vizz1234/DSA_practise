
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def supplyVaccine(self, root):
        # Your code here
        self.kits = 0
        
        def post_order(node):
            
            if not node:
                return 2
            
            left = post_order(node.left)
            right = post_order(node.right)
            
            if left == 0 or right == 0:
                self.kits += 1
                return 1
            
            if left == 1 or right == 1:
                return 2
            
            return 0
        
        if post_order(root) == 0:
            self.kits += 1
        
        return self.kits


root = Node(0)
root.left = Node(0)
root.right = Node(0)
root.right.left = Node(0)
root.right.right = Node(0)
root.right.right.left = Node(0)

sol = Solution()
print(sol.supplyVaccine(root))
