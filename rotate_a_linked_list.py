class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    
    #Function to rotate a linked list.
    def rotate(self, head, k):
        # code here
        if not head or not head.next or k == 0:
            return head
        cur = head
        c = 1
        while cur.next != None:
            cur = cur.next
            c += 1

        n = k % c
        if n == 0:
            cur.next = None
            return head
        cur.next = head
        cur = cur.next
        for i in range(1, n):
            cur = cur.next
        newHead = cur.next
        cur.next = None
        return newHead