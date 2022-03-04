class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        
        firstRow = False
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    if i == 0:
                        firstRow = True
                    else :
                        matrix[i][0] = 0
        
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
                    
        if matrix[0][0] == 0:
            for i in range(n):
                matrix[i][0] = 0
        
        if firstRow :
            for j in range(m):
                matrix[0][j] = 0
                