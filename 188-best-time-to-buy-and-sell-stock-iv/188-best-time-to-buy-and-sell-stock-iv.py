class Solution:
    def maxProfit(self, cnt: int, prices: List[int]) -> int:
        n = len(prices)
        
        dp = [[[0 for i in range(cnt+1)]for j in range(2)]for k in range(n+1)]
    
        for i in range(n-1,-1,-1):
            for j in range(2):
                for k in range(cnt-1,-1,-1):
                    if j == 1:
                        dp[i][j][k] =  max(prices[i]+dp[i+1][0][k+1],dp[i+1][1][k])
                    else:
                        dp[i][j][k] =  max(-prices[i]+dp[i+1][1][k],dp[i+1][0][k]) 
            
        return dp[0][0][0]
        
#         def helper(i,isSell,cnt):
#             if i == len(prices) or cnt == k:
#                 return 0
            
#             if isSell == 1:
#                 return max(prices[i]+helper(i+1,0,cnt+1) , helper(i+1,1,cnt))
#             else:
#                 return max(-prices[i]+helper(i+1,1,cnt),helper(i+1,0,cnt))
        
#         return helper(0,0,0)