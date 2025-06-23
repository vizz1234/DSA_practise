class Solution:
    def nextLargerElement(self, arr):
        # code here
        n = len(arr)
        output = [-1] * len(arr)
        stack = []
        for i in range(n - 1, -1, -1):
            val = arr[i]
            while stack and stack[-1] <= val:
                stack.pop()
            if stack:
                output[i] = stack[-1]
            stack.append(val)
        return output


if __name__ == "__main__":
    sol = Solution()
    print(sol.nextLargerElement([1, 3, 2, 4]))
