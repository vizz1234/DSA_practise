class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution():
    def cloneGraph(self, node):
        #code here
        if not node:
            return None
        old_new = {}
        def dfs(curr):
            if curr in old_new:
                return old_new[curr]
            clone = Node(curr.val)
            old_new[curr] = clone
            for n in curr.neighbors:
                clone.neighbors.append(dfs(n))
            return clone
        return dfs(node)
sol = Solution()
print(sol.cloneGraph(Node(1, [Node(2), Node(3)])))