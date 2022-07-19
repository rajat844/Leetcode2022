class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def match(i,j):
            if dp[i][j] != None:
                return dp[i][j]
            if i < 0 and j < 0:
                dp[i][j] = True
                return dp[i][j]
            if j < 0 :
                dp[i][j] = False
                return dp[i][j]
            if i < 0 :
                for x in range(j,-1,-1):
                    if p[x] != "*":
                        dp[i][j] = False
                        return dp[i][j]
                dp[i][j] = True
                return dp[i][j]
            
            if s[i] == p[j] or p[j] == "?":
                dp[i][j] =  match(i-1,j-1)
                return dp[i][j]
            if p[j] == "*":
                dp[i][j] =  match(i-1,j) or match(i,j-1)
                return dp[i][j]
            dp[i][j] =  False
            return dp[i][j]
        
        dp = [[None for i in range(len(p)+1)]for j in range(len(s)+1)]
        return match(len(s)-1,len(p)-1)
                
        