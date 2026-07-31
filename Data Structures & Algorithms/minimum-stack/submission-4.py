class MinStack:

    def __init__(self):
        self.stack:list[int] = []
        self.lowest:list[int] = []

    def push(self, val: int) -> None:
        if not self.lowest:
            self.lowest.append(val)
        elif self.lowest[-1] >= val:
            self.lowest.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        popped_value = self.stack.pop()
        if popped_value == self.lowest[-1]:
            self.lowest.pop()
        return None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.lowest[-1]
