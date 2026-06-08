from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        def recur(front):
            if not front:
                return None
            if not front.next:
                return TreeNode(front.val)
            
            fast = slow = front
            prev = None

            while fast and fast.next:
                # print(prev.val, slow.val, fast.val)
                prev = slow
                slow = slow.next
                fast = fast.next.next
                
            prev.next = None
            root = TreeNode(slow.val)
            root.left = recur(front)
            root.right = recur(slow.next)
            return root
        
        return recur(head)
        
root = ListNode(-1)
root.next = ListNode(0)
root.next.next = ListNode(3)
root.next.next.next = ListNode(5)
root.next.next.next.next = ListNode(9)

sol = Solution()
print(sol.sortedListToBST(root))
        