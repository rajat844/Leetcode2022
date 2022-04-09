class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.st = nums
        self.k = k
        
        heapq.heapify(self.st)
        
        while len(self.st) > k:
            heapq.heappop(self.st)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.st,val)
        if len(self.st) > self.k:
            heapq.heappop(self.st)
        
        return self.st[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)