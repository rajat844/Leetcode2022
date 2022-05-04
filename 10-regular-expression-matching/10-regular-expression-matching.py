class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[None for j in range(len(p))] for i in range(len(s)+1)]
        def helper(i,j):
            if j ==  len(p):
                return i == len(s)
            
            if dp[i][j] != None:
                return dp[i][j]
            
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            
            if j + 1 < len(p) and p[j+1] == "*":
                dp[i][j] = helper(i,j+2) or (match  and helper(i+1,j))
            
            elif match == True:
                dp[i][j]= helper(i+1,j+1)
            else :
                dp[i][j] =  False
                
            return dp[i][j]
        
        return helper(0,0)