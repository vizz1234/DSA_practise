#User function Template for python3

class Solution:
    
    #Function to find minimum number of attempts needed in 
    #order to find the critical floor.
    def eggDrop(self, n, k):
        # code here
        
        dp = [0] * (n + 1)
        t = 0
        
        while dp[n] < k:
            
            t += 1
            
            new_dp =[0] * (n + 1)
            
            for i in range(1, n + 1):
                new_dp[i] = dp[i - 1] + 1 + dp[i]
            
            dp = new_dp
        
        return t

sol = Solution()
print(sol.eggDrop(2, 10))
print(sol.eggDrop(3, 14))