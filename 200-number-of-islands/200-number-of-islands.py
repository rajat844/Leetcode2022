class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
    
        rows, cols = len(grid), len(grid[0])
    
        def sink(r, c):
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == '1':
                grid[r][c] = '0'
            
                sink(r + 1, c)
                sink(r - 1, c)
                sink(r, c + 1)
                sink(r, c - 1)
    
        cnt = 0 
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    sink(r, c)
                    cnt += 1
        return cnt
        