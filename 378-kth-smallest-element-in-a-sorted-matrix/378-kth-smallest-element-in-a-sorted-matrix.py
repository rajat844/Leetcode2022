class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def greater(arr,target):
            l = 0
            h = len(arr) - 1
            
            while l <= h:
                mid = (l+h) >> 1
                if arr[mid] <= target:
                    l = mid + 1
                else:
                    h = mid - 1
            return l
            
        n = len(matrix)
        m = len(matrix[0])
        l = matrix[0][0]
        h = matrix[n-1][m-1]
        
        while l <= h:
            mid = (l+h)//2
            
            great = 0
            for i in range(n):
                great += greater(matrix[i],mid)
                
            if great < k:
                l = mid + 1
            else :
                h = mid - 1
        
        return int(l)
            
        