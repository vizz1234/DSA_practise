class Solution:
    def longestUniqueSubstr(self, s):
        # code here
        right = 0
        left = 0
        n = len(s)
        vis = [0] * 26
        res = 0
        while right < n:
            while vis[ord(s[right]) - ord('a')] == 1:
                vis[ord(s[left]) - ord('a')] = 0
                left += 1
            vis[ord(s[right]) - ord('a')] = 1
            res = max(res, right - left + 1)
            right += 1
        return res
obj = Solution()
print(obj.longestUniqueSubstr("abcabcbb"))