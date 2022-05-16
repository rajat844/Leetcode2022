class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1 for j in range(2)] for i in range(n+1)]
        
        dp[n][0] = dp[n][1] = 0
    
        for i in range(n-1,-1,-1):
            dp[i][1] = max(-1*prices[i]+dp[i+1][0],dp[i+1][1])
            dp[i][0] = max(prices[i] + dp[i+1][1],dp[i+1][0])
        
        return dp[0][1]
            
#         def helper(i,b):
#             if i == len(prices):
#                 return 0
#             case1 = 0
#             case2 = 0
#             if b == True:
#                 case1 = -1*prices[i] + helper(i+1,False)
#                 case2 = helper(i+1,True)
#             else:
#                 case1 = prices[i] + helper(i+1,True)
#                 case2 = helper(i+1,False)
            
#             return max(case1,case2)
        
#         return helper(0,True)
                
        