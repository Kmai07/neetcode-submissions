class MinStack:
    # create a second stack to keep track of the min value
    # edge case inlcude when the min stack is empty have to reset min value to orginal value
    # another edge is that 
    def __init__(self):
        self.__st = []
        self.__stack = []
        self.__mi = pow(2, 31) - 1

    def push(self, val: int) -> None:
        if val <= self.__mi:
            self.__mi = val
            self.__st.append(self.__mi)
        self.__stack.append(val)

    def pop(self) -> None:
        if self.__stack[-1] == self.__mi:
            self.__st.pop()
            if len(self.__st) > 0:
                self.__mi = self.__st[-1]
            else:
                self.__mi = pow(2, 31) - 1
        self.__stack.pop()

    def top(self) -> int:
        return self.__stack[-1]

    def getMin(self) -> int:
        return self.__st[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
