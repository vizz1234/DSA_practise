class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
      
    def __init__(self, cap):
        #code here
        self.cap = cap
        self.q = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def insert(self, node):
        tempNode = self.head.next
        self.head.next = node
        node.next = tempNode
        node.prev = self.head
        tempNode.prev = node
    
    def remove(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode

    def get(self, key):
        #code here
        if key not in self.q:
            return -1
        node = self.q[key]
        self.remove(node)
        self.insert(node)
        return node.value
        

    def put(self, key, value):
        #code here
        if key in self.q:
            node = self.q[key]
            self.remove(node)
            del self.q[key]
        
        if len(self.q) >= self.cap:
            LRUnode = self.tail.prev
            self.remove(LRUnode)
            del self.q[LRUnode.key]
        
        MRUnode = Node(key, value)
        self.insert(MRUnode)
        self.q[key] = MRUnode