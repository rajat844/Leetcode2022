class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        def countpaths(i,j):
            if dp[i][j] != -1 :
                return dp[i][j]
            
            res = 1
            
            for d in range(4):
                x = i+drs[d]
                y = j+drs[d+1]
                
                if 0 <= x < n and 0 <= y < m and grid[x][y] > grid[i][j]:
                    res += countpaths(x,y)
            
            dp[i][j] = res
            return dp[i][j]
        
        n = len(grid)
        m = len(grid[0])
        drs = [0,1,0,-1,0]
        
        dp = [[-1 for i in range(m)]for j in range(n)]
        ans = 0
        
        for i in range(n):
            for j in range(m):
                ans += countpaths(i,j)
        
        return ans % (10**9+7)