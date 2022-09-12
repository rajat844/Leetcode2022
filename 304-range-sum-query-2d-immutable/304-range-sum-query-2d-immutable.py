class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.SumMatrix = []
        for i in range(len(matrix)):
            temp = []
            temp.append(matrix[i][0])
            for j in range(1,len(matrix[i])):
                temp.append(temp[-1] + matrix[i][j])
            
            self.SumMatrix.append(temp)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for i in range(row1,row2+1,+1):
            if col1 != 0:
                ans += self.SumMatrix[i][col2] - self.SumMatrix[i][col1-1]
            else:
                ans += self.SumMatrix[i][col2]
                
        return ans
        pass
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)