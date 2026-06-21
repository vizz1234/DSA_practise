from collections import deque, defaultdict
from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        word_set = set(wordList)
        if endWord not in word_set:
            return []
        
        pattern = defaultdict(list)

        for word in word_set | {beginWord}:
            for i in range(len(word)):
                pattern[word[:i] + '*' + word[i+1:]].append(word)
        
        dist = {beginWord: 0}
        q = deque([beginWord])

        while q:

            word = q.popleft()

            for i in range(len(word)):
                for neighbor in pattern[word[:i] + '*' + word[i+1:]]:
                    if neighbor not in dist:
                        dist[neighbor] = dist[word] + 1
                        q.append(neighbor)
            
        if endWord not in dist:
            return []
        
        result = []
        def dfs(word, path):

            if word == endWord:
                result.append(path)
                return
            
            for i in range(len(word)):
                for neighbor in pattern[word[:i] + '*' + word[i+1:]]:
                    if neighbor in dist and dist[neighbor] == dist[word] + 1:
                        dfs(neighbor, path + [neighbor])
        
        dfs(beginWord, [beginWord])
        return result