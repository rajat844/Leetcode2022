class Solution:
    def maxArea(self, heights: List[int]) -> int:
        r = len(heights) -1 
        l = 0
        ans = 0
        while l < r:
            if heights[r] > heights[l]:
                tempans = (r-l )* heights[l]
                l += 1
                
            else :
                tempans = (r-l) * heights[r]
                r -= 1
            ans = max(ans,tempans)
        
        return ans
        