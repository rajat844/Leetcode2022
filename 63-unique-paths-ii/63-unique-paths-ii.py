class Solution:
    def uniquePathsWithObstacles(self, dp: List[List[int]]) -> int:
        n = len(dp)
        m = len(dp[0])
        
        for i in range(1,n):
            if dp[i-1][0] == 1:
                dp[i][0] = 1
                
        for j in range(1,m):
            if dp[0][j-1] == 1:
                dp[0][j] = 1
        
        for i in range(n):
            for j in range(m):
                if dp[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = 1
        
        for i in range(1,n):
            for j in range(1,m):
                if dp[i][j] != 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[n-1][m-1]