class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        dp = [[-1 for i in range(2)] for j in range(n+1)]
        dp[n][0] = dp[n][1] = 0
        
        
        for i in range(n-1,-1,-1):
            for buy in range(0,2,1):
                if buy == 1:
                    dp[i][buy] = max(-prices[i] + dp[i+1][0],dp[i+1][1])
                else :
                    dp[i][buy] = max(prices[i] + dp[i+1][1], dp[i+1][0])
        
        return dp[0][1]

        