from collections import deque
class MyStack:

    def __init__(self):
        self.st = deque()
        

    def push(self, x: int) -> None:
        self.st.append(x)
        n = len(self.st)
        for i in range(n-1):
            self.st.append(self.st.popleft())
        

    def pop(self) -> int:
        if len(self.st) > 0:
            x = self.st.popleft()
            return x
        else :
            return None

    def top(self) -> int:
        if len(self.st) > 0:
            return self.st[0]
        return None

    def empty(self) -> bool:
        if len(self.st)> 0:
            return False
        return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()