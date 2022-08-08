class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        0 0 0
        1 0 1
        0 1 2
        1 1 3
        """
        def neighbours(row,col):
            count = 0
            for i in range(row-1,row+2):
                for j in range(col-1,col+2):
                    if i >= n or j >= m or i < 0 or j < 0 or (i==row and j ==col):
                        continue
                    elif board[i][j] == 1 or board[i][j] == 3:
                        count += 1
            return count
                    
            
        n = len(board)
        m = len(board[0])
        
        for i in range(n):
            for j in range(m):
                
                cnt = neighbours(i,j)
                
                if board[i][j] == 1:
                    if cnt == 2 or cnt == 3:
                        board[i][j] = 3
                    
                elif cnt == 3:
                    board[i][j] = 2
        
        for i in range(n):
            for j in range(m):
                board[i][j] //=  2
                    
                    
       
        
        