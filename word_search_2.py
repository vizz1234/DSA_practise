from typing import List

class TrieNode:

    def __init__(self):

        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root = TrieNode()

        for word in words:
            node = root

            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            
            node.word = word
        
        m, n = len(board), len(board[0])
        output = []
        
        def dfs(r, c, node):

            ch = board[r][c]

            if ch not in node.children:
                return
            
            node = node.children[ch]

            if node.word:
                output.append(node.word)
                node.word = None
            
            board[r][c] = '#'
            
            for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:

                nr = r + dr
                nc = c + dc

                if (0 <= nr < m) and (0 <= nc < n) and board[nr][nc] != '#':
                    dfs(nr, nc, node)
            
            board[r][c] = ch
        
        for i in range(m):
            for j in range(n):
                dfs(i, j, root)
        
        return output  

sol = Solution()
print(sol.findWords(board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]))