class Solution:
	def mergeOverlap(self, arr):
		#Code here
		n = len(arr)
		if n <= 1:
			return arr
		arr = sorted(arr, key = lambda x: x[0], reverse = False)
		i = 0
		j = 1
		while j < len(arr):
			start, end = arr[i][0], arr[i][1]
			start1, end1 = arr[j][0], arr[j][1]
			if start1 <= end:
				arr[i][1] = max(end, end1)
				del arr[j]
			else:
				i += 1
				j += 1
		return arr
obj = Solution()
print(obj.mergeOverlap([[1,3],[2,6],[8,10],[15,18]]))