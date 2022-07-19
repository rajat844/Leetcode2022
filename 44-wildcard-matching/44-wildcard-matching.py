class Solution:
    def isMatch(self, s: str, p: str) -> bool:        
        dp = [[None for i in range(len(p)+1)]for j in range(len(s)+1)]
        dp[0][0] = True
        
        for i in range(1,len(s)+1):
            dp[i][0] = False
        
        for j in range(1,len(p)+1):
            dp[0][j] = True
            for x in range(j,0,-1):
                if p[x-1] != "*":
                    dp[0][j] = False
                    break
                    
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if s[i-1] == p[j-1] or p[j-1] == "?":
                    dp[i][j] =  dp[i-1][j-1]
                elif p[j-1] == "*":
                    dp[i][j] =  dp[i-1][j] or dp[i][j-1]
                else :
                    dp[i][j] = False
                    
        return dp[len(s)][len(p)]
                
        