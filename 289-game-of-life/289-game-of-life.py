class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 0 0 0
        # 1 0 1
        # 0 1 2
        # 1 1 3
        def countindex(row,col):
            cnt = 0
            
            for i in range(row-1,row+2):
                for j in range(col-1,col+2):
                    if (i == row and j == col) or i < 0 or j < 0 or i >= n or j >= m:
                        continue
                    elif board[i][j] == 1 or board[i][j] == 3:
                        cnt += 1
            return cnt
        
        
        n = len(board)
        m = len(board[0])
        
        for i in range(n):
            for j in range(m):
                cnt = countindex(i,j)
                
                if board[i][j] == 0:
                    if cnt == 3:
                        board[i][j] = 2
                        
                elif cnt == 2 or cnt == 3:
                    board[i][j] = 3
        
        for i in range(n):
            for j in range(m):
                board[i][j] = board[i][j] // 2