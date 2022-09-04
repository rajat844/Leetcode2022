class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:
        def isPossible(row,col):
            i = row
            j = col
            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -=1
            
            i = row
            j = col
            
            while j >= 0:
                if board[i][j] == "Q":
                    return False
                j -= 1
            
            j = col
            
            while i < n and j >= 0:
                if board[i][j] == "Q":
                    return False
                j -= 1
                i += 1
            return True
                    
        def helper(col):
            nonlocal ans
            if col == n:
                ans += 1
                return 
            for row in range(n):
                if isPossible(row,col):
                    board[row][col] = "Q"
                    helper(col+1)
                    board[row][col] = "."
            
                    
            
        board = [["." for i in range(n)]for j in range(n)]
        ans = 0
        helper(0)
        return ans
        