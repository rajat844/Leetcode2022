class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[-1 for i in range(2)]for j in range(3)]for k in range(n+1)]
        
        def recursion(isBuy,i,cnt):
            if i == len(prices) or cnt == 2:
                return 0
            if dp[i][cnt][isBuy] != -1:
                return dp[i][cnt][isBuy]
            
            if isBuy == True:
                dp[i][cnt][isBuy] = max(-prices[i] + recursion(0,i+1,cnt),recursion(1,i+1,cnt))
                return dp[i][cnt][isBuy]
            else :
                dp[i][cnt][isBuy] = max(prices[i] + recursion(1,i+1,cnt+1),recursion(0,i+1,cnt))
                return dp[i][cnt][isBuy]
        
        return recursion(1,0,0)
                