class Solution:
    def exactlyK(self, arr, k):
        # Code here
        def atmost(k):
            n = len(arr)
            freq = {}
            count = 0
            left = 0
            
            for right in range(n):
                freq[arr[right]] = freq.get(arr[right], 0) + 1
                while len(freq) > k:
                    freq[arr[left]] -= 1
                    if freq[arr[left]] == 0:
                        del freq[arr[left]]
                    left += 1
                count += (right - left + 1)
            
            return count
        
        return atmost(k) - atmost(k - 1)
sol = Solution()
arr = [1, 2, 3, 4, 5]
k = 3
print(sol.exactlyK(arr, k))
arr = [1, 1, 2, 3, 1, 4, 2]
k = 2
print(sol.exactlyK(arr, k))
arr = [1, 1, 1]
k = 1
print(sol.exactlyK(arr, k))