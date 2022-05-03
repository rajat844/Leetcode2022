class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [[None for i in range(n)]for i in range(n)]
                        
        def helper(i,j):
            if i > j :
                dp[i][j] = False
                return dp[i][j]
            if dp[i][j] != None:
                return dp[i][j]
            
            if s[i:j+1] in wordDict:
                dp[i][j] = True
                return dp[i][j]

            for k in range(i,j):
                x = helper(i,k)
                y = helper(k+1,j)
                
                if x and y:
                    dp[i][j] = True
                    return dp[i][j]
            dp[i][j] = False
        return helper(0,len(s) - 1)
        
                
        