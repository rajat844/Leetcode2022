from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        st = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    st.append((i,j))
        ans = 0
        while len(st) > 0:
            s = len(st)
            
            while s > 0:
                i,j = st.popleft()
                s -= 1
                
                if i-1 >= 0 and grid[i-1][j] == 1:
                    grid[i-1][j] = 2
                    st.append((i-1,j))
                if j-1 >= 0 and grid[i][j-1] == 1:
                    grid[i][j-1] = 2
                    st.append((i,j-1)) 
                if i+1 < n and grid[i+1][j] == 1:
                    grid[i+1][j] = 2
                    st.append((i+1,j))
                if j+1 < m and grid[i][j+1] == 1:
                    grid[i][j+1] = 2
                    st.append((i,j+1))
            if len(st) > 0:
                ans += 1
            
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
                
        return ans