class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        
        lo, hi = min(nums), max(nums)
        if lo == hi:
            return 0
        
        # Bucket size and count
        bucket_size = max(1, (hi - lo) // (n - 1))
        bucket_count = (hi - lo) // bucket_size + 1
        
        bucket_min = [float('inf')] * bucket_count
        bucket_max = [float('-inf')] * bucket_count
        
        for num in nums:
            idx = (num - lo) // bucket_size
            bucket_min[idx] = min(bucket_min[idx], num)
            bucket_max[idx] = max(bucket_max[idx], num)
        
        max_gap = 0
        prev_max = lo
        for i in range(bucket_count):
            if bucket_min[i] == float('inf'):
                continue  # empty bucket, skip
            max_gap = max(max_gap, bucket_min[i] - prev_max)
            prev_max = bucket_max[i]
        
        return max_gap

sol = Solution()
print(sol.maximumGap([3, 6, 9, 1]))