class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def diameter(self, root):
        # Your code here
        self.max_diameter = 0
        
        def height(root):
            if not root:
                return 0
            
            left = height(root.left)
            right = height(root.right)
            
            self.max_diameter = max(self.max_diameter, left + right)
            
            return 1 + max(left, right)
        
        height(root)
        
        return self.max_diameter
    
# Example usage:
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
sol = Solution()
print(sol.diameter(root))