class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        def helper(i,j):
            if i >= 0 and j >= 0 and i < n and j < m and grid[i][j] == "1":
                grid[i][j] = "0"
                
                helper(i-1,j)
                helper(i,j-1)
                helper(i+1,j)
                helper(i,j+1)
        
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    helper(i,j)
                    ans += 1
        return ans