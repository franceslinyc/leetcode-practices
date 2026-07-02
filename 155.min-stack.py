#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self):

        self.stack = []

        self.min_stack = []
        

    def push(self, value: int) -> None:

        self.stack.append(value)

        if self.min_stack: 

            value = min(value, self.min_stack[-1])

        self.min_stack.append(value)
        

    def pop(self) -> None:

        self.stack.pop()

        self.min_stack.pop()
        

    def top(self) -> int:

        return self.stack[-1]
        

    def getMin(self) -> int:

        return self.min_stack[-1]
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

