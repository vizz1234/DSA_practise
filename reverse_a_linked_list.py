class Solution:
    def reverseList(self, head):
        # Code here
        prev = None
        cur = head
        fwd = cur.next
        while cur.next != None:
            cur.next = prev
            prev = cur
            cur = fwd
            fwd = cur.next
        cur.next = prev
        return cur
obj = Solution()
print(obj.reverseList([1,2,3,4,5]))