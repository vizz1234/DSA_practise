#User function Template for python3
class TrieNode:
    def __init__(self):
        self.children = [None, None]

class Solution:
    def maxXor(self, arr):
        if len(arr) < 2:
            return 0
        #code here
        root = TrieNode()
        max_bits = max(1, max(arr)).bit_length()
    
        def insert(x):
            node = root
            for b in range(max_bits - 1, -1, -1):
                bit = (x >> b) & 1
                if node.children[bit] is None:
                    node.children[bit] = TrieNode()
                node = node.children[bit]
        
        def best_xor(x):
            ans = 0
            node = root
            for b in range(max_bits - 1, -1, -1):
                bit = (x >> b) & 1
                wanted_bit = 1 - bit
                if node.children[wanted_bit] is not None:
                    ans |= (1 << b)
                    node = node.children[wanted_bit]
                else:
                    node = node.children[bit]
            return ans
        
        insert(arr[0])
        res = 0
        for i in range(1, len(arr)):
            res = max(res, best_xor(arr[i]))
            insert(arr[i])
        
        return res