import heapq
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Solution:
    def mergeKLists(self, arr):
        # code here
        # return head of merged list
        H = []
        for ll in arr:
            head = ll
            while head:
                heapq.heappush(H, head.data)
                head = head.next
        
        if len(H) == 0:
            return None
        
        opLL = Node(heapq.heappop(H))
        root = opLL
        while len(H) > 0:
            opLL.next = Node(heapq.heappop(H))
            opLL = opLL.next
        
        return root