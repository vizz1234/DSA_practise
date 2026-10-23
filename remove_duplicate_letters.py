class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        last_occ = {char:i for i, char in enumerate(s)}
        seen = set()
        stack = []

        for i, char in enumerate(s):

            if char in seen:
                continue
            
            while stack and char < stack[-1] and last_occ[stack[-1]] > i:
                removed = stack.pop()
                seen.remove(removed)
            
            stack.append(char)
            seen.add(char)
        
        return ''.join(stack)

sol = Solution()
print(sol.removeDuplicateLetters('bcabc'))