class Solution:
    def searchRange(self, arr: List[int], target: int) -> List[int]:
        def binary(flag):
            l = 0
            h = len(arr) - 1
            prev = -1
            
            while l <= h:
                mid = (l+h) >> 1
                
                if arr[mid] == target:
                    prev = mid
                    if flag == True:
                        h = mid - 1
                    else :
                        l = mid + 1
                elif arr[mid] < target:
                    l = mid + 1
                else :
                    h = mid - 1
                    
            return prev
        
        start = binary(True)
        end = binary(False)
        return [start,end]