class MinStack:

    def __init__(self):
        self.stack = []
        self.min_vals = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_vals or self.min_vals[-1]>=val:
            self.min_vals.append(val)

    def pop(self) -> None:
        val = self.stack[-1]
        self.stack.pop(-1)
        if self.min_vals:
            if val == self.min_vals[-1]:
                self.min_vals.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.min_vals:
            return 0
        return self.min_vals[-1]
