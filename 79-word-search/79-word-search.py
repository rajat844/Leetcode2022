class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def recursion(i,j,index):
            if index == len(word):
                return True
            if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == word[index]:
                board[i][j] = None
                if recursion(i+1,j,index+1) == True:
                    return True
                if recursion(i-1,j,index+1) == True:
                    return True
                if recursion(i,j+1,index+1) == True:
                    return True
                if recursion(i,j-1,index+1) == True:
                    return True
                board[i][j] = word[index]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if recursion(i,j,0) == True:
                    return True
        
        return False
                
            
            
        