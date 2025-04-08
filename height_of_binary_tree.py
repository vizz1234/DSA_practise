
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    #Function to find the height of a binary tree.
    def height(self, root):
        # code here
        def find_height(root, level):
            if not root:
                return level - 1
            
            level_l = find_height(root.left, level + 1)
            level_r = find_height(root.right, level + 1)
            
            return max(level_l, level_r)
        
        ht = find_height(root, 0)
        return ht

sol = Solution()
root = Node(1)
root.left = Node(2)
root.right = Node(3)
print(sol.height(root))

# Efficient Solution
class Solution:
    def height(self, root):
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))
