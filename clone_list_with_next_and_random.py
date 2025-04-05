class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None

class Solution:
    def cloneLinkedList(self, head):
        # code here
        def cloneHelper(node, d):
            if not node:
                return None
            if node in d:
                return d[node]
            
            newNode = Node(node.data)
            d[node] = newNode
            newNode.next = cloneHelper(node.next, d)
            newNode.random = cloneHelper(node.random, d)
            
            return newNode
        return cloneHelper(head, {})

