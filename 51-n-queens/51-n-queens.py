class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board =[['.' for i in range(n)]for j in range (n)]
        ans = []
        
        def issafe(col,row):
            duplrow = row
            duplcol = col
            
            while row >= 0 and col >= 0:
                if board[row][col] == 'Q':
                    return False
                row -= 1
                col -= 1
                
            row = duplrow
            col = duplcol
            
            while col >= 0:
                if board[row][col] == 'Q':
                    return False
                col -= 1
                
            row = duplrow
            col = duplcol
            
            while col >= 0 and row < n:
                if board[row][col] == 'Q':
                    return False
                col -= 1
                row += 1
                
            row = duplrow
            col = duplcol
            return True
                
        def helper(col):
            if col == n:
                t = [''.join(row) for row in board]
                ans.append(t)
                return
            for row in range(n):
                if(issafe(col,row)):
                    board[row][col] = 'Q'
                    helper(col+1)
                    board[row][col] = '.'
                    
        helper(0)
        return ans
            
                        
        