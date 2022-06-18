class Solution:
    def maxArea(self, arr: List[int]) -> int:
        l = 0
        r = len(arr) - 1
        maxarea = 0
        
        while l < r:
            h = min(arr[l],arr[r])
            w = r - l
            maxarea = max(maxarea,h*w)
            if arr[l] > arr[r]:
                r -= 1
            else :
                l += 1
        
        return maxarea
            
             
        