#User function Template for python3

class Solution:
    def nextPermutation(self, arr):
        # code here
        n = len(arr)
        pivot = -1
        for i in range(n-2, -1, -1):
            if arr[i] < arr[i+1]:
                pivot = i
                break
        if pivot == -1:
            arr = arr.reverse()
        else:
            minNum = float('inf')
            for i in range(n-1, pivot, -1):
                if arr[i] > arr[pivot]:
                    swap = i
                    minNum = arr[i]
                    break
            arr[pivot], arr[swap] = arr[swap], arr[pivot]
            left = pivot + 1
            right = n - 1
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        N = len(arr)
        for i in range(N):
            arr[i] = int(arr[i])

        ob = Solution()
        ob.nextPermutation(arr)
        for i in range(N):
            print(arr[i], end=" ")
        print()

# } Driver Code Ends
obj = Solution()
print(obj.nextPermutation([1,2,3]))