from functools import cmp_to_key
class Solution:

    def findLargest(self, arr):
        # code here
        arr = list(map(str, arr))
        
        def compare(a, b):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0
        
        arr.sort(key=cmp_to_key(compare))
        result = "".join(arr)
        return "0" if result[0] == "0" else result
sol = Solution()
print(sol.findLargest([3, 30, 34, 5, 9]))