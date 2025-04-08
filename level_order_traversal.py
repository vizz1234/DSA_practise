
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

class Solution:
    def levelOrder(self, root):
        # Your code here
        
        output = []
        
        def traversal(root, level):
            if not root:
                return
            
            if len(output) <= level:
                output.append([])
            
            output[level].append(root.data)
            traversal(root.left, level + 1)
            traversal(root.right, level + 1)
        
        traversal(root, 0)
        return output

# Example usage:
# Create a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
sol = Solution()
print(sol.levelOrder(root))