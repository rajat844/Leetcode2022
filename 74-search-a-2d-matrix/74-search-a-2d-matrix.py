class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        
        l = 0
        h = n-1
        
        while  l <= h:
            mid = (l+h)>>1
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                l = mid + 1
            else:
                h = mid - 1
        
        r = h
        
        l = 0
        h = m-1
        
        while l <= h:
            mid = (l+h) >>1
            if matrix[r][mid] == target:
                return True
            elif matrix[r][mid] <= target:
                l = mid + 1
            else :
                h = mid -1
        
        return False
                
            
        