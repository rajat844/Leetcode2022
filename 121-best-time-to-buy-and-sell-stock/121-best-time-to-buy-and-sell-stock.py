import math
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = math.inf
        maxprofit = 0
        
        for i in range(len(prices)):
            minprice = min(prices[i],minprice)
            maxprofit = max(maxprofit,prices[i]- minprice )
        return maxprofit
        