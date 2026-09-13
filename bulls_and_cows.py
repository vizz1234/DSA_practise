from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = sum(s == g for s, g in zip(secret, guess))
        
        s_counter = Counter(s for s, g in zip(secret, guess) if s != g)
        g_counter = Counter(g for s, g in zip(secret, guess) if s != g)
        
        cows = sum((s_counter & g_counter).values())  # Counter & does min per key
        
        return f"{bulls}A{cows}B"

sol = Solution()
print(sol.getHint("1807", "7810"))
print(sol.getHint("1123", "0111"))