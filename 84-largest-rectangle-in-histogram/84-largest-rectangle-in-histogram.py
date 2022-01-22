class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxA = 0
        for i in range(0,len(heights)+1,1):
            while len(stack) > 0 and (i == len(heights) or heights[stack[-1]] >= heights[i]):
                hi = heights[stack[-1]]
                stack.pop()
                wi = 0
                if len(stack) == 0:
                    wi = i
                else :
                    wi = i - stack[-1] -1
                maxA = max(maxA,wi * hi)  
            stack.append(i)
        return maxA
        