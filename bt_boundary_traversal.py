
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None


class Solution:
    def boundaryTraversal(self, root):
        # code here
        if not root:
            return
        
        def is_leaf(node):
            return node.left is None and node.right is None
        
        res = [root.data]
        
        cur = root.left
        while cur:
            if not is_leaf(cur):
                res.append(cur.data)
            if cur.left:
                cur = cur.left
            else:
                cur = cur.right
        
        def leaf_nodes(node):
            if not node:
                return
            if is_leaf(node):
                if node != root:
                    res.append(node.data)
                return
            leaf_nodes(node.left)
            leaf_nodes(node.right)
        
        leaf_nodes(root)
        
        right_nodes = []
        cur = root.right
        while cur:
            if not is_leaf(cur):
                right_nodes.append(cur.data)
            cur = cur.right if cur.right else cur.left
        
        res.extend(reversed(right_nodes))
        
        return res
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
sol = Solution()
print(sol.boundaryTraversal(root))         