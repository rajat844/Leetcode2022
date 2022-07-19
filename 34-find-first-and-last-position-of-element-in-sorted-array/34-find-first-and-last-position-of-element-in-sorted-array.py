class Solution:
    def searchRange(self, arr: List[int], target: int) -> List[int]:
        def binary(flag):
            l = 0
            h = len(arr) - 1
            ans = -1
            while l <= h:
                mid = (l+h) >> 1
                if arr[mid] == target:
                    ans = mid
                    if flag == True:
                        l = mid + 1
                    else :
                        h = mid - 1
                elif arr[mid] > target:
                    h = mid - 1
                else :
                    l = mid + 1
            return ans
        
        start = binary(False)
        end = binary(True)
        return [start,end]