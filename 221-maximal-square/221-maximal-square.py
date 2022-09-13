class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        
        dp = [[None for i in range(cols)] for j in range(rows)]
        
        def recursion(r,c):
            if r >= rows or c >= cols:
                return 0
            
            if dp[r][c] != None:
                return dp[r][c]
            
            bottom = recursion(r+1,c)
            right = recursion(r,c+1)
            diag = recursion(r+1,c+1)
            
            dp[r][c] = 0
            if matrix[r][c] == "1":
                dp[r][c] = 1+ min(bottom,right,diag)
            
            return dp[r][c]
        
        recursion(0,0)
        
        mx = 0
        for x in range(rows):
            mx = max(mx,max(dp[x]))
        
        return mx**2
        