
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



class Solution:
    def isPalindrome(self, head):
        # code here
        if not head or not head.next:
            return True
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        curr = slow.next
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        p1, p2 = head, prev
        while p2:
            if p1.data != p2.data:
                return False
            p1 = p1.next
            p2 = p2.next
        return True

sol = Solution()
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(2)
head.next.next.next.next = Node(1)
print(sol.isPalindrome(head))