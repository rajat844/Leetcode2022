class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(i,j,dp):
            dp[i][j] = True
            
            for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
                a,b = i+x,j+y
                if a < 0 or a >= m or b < 0 or b >= n or dp[a][b] or heights[a][b] < heights[i][j]:
                    continue
                dfs(a,b,dp)
                
            
            
        m = len(heights)
        n = len(heights[0])  
        
        p_dp = [[False for i in range(n)] for j in range(m)]
        a_dp = [[False for i in range(n)] for j in range(m)]
        
        ans = []
        
        
        for i in range(m):
            dfs(i,0,p_dp)
            dfs(i,n-1,a_dp)
        
        for j in range(n):
            dfs(0,j,p_dp)
            dfs(m-1,j,a_dp)
            
            
        for i in range(m):
            for j in range(n):
                if p_dp[i][j] and a_dp[i][j]:
                    ans.append([i,j])
                    
        return ans
        