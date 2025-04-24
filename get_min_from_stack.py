# Python program to implement a stack that supports
# all operations in O(1) time and O(1) extra space.

class SpecialStack:
    def __init__(self):
        self.s = []
        self.minEle = -1

    # Add an element to the top of Stack
    def push(self, x):
        if not self.s:
            self.minEle = x
            self.s.append(x)
        # If new number is less than minEle
        elif x < self.minEle:
            self.s.append(2 * x - self.minEle)
            self.minEle = x
        else:
            self.s.append(x)

    # Remove the top element from the Stack
    def pop(self):
        if not self.s:
            return

        top = self.s.pop()

        # Minimum will change, if the minimum element
        # of the stack is being removed.
        if top < self.minEle:
            self.minEle = 2 * self.minEle - top

    # Returns top element of Stack
    def peek(self):
        if not self.s:
            return -1

        top = self.s[-1]

        # If minEle > top means minEle stores value of top.
        return self.minEle if self.minEle > top else top

    # Finds minimum element of Stack
    def getMin(self):
        if not self.s:
            return -1

        # variable minEle stores the minimum element
        # in the stack.
        return self.minEle

if __name__ == '__main__':
    ss = SpecialStack()
    
    # Function calls
    ss.push(2)
    ss.push(3)
    print(ss.peek(), end=" ")
    ss.pop()
    print(ss.getMin(), end=" ")
    ss.push(1)
    print(ss.getMin(), end=" ")
    
