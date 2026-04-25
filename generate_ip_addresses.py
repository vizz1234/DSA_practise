class Solution:
    def generateIp(self, s):
        # Code here
        result = []
        
        def backtrack(index, parts):
            
            if len(parts) == 4 and index == len(s):
                result.append('.'.join(parts))
                return
            
            parts_remaining = 4 - len(parts)
            remaining_len = len(s) - index
            
            if remaining_len < parts_remaining:
                return
            if remaining_len > parts_remaining * 3:
                return
            
            for length in range(1, 4):
                
                if index + length > len(s):
                    break
                ip_part = s[index:index+length]
                
                if len(ip_part) > 1 and ip_part[0] == '0':
                    break
                if int(ip_part) > 255:
                    break
                
                backtrack(index + length, parts + [ip_part])
        
        backtrack(0, [])
        
        return result

sol = Solution()
print(sol.generateIp("25525511135"))