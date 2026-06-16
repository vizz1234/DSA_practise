

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        leftmost = root
        while leftmost:
            dummy = Node(0)
            prev = dummy
            node = leftmost
            while node:
                if node.left:
                    prev.next = node.left
                    prev = prev.next
                if node.right:
                    prev.next = node.right
                    prev = prev.next
                node = node.next
            leftmost = dummy.next
        return root

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

sol = Solution()
print(sol.connect(root))  

                