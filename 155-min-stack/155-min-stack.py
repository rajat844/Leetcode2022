import math
class MinStack:

    def __init__(self):
        self.st = []
        self.min = math.inf
        

    def push(self, val: int) -> None:
        if len(self.st) == 0:
            self.st.append(val)
            self.min = val
        else:
            if val >= self.min:
                self.st.append(val)
            else:
                x = 2 * val - self.min
                self.st.append(x)
                self.min = val

    def pop(self) -> None:
        if len(self.st) > 0:
            if self.min <= self.st[-1]:
                self.st.pop()
            else:
                x = 2 * self.min - self.st[-1]
                self.min = x
                self.st.pop()
                
            

    def top(self) -> int:
        if len(self.st) > 0:
            if self.min <= self.st[-1]:
                return self.st[-1]
            else:
                return self.min
        return None
        

    def getMin(self) -> int:
        if len(self.st) > 0:
            return self.min
        return None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()