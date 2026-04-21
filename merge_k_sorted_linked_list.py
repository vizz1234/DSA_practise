import heapq

class Node:
    def _init_(self, x):
        self.data = x
        self.next = None

class Solution:
    def mergeKLists(self, arr):
        # code here
        heap = []
        for i, node in enumerate(arr):
            heapq.heappush(heap, (node.data, i, node))
        result = Node(0)
        curr = result
        while heap:
            data, i, next_node = heapq.heappop(heap)
            curr.next = next_node
            curr = curr.next
            if next_node.next:
                heapq.heappush(heap, (next_node.next.data, i, next_node.next))
        return result.next

sol = Solution()
arr = [Node(1), Node(2), Node(3), Node(4), Node(5)]
print(sol.mergeKLists(arr))