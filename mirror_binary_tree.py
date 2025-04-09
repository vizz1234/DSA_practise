
class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None

# your task is to complete this function

class Solution:
    #Function to convert a binary tree into its mirror tree.
    def mirror(self, root):
        # Code here
        if not root:
            return
        
        root.left, root.right = root.right, root.left
        
        self.mirror(root.left)
        self.mirror(root.right)

# Example usage:
root = Node(1)
root.left = Node(2)
root.right = Node(3)
sol = Solution()
sol.mirror(root)
print(root.left.data)