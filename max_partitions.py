class Solution:
    def maxPartitions(self , s):
        # code here
        d = {}
        count = 0
        n = len(s)
        
        for i in range(n):
            d[s[i]] = d.get(s[i], 0) + 1
        
        ws = set()
        for i in range(n):
            d[s[i]] -= 1
            ws.add(s[i])
            
            if d[s[i]] == 0:
                flag = 0
                for key in ws:
                    if d[key] != 0:
                        flag = 1
                        break
                if flag == 0:
                    count += 1
                    ws = set()
        
        return count

sol = Solution()
print(sol.maxPartitions("abacaba"))