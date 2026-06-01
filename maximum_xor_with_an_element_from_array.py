#User function Template for python3

class TrieNode:
    def __init__(self):
        self.children = [None, None]

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.is_empty = True
    
    def insert(self, num):
        self.is_empty = False
        node = self.root
        
        for i in range(29, -1, -1):
            b = (num >> i) & 1
            if not node.children[b]:
                node.children[b] = TrieNode()
            node = node.children[b]
    
    def max_xor(self, num):
        
        node = self.root
        xor_value = 0
        
        for i in range(29, -1, -1):
            b = (num >> i) & 1
            want = 1 - b
            
            if node.children[want]:
                xor_value |= (1 << i)
                node = node.children[want]
            else:
                node = node.children[b]
        
        return xor_value
            

class Solution:
    def maxXor(self, arr, queries):
        # Code here
        arr.sort()
        idx_queries = sorted(enumerate(queries), key = lambda x : x[1][1])
        
        t = Trie()
        ptr = 0
        res = [-1] * len(queries)
        
        for i, (x, m) in idx_queries:
            
            while ptr < len(arr) and arr[ptr] <= m:
                t.insert(arr[ptr])
                ptr += 1
            
            if not t.is_empty:
                res[i] = t.max_xor(x)
        
        return res

sol = Solution()
print(sol.maxXor([1,2,3,4,5], [[1,2],[3,2],[0,3],[5,5]]))
