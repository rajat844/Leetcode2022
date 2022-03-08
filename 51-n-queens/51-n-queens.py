class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = [["."for i in range(n)]for i in range(n)]
        
        def isSafe(row,col):
            tem_row,tem_col = row,col
            while row >= 0 and col >= 0:
                if board[row][col] == 'Q':
                    return False
                row -= 1
                col -= 1
            
            row,col = tem_row,tem_col
            while col >= 0:
                if board[row][col] == 'Q':
                    return False
                col -= 1
            
            row,col = tem_row,tem_col
            while row<n and col >= 0:
                if board[row][col] == 'Q':
                    return False
                col -= 1
                row += 1
            
            return True
            
        def helper(col):
            if n == col:
                t = [''.join(row) for row in board]
                ans.append(t)
                return 
            for row in range(n):
                if isSafe(row,col):
                    board[row][col] = 'Q'
                    helper(col+1)
                    board[row][col] = '.'
        helper(0)
        return ans
            
        