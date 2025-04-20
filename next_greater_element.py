# Python implementation to find the next
# greater element using a stack
def nextLargerElement(arr):
    n = len(arr)
    res = [-1] * n  
    stk = []  

    # Traverse the array from right to left
    for i in range(n - 1, -1, -1):

        # Pop elements from the stack that are less 
        # than or equal to the current element
        while stk and arr[stk[-1]] <= arr[i]:
            stk.pop()

        # If the stack is not empty, the element at the 
        # top of the stack is the next greater element
        if stk:
            res[i] = arr[stk[-1]]

        # Push the current index onto the stack
        stk.append(i)

    return res

if __name__ == "__main__":
  
    arr = [6, 8, 0, 1, 3]
    res = nextLargerElement(arr)
    print(" ".join(map(str, res)))
