class Solution:

    def __init__(self):
        # code here
        self.min = -1
        self.stack = []
        
    # Add an element to the top of Stack
    def push(self, x):
        # code here
        if not self.stack:
            self.min = x
            self.stack.append(x)
        elif x < self.min:
            self.stack.append(2 * x - self.min)
            self.min = x
        else:
            self.stack.append(x)

    # Remove the top element from the Stack
    def pop(self):
        # code here
        if not self.stack:
            return -1
        top = self.stack.pop()
        if top < self.min:
            temp = self.min
            self.min = 2 * self.min - top
            top = temp
        return top

    # Returns top element of Stack
    def peek(self):
        # code here
        if not self.stack:
            return -1
        top = self.stack[-1]
        return self.stack[-1] if top > self.min else self.min

    # Finds minimum element of Stack
    def getMin(self):
        # code here
        return self.min if self.stack else -1

s = Solution()
s.push(3)
s.push(5)
print(s.getMin())
s.push(2)
print(s.getMin())
