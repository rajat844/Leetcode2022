from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dx = [1,1,1,0,0,-1,-1,-1]
        dy = [1,0,-1,-1,1,1,0,-1]
        
        st = deque()
        if grid[0][0] == 1:
            return -1
        else :
            st.append((0,0))
            grid[0][0] = 1
        
        ans = 1
        
        while len(st) > 0:
            k = len(st)
            while k > 0:
                k -= 1
                x,y = st.popleft()
                if x == n-1 and y == m-1:
                    return ans
                
                for i in range(8):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    
                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0:
                        st.append((nx,ny))
                        grid[nx][ny] = 1
            ans += 1
        
        return -1

                
        