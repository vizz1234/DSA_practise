from collections import defaultdict, deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        pattern = defaultdict(list)
        word_set = set(wordList)

        if endWord not in word_set:
            return 0

        for word in word_set | {beginWord}:
            for i in range(len(word)):
                pattern[word[:i] + '*' + word[i+1:]].append(word)
        
        dist = {beginWord}
        q = deque([(beginWord, 1)])
        level = 1

        while q:
            word, level = q.popleft()
            if word == endWord:
                return level
            for i in range(len(word)):
                for neighbor in pattern[word[:i] + '*' + word[i+1:]]:
                    if neighbor not in dist:
                        dist.add(neighbor)
                        q.append((neighbor, level + 1))
        
        print(dist)
        return 0

sol = Solution()
print(sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
