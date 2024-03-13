from collections import deque


class MinStack(object):

    def __init__(self):
        self.stack = deque()

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.stack:  # empty stack
            minn = val
        elif self.stack[-1][1] > val:  # new min val
            minn = val
        else:  # old min val
            minn = self.stack[-1][1]
        self.stack.append((val, minn))

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        # print(self.stack[-1][0])
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        # print(self.stack[-1][1])
        return self.stack[-1][1]


funcs = [
    "MinStack",
    "push",
    "push",
    "getMin",
    "getMin",
    "push",
    "getMin",
    "getMin",
    "top",
    "getMin",
    "pop",
    "push",
    "push",
    "getMin",
    "push",
    "pop",
    "top",
    "getMin",
    "pop",
]
nums = [
    [],
    [-10],
    [14],
    [],
    [],
    [-20],
    [],
    [],
    [],
    [],
    [],
    [10],
    [-12],
    [],
    [-7],
    [],
    [],
    [],
    [],
]

for f, n in zip(funcs, nums):
    if f == "MinStack":
        minStack = MinStack()
    if f == "push":
        minStack.push(n[0])
        print(minStack.stack)
    if f == "pop":
        minStack.pop()
        print(minStack.stack)
    if f == "top":
        print(minStack.top())
    if f == "getMin":
        print(minStack.getMin())
