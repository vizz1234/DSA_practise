
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



class Solution:
    def intersectPoint(self, head1, head2):
        # code here
        p1, p2 = head1, head2
        while p1 != p2:
            p1 = p1.next if p1 else head2
            p2 = p2.next if p2 else head1
        return p1

sol = Solution()
common1 = Node(15)
common2 = Node(30)
common1.next = common2

# head1: 10 → [common1]
head1 = Node(10)
head1.next = common1

# head2: 3 → 6 → 9 → [common1]
head2 = Node(3)
head2.next = Node(6)
head2.next.next = Node(9)
head2.next.next.next = common1  # ← same node object, not a copy

sol = Solution()
result = sol.intersectPoint(head1, head2)
print(result.data)  # Output: 15