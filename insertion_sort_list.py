from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return
        
        curr = head.next
        outer_prev = head
        while curr:
            inside_curr = head
            nxt = curr.next
            v1 = curr.val
            prev = None
            moved = False
            while inside_curr != curr:
                v2 = inside_curr.val
                if v2 > v1:
                    curr.next = inside_curr
                    if prev:
                        prev.next = curr
                    else:
                        head = curr
                    outer_prev.next = nxt
                    moved = True
                    break
                prev = inside_curr
                inside_curr = inside_curr.next
            curr = nxt
            if not moved:
                outer_prev = outer_prev.next
        return head
                    
head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(3)
sol = Solution()
print(sol.insertionSortList(head).val, sol.insertionSortList(head).next.val, sol.insertionSortList(head).next.next.val, sol.insertionSortList(head).next.next.next.val)
