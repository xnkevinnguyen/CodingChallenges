class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list = []

    def push(self, x: int) -> None:
        if self.list:
            self.list.append((x, min(x, self.list[-1][1])))
        else:
            self.list.append((x, x))
        print(self.list)

    def pop(self) -> None:
        if self.list:
            self.list.pop()
        print(self.list)

    def top(self) -> int:
        if self.list:
            return self.list[len(self.list)-1][0]
        print(self.list)

    def getMin(self) -> int:
        print(self.list[-1][1])
        return self.list[-1][1]

        # Your MinStack object will be instantiated and called as such:
        # obj = MinStack()
        # obj.push(x)
        # obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.getMin()


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
