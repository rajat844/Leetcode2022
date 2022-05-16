class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1 for j in range(2)] for i in range(n+1)]
        
        prev0= prev1 = 0
    
        for i in range(n-1,-1,-1):
            temp1 = max(-1*prices[i]+prev0,prev1)
            temp0 = max(prices[i] +prev1,prev0)
            prev1 = temp1
            prev0 = temp0
        
        return prev1
            
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
                
        