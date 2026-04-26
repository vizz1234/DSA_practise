class Solution:
    def targetSumComb(self, arr, target):
        # code here
        result = []
        arr.sort()
        
        def backtrack(index, cur_arr, cur_sum):
            
            if cur_sum == target:
                result.append(cur_arr)
                return
            
            for i in range(index, len(arr)):
                if arr[i] > target - cur_sum:
                    break
                backtrack(i, cur_arr + [arr[i]], cur_sum + arr[i])
            
        backtrack(0, [], 0)
        return result

sol = Solution()
print(sol.targetSumComb([10,1,2,7,6,1,5],8))