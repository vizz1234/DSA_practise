class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
class Solution:
    def sortedMerge(self,head1, head2):
        # code here
        if head1 is None:
            return head2
        if head2 is None:
            return head1
        dummy = Node(-1)
        cur = dummy
        while head1 and head2:
            if head1.data <= head2.data:
                cur.next = head1
                head1 = head1.next
            else:
                cur.next = head2
                head2 = head2.next
            cur = cur.next
        if head1:
            cur.next = head1
        if head2:
            cur.next = head2
        return dummy.next
