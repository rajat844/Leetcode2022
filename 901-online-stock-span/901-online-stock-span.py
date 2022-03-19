class StockSpanner:

    def __init__(self):
        self.st = []
        self.prices = []
        

    def next(self, price: int) -> int:
        self.prices.append(price)
        i = len(self.prices) - 1
        
        while len(self.st) > 0 and self.prices[self.st[-1]] <= price:
            self.st.pop()
            
        ans = 0
            
        if len(self.st) == 0:
            ans = i+1
        else :
            ans = i-self.st[-1]
        self.st.append(i)
        return ans
        
        
            
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)