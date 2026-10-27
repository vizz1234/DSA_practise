class Solution:
    def maxNumber(self, nums1: list[int], nums2: list[int], k: int) -> list[int]:
        
        def max_subsequence(nums, length):

            stack = []
            drop = len(nums) - length

            for digit in nums:
                while stack and drop > 0 and stack[-1] < digit:
                    stack.pop()
                    drop -= 1
                stack.append(digit)
            
            return stack[:length]
        
        def merge(a, b):

            result = []
            i = j = 0

            while i < len(a) and j < len(b):

                if a[i:] > b[j:]:
                    result.append(a[i])
                    i += 1
                
                else:
                    result.append(b[j])
                    j += 1
            
            result.extend(a[i:])
            result.extend(b[j:])

            return result
        
        start = max(0, k - len(nums2))
        end = min(k, len(nums1))
        best = []

        for i in range(start, end + 1):

            a = max_subsequence(nums1, i)
            b = max_subsequence(nums2, k - i)
            merged = merge(a, b)

            if merged > best:
                best = merged
        
        return best

sol = Solution()
print(sol.maxNumber([6, 7], [6, 0, 4]))
print(sol.maxNumber([3, 4, 6, 5], [9, 1, 2, 5, 8, 3]))
print(sol.maxNumber([2, 5, 6, 4, 4, 0], [7, 3, 8, 0, 6, 5, 7, 6, 2]))
print(sol.maxNumber([6, 3], [4, 0, 1, 5]))
print(sol.maxNumber([8, 9], [3, 9]))