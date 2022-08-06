class MyCalendar:

    def __init__(self):
        self.st = []

    def book(self, start: int, end: int) -> bool:
        for i in range(len(self.st)):
            if end > self.st[i][0] and start < self.st[i][1]:
                return False
        
        self.st.append((start,end))
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)