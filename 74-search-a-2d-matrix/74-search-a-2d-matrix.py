class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        
        low = 0
        high = n-1
        
        while high >= low:
            mid = (high+low)//2
            
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                high = mid -1
            else :
                low = mid + 1
                
        row_number = high
        
        high = m-1
        low = 0
        
        while high >= low:
            mid = (high + low)//2
            if matrix[row_number][mid] == target:
                return True
            elif matrix[row_number][mid] > target:
                high = mid -1
            else :
                low = mid + 1
        
        return False
        
        