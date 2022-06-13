class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle[-1])
        n = len(triangle)
        dp = [[-1 for i in range(m)]for j in range(n)]
        
        def recursion(i,j):
            if dp[i][j] != -1:
                return dp[i][j]
            
            if i == len(triangle) - 1:
                dp[i][j] =  triangle[i][j]
                return dp[i][j]
            
            dp[i][j] = triangle[i][j] + min(recursion(i+1,j),recursion(i+1,j+1))
            return dp[i][j]
        
        return recursion(0,0)
                
            
            
        