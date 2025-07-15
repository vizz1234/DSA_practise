class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,arr,dep):
        # code here
        maxD = max(dep)
        gA = [0] * (maxD + 2)
        n = len(arr)
        
        for i in range(n):
            gA[arr[i]] += 1
            gA[dep[i] + 1] -= 1
        
        count = 0
        output = 0
        
        for i in range(maxD + 2):
            count += gA[i]
            output = max(output, count)
        
        return output

sol = Solution()
print(sol.minimumPlatform([900, 940, 950, 1100, 1500, 1800], [910, 1200, 1120, 1130, 1900, 2000]))