from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        rotten = deque()
        total = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    total += 1
                if grid[i][j] == 2:
                    rotten.append((i,j))
                    
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        days = 0
        count = 0
        while len(rotten) > 0:
            x = len(rotten)
            count += x
            while x > 0:
                x -= 1
                nx,ny = rotten.popleft()
                for j in range(4):
                    a = nx + dx[j]
                    b = ny + dy[j]
                    if a < 0 or a >= m or b < 0 or b >= n or grid[a][b] != 1:
                        continue
                    else:
                        grid[a][b] = 2
                        rotten.append((a,b))
            if len(rotten) > 0 :
                days += 1
            
        if total == count:
            return days
        else :
            return -1