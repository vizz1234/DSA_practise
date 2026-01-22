class Solution:
    
    def findSplit(self, arr):
        # Return an array of possible answer, driver code will judge and return true or false based on
        s = sum(arr)
        s3 = s // 3
        # print(s3)
        if s % 3 != 0:
            # print(s3 % 3)
            return [-1, -1]
        cur_sum = 0
        i, j = -1, -1
        for k in range(len(arr)):
            cur_sum += arr[k]
            # print(cur_sum)
            if i == -1:
                if cur_sum == s3:
                    # print(i)
                    i = k
            else:
                if cur_sum == 2 * s3:
                    # print(i, k)
                    return [i, k]
        return [-1, -1]
sol = Solution()
print(sol.findSplit([1, 2, 3, 4, 5, 6, 7, 8, 9]))