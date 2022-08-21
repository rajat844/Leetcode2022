class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def helper(i,j):
            nonlocal ans
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
                if grid[i][j] == 2:
                    grid[i][j] = -1
                    for x in range(len(grid)):
                        for y in range(len(grid[0])):
                            if grid[x][y] != -1:
                                grid[i][j] = 2
                                return
                    ans += 1                                
                    grid[i][j] = 2
                    return
                
                elif grid[i][j] != -1:
                    x = grid[i][j]
                    grid[i][j] = -1
                    helper(i+1,j)
                    helper(i-1,j)
                    helper(i,j+1)
                    helper(i,j-1)
                    grid[i][j] = x                              
                            
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    helper(i,j)
        
        return ans
        