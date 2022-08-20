class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def helper(i,j,s):
            if s == len(word) :
                return True
            if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == word[s]:
                board[i][j] = None
                if helper(i+1,j,s+1) or helper(i,j+1,s+1) or helper(i,j-1,s+1) or helper(i-1,j,s+1):
                    return True
                board[i][j] = word[s]
            else:
                return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if helper(i,j,0):
                    return True
        
        return False
                
                
            
            
        