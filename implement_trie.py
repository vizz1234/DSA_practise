#User function Template for python3
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
class Trie:
    def __init__(self):
        # implement Trie
        self.root = TrieNode()
        
        
    def insert(self, word: str):
       # insert word into Trie
        node = self.root
        for ch in word:
            if ch not in node.children:
               node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isEnd = True

    def search(self, word: str) -> bool:
         # search word in the Trie
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.isEnd

    def isPrefix(self, word: str) -> bool:
         # search prefix word in the Trie
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True