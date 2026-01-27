class Solution:
    def camelCase(self,arr,pat):
        #code here
        result = []
        for word in arr:
            uc = ''
            for ch in word:
                if ch.isupper():
                    uc += ch
                    if pat == uc:
                        result.append(word)
                        break
        return result
sol = Solution()
print(sol.camelCase(["HelloWorld", "HelloWorld", "HelloWorld"], "HW"))