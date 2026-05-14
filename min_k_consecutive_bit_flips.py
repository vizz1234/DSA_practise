from collections import deque
class Solution:
    def kBitFlips(self, arr, k):
        # code here
        n = len(arr)
        n_of_flips = 0
        queue = deque()
        flag = 0
        
        for i in range(n):
            
            if i >= k:
                f = queue.popleft()
                flag ^= f
            
            if flag == 1:
                arr[i] ^= 1
            
            if arr[i] == 0:
                
                if i + k > n:
                    return -1
                
                n_of_flips += 1
                flag ^= 1
                queue.append(1)
            
            else:
                queue.append(0)
        
        return n_of_flips
    
sol = Solution()
print(sol.kBitFlips([1, 1, 1, 0, 0, 1, 1, 0, 0, 0], 3))
