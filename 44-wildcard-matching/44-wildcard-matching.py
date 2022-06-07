class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        dp = [[None for j in range(m+1)]for i in range(n+1)]
        
        dp[0][0] = True
        
        for i in range(1,n+1):
            dp[i][0] = False
        
        for j in range(1,m+1):
            dp[0][j] = True
            for x in range(1,j+1):
                if p[x-1] != "*":
                    dp[0][j] = False
                    break
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                
                if p[j-1] == "*":
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                
                elif s[i-1] == p[j-1] or  p[j-1] == "?":
                    dp[i][j] = dp[i-1][j-1]
                    
                else:
                    dp[i][j] = False
        
        return dp[n][m]
        
        
        
        
        
        
        
#         def matching(s_idx,p_idx):
#             if p_idx < 0 and s_idx < 0:
#                 return True
#             if p_idx < 0 and s_idx >= 0:
#                 return False
            
#             if s_idx < 0 and p_idx >= 0 :
#                 for i in range(p_idx+1):
#                     if p[i] != "*":
#                         return False
#                 return True
            
#             if s[s_idx] == p[p_idx] or p[p_idx] == "?":
#                 return matching(s_idx-1,p_idx-1)
            
#             if p[p_idx] == "*":
#                 return matching(s_idx-1,p_idx) or matching(s_idx,p_idx-1)
            
#             return False
        
#         return matching(len(s)-1,len(p)-1)
