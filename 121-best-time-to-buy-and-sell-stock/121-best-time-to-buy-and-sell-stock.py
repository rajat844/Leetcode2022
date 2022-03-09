import math
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = math.inf
        profit = 0
        
        for i in range(len(prices)):
            minprice = min(prices[i],minprice)
            profit = max(profit,prices[i] - minprice)
        
        return profit
        