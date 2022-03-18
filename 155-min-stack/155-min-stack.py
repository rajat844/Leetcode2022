import math
class MinStack:

    def __init__(self):
        self.st = []
        self.min = math.inf
        

    def push(self, val: int) -> None:
        if len(self.st) == 0:
            self.min = val
            self.st.append(val)
            
        else :
            if val < self.min:
                self.st.append(2 * val - self.min)
                self.min = val
            else:
                self.st.append(val)
        
    def pop(self) -> None:
        if len(self.st) == 0 :
            return
        y = self.st.pop()
        if y < self.min:
            self.min = 2 *self.min - y
    
    def top(self) -> int:
        if self.st[-1] < self.min:
            return self.min
        else :
            return self.st[-1]

    def getMin(self) -> int:
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()