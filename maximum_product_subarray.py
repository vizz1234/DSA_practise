class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr):
		# code here
		curMax = arr[0]
		curMin = arr[0]
		maxProd = arr[0]
		for i in range(1, len(arr)):
			temp = max(arr[i], curMax * arr[i], curMin * arr[i])
			curMin = min(arr[i], curMax * arr[i], curMin * arr[i])
			curMax = temp
			maxProd = max(curMax, maxProd)
		return maxProd