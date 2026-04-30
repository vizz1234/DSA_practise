
from collections import defaultdict, deque

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def verticalOrder(self, root): 
        # code here
        dic = defaultdict(list)
        
        def level_order(node, node_num):
            if not node:
                return
            
            queue = deque([(node, node_num)])
            
            while queue:
                n, c = queue.popleft()
                dic[c].append(n.data)
                
                if n.left:
                    queue.append((n.left, c - 1))
                if n.right:
                    queue.append((n.right, c + 1))
        
        level_order(root, 0)
        
        min_num = min(list(dic.keys()))
        max_num = max(list(dic.keys()))
        
        return [dic[key] for key in range(min_num, max_num + 1)]
        
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

sol = Solution()
print(sol.verticalOrder(root))