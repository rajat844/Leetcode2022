class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack,left,right = [],[],[]
        for i in range(len(heights)):
            while len(stack) > 0 and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if len(stack) == 0 :
                left.append(0)
            else :
                left.append(stack[-1] + 1 )

            stack.append(i)
        
        stack.clear()
        
        for i in range(len(heights)-1,-1,-1):
            while len(stack) > 0 and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            if len(stack) == 0:
                right.append(len(heights)-1)
            else :
                right.append(stack[-1] - 1)

            stack.append(i)

        right.reverse()
        
        ans = []
        
        for i in range(len(heights)):
            ans.append(heights[i] * (right[i] - left[i] + 1))
        
        return max(ans)

        