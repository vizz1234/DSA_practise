class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:

        n = len(nums)
        counts = [0] * n
        idx_nums = [(val, i) for i, val in enumerate(nums)]

        def merge_sort(arr):

            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            i = j = 0
            merged = []

            while i < len(left) and j < len(right):

                if left[i][0] > right[j][0]:
                    merged.append(right[j])
                    j += 1
                
                else:
                    counts[left[i][1]] += j
                    merged.append(left[i])
                    i += 1
            
            while i < len(left):
                counts[left[i][1]] += j
                merged.append(left[i])
                i += 1
            
            while j < len(right):
                merged.append(right[j])
                j += 1
            
            return merged
        
        merge_sort(idx_nums)

        return counts

sol = Solution()
print(sol.countSmaller([5, 2, 6, 1]))