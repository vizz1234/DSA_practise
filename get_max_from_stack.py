class SpecialStack:

    def __init__(self):
        # Define Stack
        self.stack = []
        self.max_stack = []
        
    
    def push(self, x):
        # Add an element to the top of Stack
        self.stack.append(x)
        if not self.max_stack:
            self.max_stack.append(x)
        else:
            self.max_stack.append(max(x, self.max_stack[-1]))

    
    def pop(self):
        # Remove the top element from the Stack
        self.stack.pop()
        self.max_stack.pop()

    
    def peek(self):
        # Returns top element of Stack
        return self.stack[-1] if self.stack else -1
        
    
    def isEmpty(self):
        # Check if the stack is empty
        return len(self.stack) == 0
        
    
    def getMax(self):
        # Finds maximum element of Stack
        return self.max_stack[-1] if self.max_stack else -1

sol = SpecialStack()
sol.push(5)
sol.push(2)
sol.push(10)
sol.push(1)
print(sol.getMax())