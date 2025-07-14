class Solution:
    def wordBreak(self, s, dictionary):
        # code here
        n = len(s)
        dictionary = set(dictionary)
        dp = [False] * (n + 1)
        dp[0] = True
        
        for i in range(1, n + 1):
            for j in range(i):
                
                if dp[j] and s[j : i] in dictionary:
                    dp[i] = True
                    break
        return dp[n]

sol = Solution()
print(sol.wordBreak("ilike", ["i", "like", "sam", "sung", "samsung", "mobile", "ice", "cream", "icecream", "man", "go", "mango"]))