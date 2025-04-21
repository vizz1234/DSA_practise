# Python program to calculate stock span
# values using a stack

# Function to calculate stock span values
def calculateSpan(arr):

    n = len(arr)
    span = [0] * n  
    stk = []

    # Process each day's price
    for i in range(n):

        # Remove elements from the stack while the current
        # price is greater than or equal to stack's top price
        while stk and arr[stk[-1]] <= arr[i]:
            stk.pop()

        # If stack is empty, all elements to the left are smaller
        # Else, top of the stack is the last greater element's index
        if not stk:
            span[i] = (i + 1)
        else:
            span[i] = (i - stk[-1])

        # Push the current index to the stack
        stk.append(i)

    return span


if __name__ == "__main__":

    arr = [10, 4, 5, 90, 120, 80]
    span = calculateSpan(arr)
    
    for x in span:
        print(x, end=" ")
