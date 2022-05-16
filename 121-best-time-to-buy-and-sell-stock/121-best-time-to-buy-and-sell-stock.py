class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        minprice = max(prices)
        
        for i in range(len(prices)):
            minprice = min(prices[i],minprice)
            maxprofit = max(maxprofit,prices[i] - minprice)
        
        return maxprofit
            