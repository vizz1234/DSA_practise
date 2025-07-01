class Solution:
    def longestStringChain(self, words):
        # Code here
        words.sort(key = len)
        output = 1
        dp = {}
        for word in words:
            dp[word] = 1
            for i in range(len(word)):
                checkWord = word[:i] + word[i+1:]
                if checkWord in dp:
                    dp[word] = max(dp[word], dp[checkWord] + 1)
        return max(dp.values())

sol = Solution()
print(sol.longestStringChain(["a", "b", "ba", "bca", "bda", "bdca"]))