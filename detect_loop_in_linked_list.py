class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        #code here
        d = {}
        cur = head
        while cur:
            if cur not in d:
                d[cur] = cur
            else:
                return True
            cur = cur.next
        return False

# With O(1) space
# class Solution:
#     def detectLoop(self, head):
#         slow = head
#         fast = head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#             if slow == fast:
#                 return True
#         return False
