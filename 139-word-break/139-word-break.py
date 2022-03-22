class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [[None for i in range(n)]for j in range(n)]
        
        def helper(i,j):
            if i > j:
                return False
            
            if dp[i][j] != None:
                return dp[i][j]
            
            if s[i:j+1] in wordDict:
                dp[i][j] = True
                return dp[i][j]
            
            
            for k in range(i,j):
                lh = helper(i,k)
                rh = helper(k+1,j)
                if rh and lh :
                    ans = True
                    dp[i][j] = ans
                    return dp[i][j]
                
            dp[i][j] = False
            return dp[i][j]
            
        return helper(0,len(s) - 1)
            
                    
                    
                