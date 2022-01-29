class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ans = 0
        
        for i in range(len(heights)+1):
            while(len(stack) > 0 and (i==len(heights) or heights[stack[-1]] >= heights[i])):
                curr = stack[-1]
                stack.pop()
                h = heights[curr]
                w = 0
                if len(stack) == 0:
                    w = i
                else :
                    w = i -stack[-1] -1
                ans = max(ans,h*w)
                
            stack.append(i)
        return ans
            