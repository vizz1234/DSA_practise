class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: list[int], preorder: list[int]) -> list[int]:
        """
        Constructs a binary tree from inorder and preorder traversals and returns its postorder traversal.
        
        Args:
            inorder: List of integers representing inorder traversal
            preorder: List of integers representing preorder traversal
            
        Returns:
            List of integers representing postorder traversal
            
        Raises:
            ValueError: If input lists are empty or of different lengths
        """
        if not inorder or not preorder or len(inorder) != len(preorder):
            raise ValueError("Invalid input: traversals must be non-empty and of equal length")

        inorderHash = {value: idx for idx, value in enumerate(inorder)}
        self.preIdx = 0
        
        def buildRecurTree(left: int, right: int) -> Node:
            if left > right:
                return None
            
            preVal = preorder[self.preIdx]
            self.preIdx += 1
            root = Node(preVal)
            inorderIdx = inorderHash[preVal]
            
            root.left = buildRecurTree(left, inorderIdx - 1)
            root.right = buildRecurTree(inorderIdx + 1, right)
            
            return root
        
        def postOrderTraversal(root: Node) -> None:
            if not root:
                return
            
            postOrderTraversal(root.left)
            postOrderTraversal(root.right)
            postOrderOp.append(root.val)

        head = buildRecurTree(0, len(inorder) - 1)
        postOrderOp = []
        postOrderTraversal(head)
        
        return postOrderOp