
import heapq

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        

class Solution:
    def flatten(self, root):
        # code here
        heap = []
        cur = root
        i = 0
        while cur:
            heapq.heappush(heap, (cur.data, i, cur))
            cur = cur.next
            i += 1
        result = Node(0)
        cur = result
        while heap:
            pop_data, i, pop_node = heapq.heappop(heap)
            cur.bottom = Node(pop_data)
            cur = cur.bottom
            if pop_node.bottom:
                heapq.heappush(heap, (pop_node.bottom.data, i, pop_node.bottom))
        return result.bottom

sol = Solution()
root = Node(1)
root.next = Node(2)
root.next.bottom = Node(3)
root.next.bottom.bottom = Node(4)
root.next.bottom.bottom.bottom = Node(5)
print(sol.flatten(root))