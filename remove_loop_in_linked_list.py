class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        # code here
        if not head or not head.next:
            return
            
        slow = head
        fast = head
        
        # Detect loop using Floyd's algorithm
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                # If loop exists, find the start of loop
                if slow == head:
                    # If loop starts from head
                    while fast.next != head:
                        fast = fast.next
                    fast.next = None
                else:
                    # For other cases
                    slow = head
                    while slow.next != fast.next:
                        slow = slow.next
                        fast = fast.next
                    fast.next = None
                break
        