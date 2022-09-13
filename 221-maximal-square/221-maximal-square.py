class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        dp = {}
        
        def recursion(r,c):
            if r >= ROWS or c >= COLS:
                return 0
            
            if (r,c) not in dp:
    
                down = recursion(r+1,c)
                right = recursion(r,c+1)
                diag = recursion(r+1,c+1)
                
                dp[(r,c)] = 0
                if matrix[r][c] == "1":
                    dp[(r,c)]= 1+ min(down,right,diag)
            
            return dp[(r,c)]
        
        recursion(0,0)
        
        return max(dp.values())**2
            
        