class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True
    
    def word_search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

class Solution:
    def longestValidWord(self, words):
        # code here
        max_count = 0
        max_count_word = ''
        words.sort()
        
        node = Trie()
        for word in words:
            node.insert(word)
        
        for word in words:
            count = 0
            cur_prefix = ''
            flag = 1
            for ch in word:
                cur_prefix += ch
                if node.word_search(cur_prefix):
                    count += 1
                else:
                    flag = 0
                    break
            if flag and count > max_count:
                max_count_word = word
                max_count = count
        
        return max_count_word
            
sol = Solution()
print(sol.longestValidWord(["a","banana","app","appl","ap","apply","apple"]))
