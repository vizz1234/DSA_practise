from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        flag = 0
        
        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                flag = 1
                break
        
        slow = head
        
        while slow and fast and slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow if flag else None

sol = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = head
print(sol.detectCycle(head).val)
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
print(sol.detectCycle(head).val)
head = None
print(sol.detectCycle(head))
head = ListNode(1)
head.next = head
print(sol.detectCycle(head).val)
