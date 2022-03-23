class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        dp = [[-1 for j in range(m)]for i in range(n)]
        
        
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if i == n-1 and j == m-1:
                    dp[i][j] = grid[i][j]
                    
                elif i == n-1:
                    dp[i][j] = dp[i][j+1] + grid[i][j]
                
                elif j == m-1:
                    dp[i][j] = dp[i+1][j] + grid[i][j]
                
                else:
                    dp[i][j] = min(dp[i+1][j],dp[i][j+1])+grid[i][j]
                    
        return dp[0][0]
                
                