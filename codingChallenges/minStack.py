class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.minStack:
            self.minStack.append(min(x, self.minStack[-1]))
        else:
            self.minStack.append(x)
        self.printStacks()

    def pop(self) -> None:
        if self.stack:
            self.minStack.pop()
            self.stack.pop()
        self.printStacks()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        self.printStacks()

    def getMin(self) -> int:
        if self.minStack:
            print(self.minStack[-1])
            return self.minStack[-1]

    def printStacks(self) -> None:
        print("stack: ", self.stack, ", min stack: ", self.minStack)


# test1
minStack = MinStack()
minStack.push(2147483646)
minStack.push(2147483646)
minStack.push(2147483647)
minStack.top()
minStack.pop()
minStack.getMin()
minStack.pop()
minStack.getMin()
minStack.pop()
minStack.push(2147483647)
minStack.top()
minStack.getMin()
minStack.push(-2147483648)

# test2
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin()
minStack.pop()
minStack.top()
minStack.getMin()
