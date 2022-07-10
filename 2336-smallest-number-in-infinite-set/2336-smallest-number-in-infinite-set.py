import math
import heapq
class SmallestInfiniteSet:

    def __init__(self):
        self.currmin = 1
        self.st = []
        

    def popSmallest(self) -> int:
        res = self.currmin
        
        heapq.heapify(self.st)
        
        if len(self.st) > 0 and self.st[0] < self.currmin:
            res = heapq.heappop(self.st)
        else :
            self.currmin += 1
        
        while len(self.st) > 0 and res == self.st[0]:
            heapq.heappop(self.st)
        
        return res
        

    def addBack(self, num: int):
        if num < self.currmin:
            self.st.append(num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)