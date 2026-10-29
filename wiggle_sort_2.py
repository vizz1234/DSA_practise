class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        def quickselect(k):

            left, right = 0, n - 1

            while left <= right:

                pivot = nums[(left + right) // 2]

                lt = i = left
                gt = right

                while i <= gt:

                    if nums[i] < pivot:
                        nums[lt], nums[i] = nums[i], nums[lt]
                        i += 1
                        lt += 1
                    
                    elif nums[i] > pivot:
                        nums[gt], nums[i] = nums[i], nums[gt]
                        gt -= 1
                    
                    else:
                        i += 1
                
                if k < lt:
                    right = lt - 1
                elif k > gt:
                    left = gt + 1
                else:
                    return nums[k]
        
        def idx(i):
            return (1 + 2*i) % (n | 1)
        
        median = quickselect(n // 2)
        left = i = 0
        right = n - 1

        while i <= right:

            i_idx = idx(i)
            l_idx = idx(left)
            r_idx = idx(right)

            if nums[i_idx] > median:
                nums[i_idx], nums[l_idx] = nums[l_idx], nums[i_idx]
                left += 1
                i += 1
            
            elif nums[i_idx] < median:
                nums[i_idx], nums[r_idx] = nums[r_idx], nums[i_idx]
                right -= 1
            
            else:
                i += 1
        
        return nums

s = Solution()
print(s.wiggleSort([1,5,1,1,6,4]))