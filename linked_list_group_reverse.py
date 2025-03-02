class Solution:
    def reverseKGroup(self, head, k):
        # Code here
        if not head:
            return None
        tail = None
        newHead = None
        cur = head
        while cur:
            groupHead = cur
            prev = None
            nextNode = None
            count = 0
            
            while cur and count < k:
                nextNode = cur.next
                cur.next = prev
                prev = cur
                cur = nextNode
                count += 1
            
            if not newHead:
                newHead = prev
            
            if tail:
                tail.next = prev
            
            tail = groupHead
        
        return newHead