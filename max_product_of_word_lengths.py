class Solution:
    def maxProduct(self, words: list[str]) -> int:

        masks = {}

        for word in words:
            mask = 0
            for char in word:
                mask |= 1 << (ord(char) - ord('a'))
            masks[mask] = max(masks.get(mask, 0), len(word))
        
        max_p = 0

        for mask1, len1 in masks.items():
            for mask2, len2 in masks.items():
                if mask1 & mask2 == 0:
                    max_p = max(max_p, len1 * len2)
        
        return max_p

sol = Solution()
print(sol.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))