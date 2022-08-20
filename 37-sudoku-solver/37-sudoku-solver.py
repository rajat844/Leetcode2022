class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValid(r,c,x):
            for i in range(9):
                if board[i][c] == str(x):
                    return False
                if board[r][i] == str(x):
                    return False
                if board[3*(r//3) + i//3][3*(c//3) + i%3] == str(x):
                    return False
            
            return True
        
        n = len(board)
        m = len(board[0])
        def helper():
            for i in range(n):
                for j in range(m):
                    if board[i][j] == ".":
                        for x in range(1,10):
                            if isValid(i,j,x):
                                board[i][j] = str(x)
                                if helper() ==  True:
                                    return True
                                board[i][j] = "."
                        return False
            return True
                
        
        return helper()
                                