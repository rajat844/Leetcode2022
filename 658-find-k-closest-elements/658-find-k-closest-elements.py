class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        h = len(arr) - k
        
        while l < h:
            mid = (l+h) >> 1
            if x - arr[mid] > arr[mid+k] - x:
                l = mid + 1
            else :
                h = mid
        
        return arr[l:l+k]
            
            
        