# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        p_anc = []
        q_anc = []

        def find_p(node):
            if not node:
                return False
            
            if node == p:
                p_anc.append(node)
                return True
            
            if find_p(node.left):
                p_anc.append(node)
                return True
            
            if find_p(node.right):
                p_anc.append(node)
                return True

        def find_q(node):
            if not node:
                return False
            
            if node == q:
                q_anc.append(node)
                return True
            
            if find_q(node.left):
                q_anc.append(node)
                return True
            
            if find_q(node.right):
                q_anc.append(node)
                return True
        
        find_p(root)
        find_q(root)

        i, j = len(p_anc) - 1, len(q_anc) - 1

        while i >= 0 and j >=0 and p_anc[i] == q_anc[j]:

            i -= 1
            j -= 1
        
        return p_anc[i + 1]

sol = Solution()
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
p = TreeNode(5)
q = TreeNode(1)
print(sol.lowestCommonAncestor(root, p, q).val)
p = TreeNode(5)
q = TreeNode(4)
print(sol.lowestCommonAncestor(root, p, q).val)
        