class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        @lru_cache(maxsize=None)
        def helper(i,j,k):
            if i < 0 or i >= n or j < 0 or j >= m or k < 0:
                return False
            
            if dp[i][j][k] != None:
                return dp[i][j][k]
            
            k += 1 if grid[i][j] == "(" else -1
            if i == n-1 and j == m-1 and k == 0:
                return True
            
            dp[i][j][k] = helper(i+1,j,k) or helper(i,j+1,k)
            
            return dp[i][j][k]
        
        
        n = len(grid)
        m = len(grid[0])
        
        dp = [[[None for i in range(n+m)]for j in range(m)]for k in range(n)]
        
        return helper(0,0,0)