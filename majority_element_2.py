class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        #Your Code goes here.
        can1 = -1
        can2 = -1
        cnt1 = 0
        cnt2 = 0
        output = []
        n = len(arr)
        for i in range(n):
            if cnt1 == 0 and arr[i] != can2:
                can1 = arr[i]
                cnt1 += 1
            elif cnt2 == 0 and arr[i] != can1:
                can2 = arr[i]
                cnt2 += 1
            elif arr[i] == can1:
                cnt1 += 1
            elif arr[i] == can2:
                cnt2 += 1
            elif arr[i] != can1 and arr[i] != can2:
                cnt1 -= 1
                cnt2 -= 1
        f_cnt1 = 0
        f_cnt2 = 0
        for i in range(n):
            if arr[i] == can1:
                f_cnt1 += 1
            if arr[i] == can2:
                f_cnt2 += 1
        if f_cnt1 > n / 3:
            output.append(can1)
        if f_cnt2 > n / 3:
            output.append(can2)
        output.sort()
        return output
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.findMajority(nums)
        if not ans:
            print("[]")
        else:
            print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()

# } Driver Code Ends
obj = Solution()
print(obj.findMajority([1,2,3,4,5]))