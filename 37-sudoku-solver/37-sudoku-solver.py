class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
   
        def isValid(row,col,x):
            for i in range(9):
                if board[i][col] == str(x):
                    return False
                if board[row][i] == str(x):
                    return False
                if board[3*(row//3)+ i//3][3*(col//3) + i%3] == str(x):
                    return False
                
            return True
        
        def isValidSudoku():
            for i in range(n):
                for j in range(m):
                    
                    if board[i][j] == ".":
                        for x in range(1,10):
                            if isValid(i,j,x):
                                board[i][j] = str(x)
                                
                                if isValidSudoku() == True:
                                    return True
                                else:
                                    board[i][j] = "."
                        
                        return False
                    
            return True
        
        n = len(board)
        m = len(board[0])
        isValidSudoku()