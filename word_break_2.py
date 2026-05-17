class Solution:
    def wordBreak(self, dict, s):
        # code here
        word_set = set(dict)
        memo = {}
        
        def recur(start_idx):
            
            if start_idx == len(s):
                return [""]
            
            if start_idx in memo:
                return memo[start_idx]
            
            results = []
            
            for end_idx in range(start_idx + 1, len(s) + 1):
                word = s[start_idx:end_idx]
                if word in word_set:
                    rem = recur(end_idx)
                    for sen in rem:
                        if sen:
                            results.append(word + " " + sen)
                        else:
                            results.append(word)
            
            memo[start_idx] = results
            return results
        
        return recur(0)
    
sol = Solution()
print(sol.wordBreak(["apple", "pen", "applepen", "pine", "pineapple"], "pineapplepenapple"))
