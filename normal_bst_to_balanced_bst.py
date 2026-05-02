
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def balanceBST(self,root):
        #code here
        sorted_list = []
        
        def get_sorted_list(node):
            if not node:
                return None
            get_sorted_list(node.left)
            sorted_list.append(node.data)
            get_sorted_list(node.right)
        
        get_sorted_list(root)
        
        def balanced_bst(left, right):
            if left > right:
                return None
            
            mid = (left + right) // 2
            
            node = Node(sorted_list[mid])
            node.left = balanced_bst(left, mid - 1)
            node.right = balanced_bst(mid + 1, right)
            
            return node
        
        return balanced_bst(0, len(sorted_list) - 1)

root = Node(10)
root.left = Node(8)
root.right = Node(15)
root.left.left = Node(4)
root.left.right = Node(9)
root.right.left = Node(12)
root.right.right = Node(18)

sol = Solution()

new_root = sol.balanceBST(root)
