class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle[-1])
        n = len(triangle)
        dp = [[-1 for i in range(m)]for j in range(n)]
        
        for i in range(m):
            dp[n-1][i] = triangle[n-1][i]
        
        for i in range(n-2,-1,-1):
            for j in range(len(triangle[i])-1,-1,-1):
                dp[i][j] = triangle[i][j] + min(dp[i+1][j],dp[i+1][j+1])
        
        return dp[0][0]
        
#         def recursion(i,j):
#             if dp[i][j] != -1:
#                 return dp[i][j]
            
#             if i == len(triangle) - 1:
#                 dp[i][j] =  triangle[i][j]
#                 return dp[i][j]
            
#             dp[i][j] = triangle[i][j] + min(recursion(i+1,j),recursion(i+1,j+1))
#             return dp[i][j]
        
#         return recursion(0,0)
                
            
            
        