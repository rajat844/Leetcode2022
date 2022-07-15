class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def countArea(i,j):
            if 0 <= i < n and 0 <= j < m and grid[i][j] == 1:
                grid[i][j] = 0
                t1 = countArea(i+1,j)
                t2 = countArea(i,j+1)
                t3 = countArea(i-1,j)
                t4 = countArea(i,j-1)
                return 1+t1+t2+t3+t4
            else:
                return 0
        ans = 0
        n = len(grid)
        m = len(grid[0])
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    ans = max(ans,countArea(i,j))
        
        return ans
        