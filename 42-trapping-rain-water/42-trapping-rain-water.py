class Solution:
    def trap(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        
        ans = 0 
        leftmax = 0
        rightmax = 0
        
        while i <= j :
            if heights[i] <= heights[j]:
                if heights[i] >= leftmax:
                    leftmax = heights[i]
                else:
                    ans += leftmax - heights[i]
                i += 1
            else:
                if heights[j] >= rightmax:
                    rightmax = heights[j]
                else:
                    ans += rightmax - heights[j]
                j -= 1
                
        return ans
                    
        