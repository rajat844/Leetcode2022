class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        def isClosed(i,j):
            if i >= n or j >= m or i < 0 or j < 0:
                return False
            if grid[i][j] == 1:
                return True
            grid[i][j] = 1
            up = isClosed(i,j-1)
            down = isClosed(i,j+1)
            right = isClosed(i+1,j)
            left = isClosed(i-1,j)
            
            return up and down and left and right
        
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0 and isClosed(i,j):
                    ans += 1
        
        return ans
                    