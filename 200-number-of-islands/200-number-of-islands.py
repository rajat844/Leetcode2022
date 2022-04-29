class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def helper(i,j):
            if 0 <= i < n and 0 <= j < m and grid[i][j] == "1":
                grid[i][j] = "0"
                
                helper(i+1,j)
                helper(i-1,j)
                helper(i,j+1)
                helper(i,j-1)
            
            
        n = len(grid)
        m = len(grid[0])
        
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    ans += 1
                    helper(i,j)
        return ans
                    