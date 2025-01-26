class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        total_max = -1
        second_max = -1
        for i in arr:
            if i > total_max:
                second_max = total_max
                total_max = i
                continue
            elif i != total_max and i > second_max:
                second_max = i
        return second_max
obj = Solution()
print(obj.getSecondLargest([1,2,3,4,5]))