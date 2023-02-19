# Getting both the minimum and maximum values in the stack at any given point in time and should run in
# constant time and space

class MinMaxStack:

    def __init__(self):
        self.stack = []
        # initializing a minMax array to save current min and max number of the array [min,max]
        self.minMaxStack = []
        
    # peek return you the top value of the stack (no pop)
    def peek(self):
        return self.stack[len(self.stack)-1]

    def pop(self):
        self.minMaxStack.pop()
        return self.stack.pop()
        

    def push(self, number):
        # if it is the first element to push in stack so it is itself min and max
        currMinMax = [number, number]
        if len(self.minMaxStack):
            currMin,currMax = self.minMaxStack[len(self.minMaxStack)-1]
            # changing min and max if minMaxStack has values previously i.e not the first push in stack
            currMinMax[0] = min(number,currMin)
            currMinMax[1] = max(number,currMax)
        self.minMaxStack.append(currMinMax)
        self.stack.append(number)

    def getMin(self):
        return self.minMaxStack[len(self.minMaxStack)-1][0]

    def getMax(self):
        return self.minMaxStack[len(self.minMaxStack)-1][1]


stack = MinMaxStack()

print(stack.push(5))
print(stack.getMax()) #5
print(stack.getMin()) #5
print(stack.peek() )#5
print(stack.push(7))
print(stack.getMax()) #7
print(stack.getMin()) #5
print(stack.peek()) #7
print(stack.push(2))
print(stack.getMax()) #7
print(stack.getMin()) #2
print(stack.pop()) #2
print(stack.getMax()) #7
print(stack.getMin()) #5
