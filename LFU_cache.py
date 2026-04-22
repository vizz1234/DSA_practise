from collections import defaultdict

class Node:
    def __init__(self, key = 0, val = 0):
        self.key = key
        self.val = val
        self.freq = 1
        self.next = None
        self.prev = None

class DLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def insert_at_tail(self, node):
        self.tail.prev.next = node
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev = node
        self.size += 1
    
    def remove_node(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
        self.size -= 1
    
    def remove_lru(self):
        if self.size == 0:
            return None
        lru_node = self.head.next
        self.remove_node(lru_node)
        return lru_node
    
class LFUCache:
    def __init__(self, cap: int):
        #code here
        self.cap = cap
        self.size = 0
        self.min_freq = 0
        self.key_node = {}
        self.freq_list = defaultdict(DLinkedList)
    
    def update_freq(self, node):
        freq = node.freq
        self.freq_list[freq].remove_node(node)
        if freq == self.min_freq and self.freq_list[freq].size == 0:
            self.min_freq += 1
        node.freq += 1
        self.freq_list[node.freq].insert_at_tail(node)

    def get(self, key: int) -> int:
        #code here
        if key not in self.key_node:
            return -1
        node = self.key_node[key]
        self.update_freq(node)
        return node.val
        
    def put(self, key: int, value: int) -> None:
        #code here
        if self.cap == 0:
            return
        if key in self.key_node:
            node = self.key_node[key]
            node.val = value
            self.update_freq(node)
        else:
            if self.size == self.cap:
                evict_node = self.freq_list[self.min_freq].remove_lru()
                del self.key_node[evict_node.key]
                self.size -= 1
            new_node = Node(key, value)
            self.freq_list[1].insert_at_tail(new_node)
            self.min_freq = 1
            self.key_node[key] = new_node
            self.size += 1

sol = LFUCache(2)
sol.put(1, 1)
sol.put(2, 2)
print(sol.get(1))
sol.put(3, 3)
print(sol.get(2))
sol.put(4, 4)
print(sol.get(1))
print(sol.get(3))
print(sol.get(4))