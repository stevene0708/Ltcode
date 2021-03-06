"""
    Author: Weng Xiang Heng
    Date: 2021/10/25
"""

class MinStack:

    def __init__(self):
        self.stack = []        

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        pop_e = self.stack.pop()
        return pop_e

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        min_ = 2**31 -1
        for i in self.stack:
            if(i <= min_):
                min_ = i
        return min_


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()