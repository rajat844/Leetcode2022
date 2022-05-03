class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [[None for i in range(n)]for i in range(n)]
        
        for i in range(n-1,-1,-1):
            for j in range(n):
                if i > j:
                    dp[i][j] = False
                elif s[i:j+1] in wordDict:
                    dp[i][j] = True
                else :
                    if dp[i][j] != None:
                        dp[i][j] = True
                    else:
                        for k in range(i,j):
                            x = dp[i][k]
                            y = dp[k+1][j]
                            
                            if x and y :
                                dp[i][j] = True
        return dp[0][n-1]
                        
#         def helper(i,j):
#             if i > j :
#                 return True
            
#             if s[i:j+1] in wordDict:
#                 return True
            
#             ans = False
            
#             for k in range(i,j):
#                 x = helper(i,k)
#                 y = helper(k+1,j)
                
#                 if x and y:
#                     return True
        
#         return helper(0,len(s) - 1)
        
                
        