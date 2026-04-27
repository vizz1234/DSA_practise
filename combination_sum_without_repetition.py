class Solution:
    def uniqueCombinations(self, arr, target):
        # code here
        result = []
        arr.sort()
        
        def backtrack(index, cur_arr, cur_sum):
            
            if cur_sum == target:
                result.append(cur_arr)
                return
            
            if index >= len(arr):
                return
            
            for i in range(index, len(arr)):
                
                if arr[i] > target - cur_sum:
                    return
                
                if i > index and arr[i] == arr[i - 1]:
                    continue
                
                backtrack(i + 1, cur_arr + [arr[i]], cur_sum + arr[i])
        
        backtrack(0, [], 0)
        return result

sol = Solution()
print(sol.uniqueCombinations([10,1,2,7,6,1,5],8))
