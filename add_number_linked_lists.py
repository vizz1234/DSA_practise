class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    
    def reverse(self, head):
        if not head:
            return head
        prev = None
        cur = head
        fwd = cur.next
        while cur.next:
            cur.next = prev
            prev = cur
            cur = fwd
            fwd = cur.next
        cur.next = prev
        return cur
    
    def trimLeadingZeros(self, head):
        while head.data == 0:
            head = head.next
        return head
    
    def lengthLL(self, head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count
    
    def addTwoLists(self, num1, num2):
        # code here
        num1 = self.trimLeadingZeros(num1)
        num2 = self.trimLeadingZeros(num2)
        l1 = self.lengthLL(num1)
        l2 = self.lengthLL(num2)
        if l2 > l1:
            return self.addTwoLists(num2, num1)
        num1 = self.reverse(num1)
        num2 = self.reverse(num2)
        res = num1
        carry = 0
        while num2 or carry != 0:
            num1.data += carry
            if num2:
                num1.data += num2.data
                num2 = num2.next
            carry = num1.data // 10
            num1.data = num1.data % 10
            
            if not num1.next and carry != 0:
                num1.next = Node(0)
            
            num1 = num1.next
        return self.reverse(res)